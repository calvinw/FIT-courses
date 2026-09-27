"""Build github-compare.svg with small copies of the repo, codespaces, and pages
pictures inlined as nested <svg> elements (so it works when loaded via <img>)."""
import re, sys
from pathlib import Path

d = Path(sys.argv[1])

def inner(name):
    s = (d / name).read_text()
    return re.search(r'<svg[^>]*>(.*)</svg>', s, re.S).group(1)

# (file, crop viewBox) -- crop to the main picture in each image
thumbs = {
    "codespace": ("github-codespaces.svg", "498 186 724 444"),
    "repo":      ("github-repo.svg",       "58 138 724 534"),
    "pages":     ("github-pages.svg",      "608 212 614 384"),
}

def thumb(key, x, y, w, h):
    f, vb = thumbs[key]
    # fit the crop's aspect ratio inside the box so nothing outside the crop shows
    _, _, vw, vh = map(float, vb.split())
    scale = min(w / vw, h / vh)
    tw, th = vw * scale, vh * scale
    x, y = x + (w - tw) / 2, y + (h - th) / 2
    return (f'<svg x="{x:.1f}" y="{y:.1f}" width="{tw:.1f}" height="{th:.1f}" viewBox="{vb}" '
            f'overflow="hidden">{inner(f)}</svg>')

cards = [
    # key, x, color, name, tagline (pre, bold, post), rows
    ("codespace", 30, "#8250df", "GitHub Codespace", ("Where you ", "WORK", " on files"),
     [("WHAT IT IS", ["A computer GitHub runs for you,", "with VS Code in a browser tab"]),
      ("WHO CAN SEE IT", ["Only you"])]),
    ("repo", 490, "#0969da", "GitHub Repo", ("Where the files ", "LIVE", ""),
     [("WHAT IT IS", ["A project folder that keeps", "every version of its files"]),
      ("ADDRESS", ["https://github.com/", "calvinw/BusMgmtBenchmarks"]),
      ("WHO CAN SEE IT", ["Public: anyone", "Private: you + collaborators"])]),
    ("pages", 950, "#1a7f37", "GitHub Pages", ("Where the website is ", "SHOWN", ""),
     [("WHAT IT IS", ["A free website made from", "the repository's files"]),
      ("ADDRESS", ["https://calvinw.github.io/", "BusMgmtBenchmarks/"]),
      ("WHO CAN SEE IT", ["Anyone on the internet"])]),
]

W = 300
out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" font-family="Helvetica, Arial, sans-serif">',
       '<defs>' + ''.join(
           f'<marker id="arrow{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
           f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>'
           for n, c in [("Purple", "#8250df"), ("Blue", "#0969da"), ("Green", "#1a7f37")]) + '</defs>',
       '<rect width="1280" height="720" fill="#ffffff"/>',
       '<text x="640" y="58" font-size="36" font-weight="bold" fill="#24292f" text-anchor="middle">GitHub Codespaces, Repos, and Pages</text>',
       '<text x="640" y="92" font-size="20" fill="#57606a" text-anchor="middle">Three parts of GitHub that work together on one project</text>']

top, head_h, card_h = 118, 42, 580
for key, x, color, name, (pre, bold, post), rows in cards:
    cx = x + W / 2
    out.append(f'<rect x="{x}" y="{top}" width="{W}" height="{card_h}" rx="12" fill="#ffffff" stroke="{color}" stroke-width="3"/>')
    out.append(f'<path d="M{x+1.5} {top+12} a10.5 10.5 0 0 1 10.5 -10.5 h{W-24} a10.5 10.5 0 0 1 10.5 10.5 v{head_h-10.5} h-{W-3} z" fill="{color}"/>')
    out.append(f'<text x="{cx}" y="{top+30}" font-size="23" font-weight="bold" fill="#ffffff" text-anchor="middle">{name}</text>')
    # thumbnail in a light frame
    ty = top + head_h + 14
    out.append(f'<rect x="{x+16}" y="{ty}" width="{W-32}" height="200" rx="8" fill="#f6f8fa" stroke="#d0d7de"/>')
    out.append(thumb(key, x + 24, ty + 8, W - 48, 184))
    y = ty + 236
    out.append(f'<text x="{cx}" y="{y}" font-size="19" fill="#24292f" text-anchor="middle">{pre}<tspan font-weight="bold" fill="{color}">{bold}</tspan>{post}</text>')
    y += 22
    for label, lines in rows:
        out.append(f'<line x1="{x+22}" y1="{y}" x2="{x+W-22}" y2="{y}" stroke="#d0d7de" stroke-width="1.5"/>')
        y += 24
        out.append(f'<text x="{x+22}" y="{y}" font-size="13" font-weight="bold" letter-spacing="1" fill="#57606a">{label}</text>')
        for ln in lines:
            y += 23
            mono = label == "ADDRESS"
            fam = ' font-family="Menlo, Consolas, monospace" font-size="14"' if mono else ' font-size="16"'
            out.append(f'<text x="{x+22}" y="{y}"{fam} fill="#24292f">{ln}</text>')
        y += 14

# arrows between cards, with the steps written on them
def label(cx, y, lines, bold_first=True, color="#24292f"):
    for k, ln in enumerate(lines):
        w = ' font-weight="bold"' if (k == 0 and bold_first) else ''
        out.append(f'<text x="{cx}" y="{y + k*18}" font-size="14"{w} fill="{color}" text-anchor="middle">{ln}</text>')

gx1, gx2 = 30 + W + 10, 490 - 10          # gap between Codespace and Repo
gc = (gx1 + gx2) / 2
label(gc, 190, ["1. Create codespace", "on branch"], color="#8250df")
out.append(f'<line x1="{gx2}" y1="230" x2="{gx1}" y2="230" stroke="#8250df" stroke-width="4" marker-end="url(#arrowPurple)"/>')
out.append(f'<rect x="{gx1+8}" y="262" width="{gx2-gx1-16}" height="50" rx="8" fill="#fbefff" stroke="#8250df" stroke-dasharray="4 3"/>')
label(gc, 283, ["2. Make changes", "to files"], color="#8250df")
label(gc, 342, ["3. Commit &amp; push to", "remote repo"], color="#0969da")
out.append(f'<line x1="{gx1}" y1="382" x2="{gx2}" y2="382" stroke="#0969da" stroke-width="4" marker-end="url(#arrowBlue)"/>')

px1, px2 = 490 + W + 10, 950 - 10         # gap between Repo and Pages
pc = (px1 + px2) / 2
label(pc, 236, ["Rebuilds and", "publishes on commit", "to the repo"], bold_first=False, color="#1a7f37")
out.append(f'<line x1="{px1}" y1="296" x2="{px2}" y2="296" stroke="#1a7f37" stroke-width="4" marker-end="url(#arrowGreen)"/>')
out.append('</svg>')
(d / "github-compare.svg").write_text("\n".join(out) + "\n")
