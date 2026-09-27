"""Draw the dotplot SVGs used in the Dotplots lecture.

Run from this folder: python3 make_dotplots.py
"""
import random
import re
from collections import Counter

PLOTS = {
    "dotplot-simple": [6, 8, 8, 9, 5, 6, 8],
    "dotplot-two-peaks": [7, 11, 5, 7, 12, 12, 4, 14, 4, 13, 9, 12, 3, 4, 2, 13, 10, 12, 3, 4],
    "dotplot-no-peaks": [12, 29, 18, 14, 22, 28, 5, 24, 6, 10],
    "dotplot-range": [30, 29, 22, 26, 32, 32, 23, 28, 20, 28, 37, 35, 29, 36, 34],
    "dotplot-clusters": [3, 12, 11, 13, 14, 25, 26, 27, 45, 46, 44, 52],
    "dotplot-demand": [38, 46, 58, 36, 44, 46, 51, 43, 61, 44, 48, 53, 42, 37, 59, 27, 52, 45,
                       53, 48, 62, 35, 58, 61, 45, 25, 49, 40, 51, 47, 51, 48, 54, 43, 39, 40],
}

# Four random dotplots for the Dotplot Examples slide (fixed seed so they stay the same)
rng = random.Random(222)
PLOTS["dotplot-example-1"] = [round(rng.gauss(10, 2)) for _ in range(25)]
PLOTS["dotplot-example-2"] = [min(round(rng.expovariate(1 / 3)), 16) for _ in range(25)]
PLOTS["dotplot-example-3"] = [round(rng.gauss(5, 1.3)) for _ in range(13)] + [round(rng.gauss(14, 1.3)) for _ in range(13)]
PLOTS["dotplot-example-4"] = rng.sample(range(1, 11), 6)  # every value different: all stacks one dot

WIDTH = 900
MARGIN = 40
DOT = 22          # vertical spacing between stacked dots
RADIUS = 8
COLOR = "#b5121b"


def tick_step(lo, hi):
    span = hi - lo
    for step in (1, 2, 5, 10):
        if span / step <= 20:
            return step
    return 20


def svg(values, width=WIDTH, stack_rows=None):
    """Dotplot SVG. stack_rows fixes the room above the axis so several plots match in size."""
    counts = Counter(values)
    step = tick_step(min(values), max(values))
    lo = (min(values) // step) * step - (step if step > 1 else 1)
    hi = -(-max(values) // step) * step + (step if step > 1 else 1)
    tallest = stack_rows or max(counts.values())
    axis_y = MARGIN + tallest * DOT + 10
    height = axis_y + 45

    def x(v):
        return MARGIN + (v - lo) / (hi - lo) * (width - 2 * MARGIN)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" font-family="sans-serif">',
        f'<rect width="{width}" height="{height}" fill="white"/>',
        f'<line x1="{MARGIN}" y1="{axis_y}" x2="{width - MARGIN}" y2="{axis_y}" stroke="#333" stroke-width="2"/>',
    ]
    for t in range(int(lo), int(hi) + 1, step):
        if t < 0 <= min(values):
            continue
        parts.append(f'<line x1="{x(t):.1f}" y1="{axis_y}" x2="{x(t):.1f}" y2="{axis_y + 8}" stroke="#333" stroke-width="2"/>')
        parts.append(f'<text x="{x(t):.1f}" y="{axis_y + 30}" font-size="20" text-anchor="middle" fill="#333">{t}</text>')
    for v, n in counts.items():
        for i in range(n):
            cy = axis_y - DOT / 2 - 4 - i * DOT
            parts.append(f'<circle cx="{x(v):.1f}" cy="{cy:.1f}" r="{RADIUS}" fill="{COLOR}"/>')
    parts.append("</svg>")
    return "\n".join(parts)


MARK_H = 26      # height of one tally mark
MARK_GAP = 7     # space between marks in a group
GROUP_GAP = 12   # space between groups of five
MAX_COLS = 26    # widest tally table before it wraps to another row


def tally_marks(count, x0, y0):
    """Tally marks for count starting at (x0, y0), the top left. Returns (svg parts, width)."""
    parts = []
    x = x0
    while count > 0:
        n = min(count, 5)
        for i in range(min(n, 4)):
            xi = x + i * MARK_GAP
            parts.append(f'<line x1="{xi}" y1="{y0}" x2="{xi}" y2="{y0 + MARK_H}" stroke="#222" stroke-width="2.5" stroke-linecap="round"/>')
        if n == 5:
            parts.append(f'<line x1="{x - 4}" y1="{y0 + MARK_H - 4}" x2="{x + 3 * MARK_GAP + 4}" y2="{y0 + 4}" stroke="#222" stroke-width="2.5" stroke-linecap="round"/>')
        count -= n
        if count > 0:
            x += 3 * MARK_GAP + GROUP_GAP
        else:
            x += (min(n, 4) - 1) * MARK_GAP
    return parts, x - x0


def table_svg(rows, counts, labels=("Data Value", "Tally", "Count"), show_count=True):
    """A small table: one column per entry, rows of value / tally marks / count."""
    col_w = max(34, max(tally_marks(c, 0, 0)[1] for c in counts) + 20)
    head_w = 115
    width = head_w + col_w * len(rows)
    row_h = [34, MARK_H + 18] + ([34] if show_count else [])
    height = sum(row_h)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" font-family="sans-serif">',
        f'<rect width="{width}" height="{height}" fill="white"/>',
    ]
    y = 0
    for r, h in enumerate(row_h):
        parts.append(f'<text x="8" y="{y + h / 2 + 7}" font-size="18" font-weight="bold" fill="#333">{labels[r]}</text>')
        y += h
        if r < len(row_h) - 1:
            parts.append(f'<line x1="0" y1="{y}" x2="{width}" y2="{y}" stroke="#bbb"/>')
    for i, (v, c) in enumerate(zip(rows, counts)):
        cx = head_w + i * col_w + col_w / 2
        parts.append(f'<line x1="{head_w + i * col_w}" y1="0" x2="{head_w + i * col_w}" y2="{height}" stroke="#bbb"/>')
        parts.append(f'<text x="{cx}" y="{row_h[0] / 2 + 7}" font-size="18" text-anchor="middle" fill="#333">{v}</text>')
        marks, w = tally_marks(c, 0, 0)
        dx = cx - w / 2
        dy = row_h[0] + 9
        parts.append(f'<g transform="translate({dx:.1f},{dy})">' + "".join(marks) + "</g>")
        if show_count:
            parts.append(f'<text x="{cx}" y="{row_h[0] + row_h[1] + row_h[2] / 2 + 7}" font-size="18" text-anchor="middle" fill="{COLOR}" font-weight="bold">{c}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def tally_svg(values):
    counts = Counter(values)
    keys = list(range(min(values), max(values) + 1))
    # Wide ranges wrap onto more than one row so the labels stay readable
    rows = -(-len(keys) // MAX_COLS)
    per_row = -(-len(keys) // rows)
    chunks = [keys[i:i + per_row] for i in range(0, len(keys), per_row)]
    if len(chunks) == 1:
        return table_svg(keys, [counts[k] for k in keys], show_count=False)
    tables = [table_svg(c, [counts[k] for k in c], show_count=False) for c in chunks]
    sizes = [(int(re.search(r'width="(\d+)"', t).group(1)), int(re.search(r'height="(\d+)"', t).group(1))) for t in tables]
    width = max(w for w, _ in sizes)
    gap = 16
    height = sum(h for _, h in sizes) + gap * (len(tables) - 1)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
             f'width="{width}" height="{height}" font-family="sans-serif">',
             f'<rect width="{width}" height="{height}" fill="white"/>']
    y = 0
    for t, (_, h) in zip(tables, sizes):
        parts.append(f'<g transform="translate(0,{y})">' + t.replace('xmlns="http://www.w3.org/2000/svg" ', '') + '</g>')
        y += h + gap
    parts.append("</svg>")
    return "\n".join(parts)


# The example plots share one size so they line up in a 2 x 2 grid
EXAMPLES = [n for n in PLOTS if n.startswith("dotplot-example")]
EXAMPLE_ROWS = max(max(Counter(PLOTS[n]).values()) for n in EXAMPLES)

for name, values in PLOTS.items():
    if name in EXAMPLES:
        with open(f"{name}.svg", "w") as f:
            f.write(svg(values, width=600, stack_rows=EXAMPLE_ROWS) + "\n")
        continue
    with open(f"{name}.svg", "w") as f:
        f.write(svg(values) + "\n")
    with open(f"{name.replace('dotplot', 'tally')}.svg", "w") as f:
        f.write(tally_svg(values) + "\n")

# Example tally for the Tally Marks slide: data values 1 through 7, some empty
EXAMPLE_TALLY = [3, 0, 6, 1, 0, 4, 1]
with open("tally-counting.svg", "w") as f:
    f.write(table_svg(list(range(1, 8)), EXAMPLE_TALLY, show_count=False) + "\n")
