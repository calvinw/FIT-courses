"""Draw ATMWithdrawals-1.svg, -2.svg, -3.svg: a dotplot of the withdrawals at each ATM machine.

Run from this folder: python3 make_atm_dotplots.py
"""
from collections import Counter

MACHINES = {
    "Machine 1": {40: 25, 100: 25},
    "Machine 2": {20: 2, 30: 8, 40: 1, 50: 9, 60: 2, 70: 6, 80: 2, 90: 9, 100: 1, 110: 8, 120: 2},
    "Machine 3": {20: 9, 70: 32, 120: 9},
}

WIDTH = 900
MARGIN = 40
LO, HI, STEP = 10, 130, 10  # same axis for all three so they can be compared
DOT = 11                    # vertical spacing between stacked dots
RADIUS = 5
COLOR = "#b5121b"
ROWS = max(max(c.values()) for c in MACHINES.values())  # same height for every panel
PANEL_H = 20 + ROWS * DOT + 10 + 45


def x(v):
    return MARGIN + (v - LO) / (HI - LO) * (WIDTH - 2 * MARGIN)


def panel(counts):
    axis_y = 20 + ROWS * DOT + 10
    parts = [
        f'<line x1="{MARGIN}" y1="{axis_y}" x2="{WIDTH - MARGIN}" y2="{axis_y}" stroke="#333" stroke-width="2"/>',
    ]
    for t in range(LO, HI + 1, STEP):
        parts.append(f'<line x1="{x(t):.1f}" y1="{axis_y}" x2="{x(t):.1f}" y2="{axis_y + 8}" stroke="#333" stroke-width="2"/>')
        parts.append(f'<text x="{x(t):.1f}" y="{axis_y + 30}" font-size="18" text-anchor="middle" fill="#333">${t}</text>')
    for v, n in counts.items():
        for i in range(n):
            cy = axis_y - DOT / 2 - 3 - i * DOT
            parts.append(f'<circle cx="{x(v):.1f}" cy="{cy:.1f}" r="{RADIUS}" fill="{COLOR}"/>')
    return parts


for k, counts in enumerate(MACHINES.values(), start=1):
    assert sum(counts.values()) == 50
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {PANEL_H}" '
        f'width="{WIDTH}" height="{PANEL_H}" font-family="sans-serif">',
        f'<rect width="{WIDTH}" height="{PANEL_H}" fill="white"/>',
    ]
    parts += panel(Counter(counts))
    parts.append("</svg>")
    with open(f"ATMWithdrawals-{k}.svg", "w") as f:
        f.write("\n".join(parts))
