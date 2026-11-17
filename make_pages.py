"""Builds the Mental Math web pages (privacy policy and support) for both apps:
Mental Math for Learners (free) and Mental Math for Teachers (paid).

Edit the text below, then run:  python make_pages.py
Pages:  index.html (links to everything), privacy.html, support.html, style.css.
The app icons (logo-learners.png, logo-teachers.png) are copied in by hand from the app's assets, at 180x180.
"""

import html
from pathlib import Path

CONTACT_EMAIL = "support@dailynumbergames.com"  # the only contact on the pages
UPDATED = "16 November 2026"
APPS = [
    ("learners", "Mental Math for Learners", "Free. Learn 80 mental math tricks, practise them, then race the clock in timed contests."),
    ("teachers", "Mental Math for Teachers", "Everything in the Learners app, plus random contests of up to 1000 problems, "
                                             "printed as PDF test papers with answer keys."),
]

PRIVACY = [
    ("Mental Math collects no data", [
        "Mental Math for Learners and Mental Math for Teachers do not collect, store or share any personal information. "
        "There are no accounts, no ads, no analytics and no tracking, and the apps contain no third-party code that "
        "collects data. They do not use the internet at all.",
    ]),
    ("What stays on your device", [
        "Your practice statistics, contest scores and settings are saved only on your iPhone or iPad. They are never "
        "sent to us or to anyone else. <b>Reset progress</b> on the Progress page clears them, and deleting the app "
        "deletes them.",
    ]),
    ("Printed tests (Mental Math for Teachers)", [
        "Test papers and answer keys are made as PDF files on your device. They go only where you send them from the "
        "share sheet (a printer, Files, AirDrop, Mail and so on); we never see them.",
    ]),
    ("Purchases", [
        "Mental Math for Learners is free. Mental Math for Teachers is bought once from Apple's App Store; Apple handles "
        "the payment and we never see your payment details or your Apple Account. Neither app has in-app purchases.",
        "Apple's own privacy policy applies to the App Store: <a href=\"https://www.apple.com/legal/privacy/\">apple.com/legal/privacy</a>.",
    ]),
    ("Links", [
        "A note at the bottom of some pages opens the App Store page of our other app, Hexagon Logic Puzzles. "
        "It is the only link out of the apps.",
    ]),
    ("Children", [
        "Both apps are suitable for all ages. Because they collect no data at all, they collect none from children either.",
    ]),
    ("Changes", [
        "If this policy changes, the new version will be posted on this page with a new date.",
    ]),
]

FAQ_INTRO = "Answers to common questions about Mental Math for Learners and Mental Math for Teachers."
FAQ = [
    ("What is the difference between the two apps?",
     "<b>Mental Math for Learners</b> is free: lessons for 80 tricks, practice with hints, 20 fixed timed contests and "
     "your progress. <b>Mental Math for Teachers</b> has all of that, plus random contests of up to 1000 problems and "
     "60 minutes, and exports any contest as a printable PDF test paper and answer key."),
    ("How do I type a fraction, a mixed number or a negative answer?",
     "Use the app's own keypad: it has keys for the fraction bar, the space in a mixed number, the decimal point and "
     "the minus sign. Fractions are accepted in lowest terms."),
    ("How is a contest scored?",
     "You choose the points for a correct answer, a wrong answer and a skipped problem before you start. A problem "
     "left blank before your last answer counts as skipped; problems after your last answer were not reached and do "
     "not count. Estimation problems accept any answer within a range around the exact value."),
    ("How do I make and print a test? (Teachers)",
     "Open <b>Contest</b>, tap <b>Random</b>, and set the number of questions and minutes. <b>New problems</b> draws "
     "a different test. Tap <b>Export</b> next to Start, choose the layout and the paper size, then <b>Test paper</b> or "
     "<b>Answer key</b>, and print or save the PDF from the share sheet. Fixed contests can be exported the same way."),
    ("How do I match a paper with its answer key? (Teachers)",
     "Every page of the paper and of the key shows the same test ID. The same contest settings always give the same "
     "problems until you tap <b>New problems</b>, so you can export the key later."),
    ("How do I start my statistics again?",
     "Open <b>Progress</b> and tap <b>Reset progress</b>. This forgets all practice statistics and contest scores."),
    ("I deleted the app and my progress is gone.",
     "Progress is kept only on your device and is not copied anywhere, so deleting the app removes it."),
    ("Does Mental Math for Teachers work on my other devices?",
     "Yes, on every iPhone and iPad signed in with the same Apple Account, at no extra cost. Download it again from "
     "the App Store's <b>Purchased</b> list."),
    ("How do I ask for a refund?",
     "Refunds are handled by Apple: visit <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>."),
]

STYLE = """
:root { --bg: #0f1726; --card: #172238; --text: #e6ecf7; --dim: #9aa8bf; --accent: #6fa3ff; --green: #4cc38a; --line: #2a3a58; }
@media (prefers-color-scheme: light) {
  :root { --bg: #f3f6fb; --card: #ffffff; --text: #1b2433; --dim: #5d6a80; --accent: #2f6fde; --green: #1e8e5a; --line: #dce3ef; }
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text); font: 17px/1.6 -apple-system, "Segoe UI", sans-serif; }
main { max-width: 720px; margin: 0 auto; padding: 32px 16px 64px; }
header { display: flex; align-items: center; gap: 14px; margin-bottom: 8px; flex-wrap: wrap; }
header .icons { display: flex; gap: 8px; }
header img { width: 56px; height: 56px; border-radius: 12.5px; }
h1 { font: 800 30px/1.2 -apple-system, "Segoe UI", sans-serif; margin: 0; }
h2 { font-size: 19px; margin: 28px 0 6px; color: var(--accent); }
a { color: var(--accent); }
nav { display: flex; flex-wrap: wrap; gap: 6px 14px; margin: 14px 0 22px; font-size: 15px; }
nav a { text-decoration: none; }
nav a.on { color: var(--text); font-weight: 600; }
.dim { color: var(--dim); font-size: 14px; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 2px 18px 4px; margin: 14px 0; }
.card h2 { margin-top: 14px; }
.app { display: flex; gap: 16px; align-items: flex-start; padding: 16px 18px; }
.app img { width: 64px; height: 64px; border-radius: 14px; flex: none; }
.app h2 { margin: 0 0 4px; }
.app.teachers h2 { color: var(--green); }
.app p { margin: 0 0 6px; }
"""

ICONS = '<span class="icons"><img src="logo-learners.png" alt=""><img src="logo-teachers.png" alt=""></span>'


def shell(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="icon" href="logo-learners.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


def page(kind: str) -> str:
    title = "Privacy Policy" if kind == "privacy" else "Support"
    other, other_title = ("support", "Support") if kind == "privacy" else ("privacy", "Privacy Policy")
    body = [f"<header>{ICONS}<h1>Mental Math · {title}</h1></header>",
            f'<nav><a href="index.html">Mental Math</a> · <a href="{other}.html">{other_title}</a></nav>']
    if kind == "privacy":
        body.append(f'<p class="dim">Last updated: {UPDATED}. This policy covers both apps.</p>')
        for h, paras in PRIVACY:
            body.append(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in paras))
    else:
        body.append(f"<p>{FAQ_INTRO}</p>")
        for q, a in FAQ:
            body.append(f'<div class="card"><h2>{q}</h2><p>{a}</p></div>')
    mail = f'<a href="mailto:{CONTACT_EMAIL}">{html.escape(CONTACT_EMAIL)}</a>'
    body.append(f"<h2>Contact</h2><p>Questions or problems? Write to {mail}. Please say which app you use.</p>")
    return shell(f"Mental Math · {title}", "\n".join(body))


def index() -> str:
    rows = "".join(
        f'<div class="card app {key}"><img src="logo-{key}.png" alt=""><div><h2>{name}</h2><p>{blurb}</p>'
        f'<p><a href="privacy.html">Privacy Policy</a> · <a href="support.html">Support</a></p></div></div>'
        for key, name, blurb in APPS
    )
    return shell("Mental Math", f"<header>{ICONS}<h1>Mental Math</h1></header>\n<p>Mental arithmetic apps for iPhone and iPad.</p>\n{rows}")


if __name__ == "__main__":
    here = Path(__file__).parent
    (here / "style.css").write_text(STYLE.lstrip(), encoding="utf-8")
    (here / "index.html").write_text(index(), encoding="utf-8")
    for kind in ("privacy", "support"):
        (here / f"{kind}.html").write_text(page(kind), encoding="utf-8")
    print("pages written")
