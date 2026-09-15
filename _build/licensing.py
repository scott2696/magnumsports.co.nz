#!/usr/bin/env python3
"""The NZ online casino licensing process, as data.

Single source of truth for every dated claim about the new regime. The
tracker component computes "days remaining" at build time, so a rebuild
keeps the page honest and a stale page is visibly stale rather than
quietly wrong.

Sources (all linked on /licensed-online-casinos/):
  DIA "Online Gambling for Providers" — the three-stage process
  Online Casino Gambling Act 2026 — 15 licences, term, penalties
  Cabinet advertising decisions — affiliate and endorsement prohibition
"""
import datetime

TODAY = datetime.date.today()

# (date, stage, detail, source-ish note)
STAGES = [
    (datetime.date(2026, 7, 17), "Expressions of interest open",
     "DIA opens stage one. NZ$19,000 + GST per expression of interest.", "done"),
    (datetime.date(2026, 8, 14), "Expressions of interest close",
     "Stage one closed. DIA confirmed interest exceeded the 15 licences available, "
     "and will not name who applied.", "done"),
    (datetime.date(2026, 9, 29), "Auction opens",
     "A multi-round simultaneous ascending clock auction. The price rises in steps "
     "until demand matches the 15 licences. Participants are not made public.", "next"),
    (datetime.date(2026, 10, 1), "Full applications open",
     "Successful bidders file business plans, advertising and marketing strategy, "
     "and harm-minimisation measures.", "upcoming"),
    (datetime.date(2026, 12, 1), "Unlicensed operators must stop",
     "Any operator that has not applied must stop offering online casino gambling to "
     "New Zealanders. Those with a pending application may continue without advertising "
     "until it is decided.", "cutoff"),
    (datetime.date(2027, 3, 31), "Licences issued, market live",
     "Government expects the regulated market to be operational in early 2027. "
     "This date is our estimate of the quarter, not a published date.", "estimate"),
]

CUTOFF = datetime.date(2026, 12, 1)
AUCTION = datetime.date(2026, 9, 29)

FACTS = [
    ("Licences available", "15"),
    ("Maximum per operator", "3 (one brand each)"),
    ("Licence term", "3 years, renewable for 5"),
    ("Expression of interest fee", "NZ$19,000 + GST"),
    ("Penalty for unlicensed supply", "Up to NZ$5m (company)"),
    ("Affiliate marketing by licensees", "Prohibited"),
]


def days_to(d):
    return (d - TODAY).days


def status_of(stage_date, kind):
    """Derived, never hand-written, so the page cannot drift out of date."""
    if stage_date <= TODAY:
        return "done"
    if kind == "estimate":
        return "estimate"
    return "next" if stage_date == next_upcoming() else "upcoming"


def next_upcoming():
    future = [d for d, *_ in STAGES if d > TODAY]
    return future[0] if future else None
