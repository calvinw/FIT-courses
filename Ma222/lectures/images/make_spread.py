"""Draw the SVGs used in the Measures of Spread lecture.

Run from this folder: python3 make_spread.py
"""
from collections import Counter
from statistics import mean, stdev

WIDTH = 900
MARGIN = 40
DOT = 22
RADIUS = 8
COLOR = "#b5121b"
CENTER = "#1f5fa8"


def axis(lo, hi, axis_y, x):
    parts = [f'<line x1="{MARGIN}" y1="{axis_y}" x2="{WIDTH - MARGIN}" y2="{axis_y}" stroke="#333" stroke-width="2"/>']
    for t in range(lo, hi + 1):
        parts.append(f'<line x1="{x(t):.1f}" y1="{axis_y}" x2="{x(t):.1f}" y2="{axis_y + 8}" stroke="#333" stroke-width="2"/>')
        parts.append(f'<text x="{x(t):.1f}" y="{axis_y + 30}" font-size="20" text-anchor="middle" fill="#333">{t}</text>')
    return parts


def header(height):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" '
        f'width="{WIDTH}" height="{height}" font-family="sans-serif">',
        f'<rect width="{WIDTH}" height="{height}" fill="white"/>',
    ]


def std_dev_svg(values, lo, hi):
    """Dotplot with the mean and a band one standard deviation either side."""
    m, s = mean(values), stdev(values)
    counts = Counter(values)
    top = 50
    axis_y = top + max(counts.values()) * DOT + 30
    height = axis_y + 45

    def x(v):
        return MARGIN + (v - lo) / (hi - lo) * (WIDTH - 2 * MARGIN)

    parts = header(height)
    parts.append(f'<rect x="{x(m - s):.1f}" y="{top}" width="{x(m + s) - x(m - s):.1f}" height="{axis_y - top}" fill="{CENTER}" opacity="0.12"/>')
    parts.append(f'<line x1="{x(m):.1f}" y1="{top - 10}" x2="{x(m):.1f}" y2="{axis_y}" stroke="{CENTER}" stroke-width="3" stroke-dasharray="8 6"/>')
    parts.append(f'<text x="{x(m):.1f}" y="{top - 18}" font-size="20" text-anchor="middle" fill="{CENTER}">mean = {m:.2f}</text>')
    arrow_y = top + 14
    for end in (m - s, m + s):
        parts.append(f'<line x1="{x(m):.1f}" y1="{arrow_y}" x2="{x(end):.1f}" y2="{arrow_y}" stroke="{CENTER}" stroke-width="2"/>')
        parts.append(f'<text x="{(x(m) + x(end)) / 2:.1f}" y="{arrow_y - 6}" font-size="17" text-anchor="middle" fill="{CENTER}">{s:.2f}</text>')
    for v, n in counts.items():
        for i in range(n):
            cy = axis_y - DOT / 2 - 4 - i * DOT
            parts.append(f'<circle cx="{x(v):.1f}" cy="{cy:.1f}" r="{RADIUS}" fill="{COLOR}"/>')
    parts += axis(lo, hi, axis_y, x)
    parts.append("</svg>")
    return "\n".join(parts)


with open("spread-std-dev.svg", "w") as f:
    f.write(std_dev_svg([5, 12, 13, 5, 3, 9, 10], 1, 15))
