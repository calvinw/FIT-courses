"""Build the one-page standard normal table (ZTable.html, then ZTable.pdf).

Run from this folder: python3 make_ztable.py
"""
import math
import os
import subprocess

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def area_left(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def table(rows, negative):
    head = "<tr><th>z</th>" + "".join(f"<th>.0{c}</th>" for c in range(10)) + "</tr>"
    body = []
    for i, r in enumerate(rows):
        # Negative rows (including -0.0) go further left with each column
        label = f"-{r:.1f}" if negative else f"{r:.1f}"
        cells = []
        for c in range(10):
            z = -(r + c / 100) if negative else r + c / 100
            cells.append(f"<td>{area_left(z):.4f}".replace("0.", ".", 1) + "</td>")
        # A light band every fifth row keeps the eye on the right row
        cls = ' class="band"' if i % 5 == 4 else ""
        body.append(f"<tr{cls}><th>{label}</th>{''.join(cells)}</tr>")
    return f"<table>{head}{''.join(body)}</table>"


def curve(z0=1.32, width=270, height=110):
    """Small standard normal curve with the left tail of z0 shaded and its area, for the example."""
    base = height - 30

    def px(z):
        return 10 + (z + 3.5) / 7 * (width - 20)

    def py(z):
        return base - math.exp(-z * z / 2) * (base - 6)

    zs = [-3.5 + 7 * i / 140 for i in range(141)]
    line = " ".join(f"{px(z):.1f},{py(z):.1f}" for z in zs)
    tail = [z for z in zs if z <= z0] + [z0]
    shade = f"M {px(-3.5):.1f} {base} " + " ".join(f"L {px(z):.1f} {py(z):.1f}" for z in tail) + f" L {px(z0):.1f} {base} Z"
    return (
        f'<svg viewBox="0 0 {width} {height}" width="{width}" height="{height}" font-family="Helvetica, Arial, sans-serif">'
        f'<path d="{shade}" fill="#d0d0d0"/>'
        f'<line x1="{px(z0):.1f}" y1="{base}" x2="{px(z0):.1f}" y2="{py(z0):.1f}" stroke="#000" stroke-width="1.2"/>'
        f'<polyline points="{line}" fill="none" stroke="#000" stroke-width="1.5"/>'
        f'<line x1="{px(-3.5):.1f}" y1="{base}" x2="{px(3.5):.1f}" y2="{base}" stroke="#000"/>'
        f'<text x="{px(-0.1):.1f}" y="{base - 22}" font-size="14" font-weight="bold" text-anchor="middle">.{round(area_left(z0) * 10000):04d}</text>'
        f'<text x="{px(z0):.1f}" y="{base + 16}" font-size="13" font-weight="bold" text-anchor="middle">z = {z0}</text>'
        "</svg>"
    )


HTML = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Standard Normal Table</title>
<style>
  @page {{ size: letter; margin: 0.4in; }}
  body {{ font-family: Helvetica, Arial, sans-serif; margin: 0; color: #000; }}
  header {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px; }}
  h1 {{ font-size: 17pt; margin: 0 0 3px; }}
  p {{ font-size: 9.5pt; margin: 0; }}
  .example-text {{ margin-top: 5px; }}
  .tables {{ display: flex; gap: 12px; }}
  table {{ border-collapse: collapse; font-size: 9pt; font-variant-numeric: tabular-nums; flex: 1; }}
  th, td {{ padding: 3.3px 2px; text-align: center; border-bottom: 1px solid #ccc; }}
  tr:first-child th {{ border-top: 1.5px solid #000; border-bottom: 1.5px solid #000; }}
  th:first-child {{ border-right: 1.5px solid #000; }}
  tr.band td {{ border-bottom: 1px solid #000; }}
  tr.band th {{ border-bottom: 1px solid #000; }}
</style>
</head>
<body>
<header>
  <div>
  <h1>Standard Normal Table</h1>
  <p>Each entry is the <b>left tail area</b>: the area under the curve to the left of z.</p>
  <p>Row: the ones digit and first decimal of z. Column: the second decimal of z.</p>
  <p class="example-text"><b>Example:</b> z = 1.32 is row 1.3, column .02, so the left tail area is .9066.</p>
  </div>
  {curve()}
</header>
<div class="tables">
  {table([r / 10 for r in range(34, -1, -1)], negative=True)}
  {table([r / 10 for r in range(0, 35)], negative=False)}
</div>
</body>
</html>
"""

with open("ZTable.html", "w") as f:
    f.write(HTML)

subprocess.run(
    [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
     "--print-to-pdf=ZTable.pdf", "file://" + os.path.abspath("ZTable.html")],
    check=True, capture_output=True,
)
