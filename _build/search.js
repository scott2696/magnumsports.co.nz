/* Magnum Sports product search. Copied to assets/js/search.js by p_shop.py.

   The site is static, so search runs in the browser against
   /assets/js/search.json (written by the build from the catalogue). The index
   is fetched the first time someone opens search, not on every page load.

   - Header: a search button opens a box with live suggestions; Enter goes to
     the results page.
   - /search/?q=...: the full results as product cards. Add to cart on those
     cards is handled by cart.js, which listens for [data-add] clicks. */
(function () {
  "use strict";
  var INDEX_URL = "/assets/js/search.json";
  var SUGGEST = 8;
  var items = null, loading = null;

  function load() {
    if (items) return Promise.resolve(items);
    if (!loading) {
      loading = fetch(INDEX_URL).then(function (r) { return r.json(); }).then(function (d) {
        items = d.map(function (p) {
          p._n = norm(p.n);
          p._all = norm([p.n, p.d, p.b, p.m, p.s].join(" "));
          return p;
        });
        return items;
      }).catch(function () { loading = null; return []; });
    }
    return loading;
  }

  function norm(s) {
    return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
      .replace(/[^a-z0-9.]+/g, " ").trim();
  }

  // Every word of the query must appear somewhere; name matches rank first,
  // then matches at the start of a word, then shorter names.
  function search(q) {
    var terms = norm(q).split(" ").filter(Boolean);
    if (!terms.length || !items) return [];
    var out = [];
    items.forEach(function (p) {
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var t = terms[i], k = p._all.indexOf(t);
        if (k < 0) return;
        var inName = p._n.indexOf(t);
        if (inName >= 0) score += 10 + ((inName === 0 || p._n[inName - 1] === " ") ? 5 : 0);
        else score += 2;
      }
      out.push({ p: p, score: score - p.n.length / 100 });
    });
    out.sort(function (a, b) { return b.score - a.score; });
    return out.map(function (x) { return x.p; });
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  // No "p" in the index while prices are unconfirmed.
  function money(p) { return p ? "NZ$" + p : "Price on request"; }

  // ------------------------------------------------------------ header box
  function wireHeader() {
    var btn = document.querySelector(".nav-search");
    var panel = document.getElementById("site-search");
    if (!btn || !panel) return;
    var input = panel.querySelector("input[name=q]");
    var list = panel.querySelector(".search-sugg");

    function open() {
      panel.hidden = false;
      btn.setAttribute("aria-expanded", "true");
      input.focus();
      load().then(render);
    }
    function close() {
      panel.hidden = true;
      btn.setAttribute("aria-expanded", "false");
    }
    function render() {
      var q = input.value.trim();
      list.textContent = "";
      if (!q) return;
      var res = search(q);
      if (!res.length) {
        list.innerHTML = '<li class="search-none">No products match &ldquo;' + esc(q) + '&rdquo;.</li>';
        return;
      }
      list.innerHTML = res.slice(0, SUGGEST).map(function (p) {
        return '<li><a href="' + esc(p.u) + '">' +
          (p.i ? '<img src="' + esc(p.i) + '" alt="" width="44" height="44" loading="lazy">'
               : '<span class="search-noimg"></span>') +
          '<span class="search-txt"><b>' + esc(p.n) + '</b><span>' + esc(p.d) + '</span></span>' +
          '<span class="search-price">' + money(p.p) + '</span></a></li>';
      }).join("") + (res.length > SUGGEST
        ? '<li class="search-all"><a href="/search/?q=' + encodeURIComponent(q) + '">See all ' +
          res.length + ' results &rarr;</a></li>' : "");
    }

    btn.addEventListener("click", function () { panel.hidden ? open() : close(); });
    input.addEventListener("input", function () { load().then(render); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !panel.hidden) { close(); btn.focus(); }
      if (e.key === "/" && panel.hidden && !/input|textarea|select/i.test(e.target.tagName)) {
        e.preventDefault(); open();
      }
    });
    document.addEventListener("click", function (e) {
      if (!panel.hidden && !panel.contains(e.target) && !btn.contains(e.target)) close();
    });
  }

  // ---------------------------------------------------------- results page
  function card(p) {
    var cta = p.o
        ? '<a class="btn btn--sm" href="' + esc(p.u) + '">Choose options</a>'
        : '<button class="btn btn--sm" type="button" data-add="' + esc(p.s) + '">' +
          (p.p ? "Add to cart" : "Add to enquiry") + '</button>';
    var media = p.i
      ? '<a class="prod-img" href="' + esc(p.u) + '" tabindex="-1" aria-hidden="true"><img src="' + esc(p.i) +
        '" alt="" width="600" height="600" loading="lazy" decoding="async"></a>'
      : '<a class="prod-img prod-img--empty" href="' + esc(p.u) + '" tabindex="-1" aria-hidden="true"></a>';
    return '<div class="pick prod" data-sku="' + esc(p.s) + '">' + media +
      '<span class="pick-cat">' + esc(p.d) + '</span>' +
      '<div class="pick-brand"><b><a class="prod-link" href="' + esc(p.u) + '">' + esc(p.n) + '</a></b></div>' +
      '<p>' + esc(p.b) + '</p><div class="prod-price' + (p.p ? "" : " prod-price--ask") + '">' + money(p.p) + '</div>' + cta + '</div>';
  }

  function wirePage() {
    var box = document.getElementById("search-results");
    if (!box) return;
    var form = document.getElementById("search-form");
    var input = form.querySelector("input[name=q]");
    var count = document.getElementById("search-count");
    var q = new URLSearchParams(location.search).get("q") || "";
    input.value = q;

    function show() {
      var v = input.value.trim();
      if (!v) {
        count.textContent = "Type what you are after: a product, a colour, a model number.";
        box.innerHTML = "";
        return;
      }
      var res = search(v);
      count.textContent = res.length
        ? res.length + " product" + (res.length === 1 ? "" : "s") + " for “" + v + "”"
        : "No products match “" + v + "”. Try fewer or different words, or ring the shop.";
      box.innerHTML = res.map(card).join("");
      document.title = (v ? v + " | " : "") + "Search | Magnum Sports";
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      history.replaceState(null, "", "?q=" + encodeURIComponent(input.value.trim()));
      show();
    });
    input.addEventListener("input", function () {
      history.replaceState(null, "", "?q=" + encodeURIComponent(input.value.trim()));
      show();
    });
    load().then(show);
    if (!q) input.focus();
  }

  function init() { wireHeader(); wirePage(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
