/* Magnum Sports cart. Built from _build/cart.js by p_shop.py — edit that file,
   not assets/js/cart.js, which is overwritten on every build.

   The cart lives in this browser only (localStorage). Checkout does not take
   payment: it composes an order request and hands it to the customer's email
   app, and the shop replies to confirm stock and payment. Prices and
   names always come from the catalogue baked in below, never from storage. */
(function () {
  "use strict";
  var CAT = /*@@CATALOGUE@@*/{};
  var TO = "/*@@ORDER_EMAIL@@*/";
  // false while prices are unconfirmed: no amounts anywhere, and the order
  // email becomes an enquiry (the catalogue then carries no prices at all).
  var PRICES = /*@@SHOW_PRICES@@*/true;
  var KEY = "ms-cart-v1";

  function load() {
    try {
      var raw = JSON.parse(localStorage.getItem(KEY) || "[]");
      // Drop anything no longer sold, or with an option that has gone.
      return raw.filter(function (l) {
        var p = CAT[l.sku];
        return p && l.qty > 0 &&
          (p.options ? p.options.indexOf(l.opt) > -1 : !l.opt);
      });
    } catch (e) { return []; }
  }
  function save(lines) {
    try { localStorage.setItem(KEY, JSON.stringify(lines)); } catch (e) {}
  }
  function cents(s) { return Math.round(parseFloat(s) * 100); }
  function money(c) {
    return "NZ$" + (c / 100).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }
  function count(lines) {
    return lines.reduce(function (n, l) { return n + l.qty; }, 0);
  }
  function total(lines) {
    return lines.reduce(function (n, l) { return n + cents(CAT[l.sku].price) * l.qty; }, 0);
  }
  function label(l) {
    return CAT[l.sku].name + (l.opt ? " (" + l.opt + ")" : "");
  }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function announce(msg) {
    var live = document.getElementById("cart-live");
    if (live) { live.textContent = ""; setTimeout(function () { live.textContent = msg; }, 50); }
  }

  var lines = load();

  function badge() {
    var n = count(lines);
    document.querySelectorAll("[data-cart-count]").forEach(function (b) {
      b.textContent = n > 99 ? "99+" : String(n);
      b.hidden = n === 0;
    });
    document.querySelectorAll(".nav-cart").forEach(function (a) {
      a.setAttribute("aria-label", n ? "Cart, " + n + " item" + (n === 1 ? "" : "s") : "Cart, empty");
    });
  }

  function update(nextLines, msg) {
    lines = nextLines;
    save(lines);
    badge();
    render();
    document.dispatchEvent(new Event("cart:change"));
    if (msg) announce(msg);
  }

  function add(sku, opt) {
    var found = false;
    var next = lines.map(function (l) {
      if (l.sku === sku && (l.opt || "") === (opt || "")) {
        found = true;
        return { sku: l.sku, opt: l.opt, qty: Math.min(l.qty + 1, 99) };
      }
      return l;
    });
    if (!found) next.push(opt ? { sku: sku, opt: opt, qty: 1 } : { sku: sku, qty: 1 });
    update(next, CAT[sku].name + " added to cart");
  }

  function setQty(i, q) {
    var name = label(lines[i]);
    var next = lines.slice();
    if (q < 1) next.splice(i, 1); else next[i] = { sku: next[i].sku, opt: next[i].opt, qty: Math.min(q, 99) };
    update(next, q < 1 ? name + " removed" : name + ", quantity " + q);
  }

  // ------------------------------------------------------------ cart view
  function render() {
    var box = document.getElementById("cart-lines");
    if (!box) return;
    var form = document.getElementById("order-form");
    box.textContent = "";
    if (!lines.length) {
      box.appendChild(el("p", "cart-empty", PRICES ? "Your cart is empty. Add something from the shelves above."
        : "Your enquiry list is empty. Add products from the departments above."));
      if (form) form.hidden = true;
      return;
    }
    if (form) form.hidden = false;
    var ul = el("ul", "cart-list");
    lines.forEach(function (l, i) {
      var p = CAT[l.sku];
      var li = el("li", "cart-line");
      var info = el("div", "cart-info");
      info.appendChild(el("b", null, p.name));
      if (l.opt) info.appendChild(el("span", "cart-opt", l.opt));
      if (PRICES) info.appendChild(el("span", "cart-each", money(cents(p.price)) + " each"));
      var qty = el("div", "cart-qty");
      var minus = el("button", "cart-step", "−");
      minus.type = "button";
      minus.setAttribute("aria-label", "One fewer " + label(l));
      minus.onclick = function () { setQty(i, l.qty - 1); };
      var n = el("span", "cart-n", String(l.qty));
      var plus = el("button", "cart-step", "+");
      plus.type = "button";
      plus.setAttribute("aria-label", "One more " + label(l));
      plus.onclick = function () { setQty(i, l.qty + 1); };
      qty.append(minus, n, plus);
      var sum = el("span", "cart-sum", PRICES ? money(cents(p.price) * l.qty) : "Price on request");
      var rm = el("button", "cart-rm", "Remove");
      rm.type = "button";
      rm.setAttribute("aria-label", "Remove " + label(l));
      rm.onclick = function () { setQty(i, 0); };
      li.append(info, qty, sum, rm);
      ul.appendChild(li);
    });
    box.appendChild(ul);
    var t = el("div", "cart-total");
    var items = count(lines) + " item" + (count(lines) === 1 ? "" : "s");
    if (PRICES) {
      t.append(el("span", null, "Total (" + items + ")"), el("b", null, money(total(lines))));
    } else {
      t.append(el("span", null, "Enquiry (" + items + ")"), el("b", null, "Prices on request"));
    }
    box.appendChild(t);
    box.appendChild(el("p", "cart-fine", PRICES
      ? "Free delivery anywhere in New Zealand, 7 to 10 days. Prices are in New Zealand dollars and include GST and delivery."
      : "We are confirming prices. Send your enquiry and we reply with prices, stock and how to pay. Free delivery anywhere in New Zealand."));
  }

  // ------------------------------------------------------------ checkout
  function orderText(f) {
    var get = function (n) { return (f.elements[n] && f.elements[n].value || "").trim(); };
    var out = [(PRICES ? "ORDER REQUEST — " : "ENQUIRY — please send prices — ") + location.hostname, ""];
    lines.forEach(function (l) {
      out.push(PRICES
        ? l.qty + " x " + label(l) + "  @ " + money(cents(CAT[l.sku].price)) +
          "  = " + money(cents(CAT[l.sku].price) * l.qty) + "   [" + l.sku + "]"
        : l.qty + " x " + label(l) + "   [" + l.sku + "]");
    });
    out.push("", PRICES ? "Total: " + money(total(lines)) + " (includes GST and delivery)" : "Prices: to be quoted", "",
             "Name: " + get("name"), "Email: " + get("email"), "Phone: " + get("phone"),
             "Deliver to: " + get("address").replace(/\s*\n\s*/g, ", "));
    var pay = f.querySelector("input[name=payment]:checked");
    if (pay) out.push("Payment: " + pay.value);
    if (get("notes")) out.push("", "Notes: " + get("notes"));
    return out.join("\n");
  }

  // Pay now: send SKUs and quantities to the checkout Worker, which prices them
  // from the site's catalogue and returns a Stripe Checkout address.
  function wirePayNow() {
    var btn = document.getElementById("pay-now");
    if (!btn) return;
    var wrap = document.getElementById("pay-now-wrap");
    var err = document.getElementById("pay-now-error");
    var sync = function () { wrap.hidden = !lines.length; };
    sync();
    document.addEventListener("cart:change", sync);
    btn.addEventListener("click", function () {
      if (!lines.length) return;
      var label = btn.innerHTML;
      btn.disabled = true;
      btn.textContent = "Opening secure checkout\u2026";
      err.hidden = true;
      fetch(btn.getAttribute("data-checkout"), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ items: lines.map(function (l) { return { sku: l.sku, qty: l.qty, opt: l.opt || "" }; }) })
      }).then(function (r) { return r.json().then(function (d) { return { ok: r.ok, d: d }; }); })
        .then(function (x) {
          if (x.ok && x.d.url) { location.href = x.d.url; return; }
          throw new Error(x.d.error || "Payment could not be started.");
        })
        .catch(function (e) {
          err.textContent = (e && e.message) || "Payment could not be started. Please try again.";
          err.hidden = false;
          btn.disabled = false;
          btn.innerHTML = label;
        });
    });
  }

  function wireCheckout() {
    var f = document.getElementById("order-form");
    if (!f) return;
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!lines.length) return;
      var text = orderText(f);
      var subject = (PRICES ? "Order request — " : "Enquiry — ") + f.elements.name.value.trim();
      var sent = document.getElementById("order-sent");
      document.getElementById("order-copy").value = text;
      sent.hidden = false;
      sent.scrollIntoView({ behavior: "smooth", block: "start" });
      location.href = "mailto:" + TO + "?subject=" + encodeURIComponent(subject) +
                      "&body=" + encodeURIComponent(text);
    });
    var clear = document.getElementById("order-clear");
    if (clear) clear.onclick = function () {
      update([], "Cart cleared");
      document.getElementById("order-sent").hidden = true;
      f.reset();
    };
    var copy = document.getElementById("order-copy-btn");
    if (copy) copy.onclick = function () {
      var ta = document.getElementById("order-copy");
      ta.select();
      var done = function () { copy.textContent = "Copied"; setTimeout(function () { copy.textContent = "Copy order"; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(ta.value).then(done, function () {});
      else { try { document.execCommand("copy"); done(); } catch (e2) {} }
    };
  }

  // -------------------------------------------------------- add buttons
  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest("[data-add]");
    if (!btn) return;
    var sku = btn.getAttribute("data-add");
    var p = CAT[sku];
    if (!p) return;
    var opt = "";
    if (p.options) {
      var card = btn.closest("[data-sku]");
      var sel = card && card.querySelector("select[data-opt]");
      opt = sel ? sel.value : "";
      if (!opt) {
        if (sel) { sel.focus(); sel.setAttribute("aria-invalid", "true"); }
        announce("Choose an option for " + p.name + " first");
        return;
      }
      sel.removeAttribute("aria-invalid");
    }
    add(sku, opt);
    if (btn._was == null) btn._was = btn.innerHTML;
    btn.textContent = "Added ✓";
    btn.classList.add("is-added");
    clearTimeout(btn._t);
    btn._t = setTimeout(function () {
      btn.innerHTML = btn._was; btn._was = null; btn.classList.remove("is-added");
    }, 1400);
  });

  // Another tab changed the cart: follow it.
  window.addEventListener("storage", function (e) {
    if (e.key === KEY) { lines = load(); badge(); render(); }
  });

  function init() {
    if (!document.getElementById("cart-live")) {
      var live = el("div", "sr-only");
      live.id = "cart-live";
      live.setAttribute("aria-live", "polite");
      document.body.appendChild(live);
    }
    // Back from a paid Stripe checkout: the order is placed, so empty the cart.
    if (document.querySelector("[data-clear-cart]") && lines.length) {
      lines = [];
      save(lines);
    }
    badge();
    render();
    wireCheckout();
    wirePayNow();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
