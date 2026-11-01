"""Draw the SVGs used in the Backwards Problems lecture.

Run from this folder: python3 make_backwards.py
"""
import math

from make_normal import CENTER, COLOR, SHADE, area_left, normal_svg, write
from make_normal_table import CELL_W, FIRST_W, ROW_H, WIDTH, table_svg

FLOW_W = 900
FLOW_H = 170
BOX_W = 190
BOX_H = 80
BOX_Y = 60


def mini_curve(cx, cy, w, h):
    """Small normal curve with its left tail shaded, centered at (cx, cy)."""
    pts = [(cx - w / 2 + w * i / 60, cy + h / 2 - h * math.exp(-((i - 30) / 10) ** 2 / 2)) for i in range(61)]
    shade = [p for p in pts if p[0] <= cx + w * 0.12]
    path = f"M {shade[0][0]:.1f} {cy + h / 2} " + " ".join(f"L {x:.1f} {y:.1f}" for x, y in shade) + f" L {shade[-1][0]:.1f} {cy + h / 2} Z"
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<path d="{path}" fill="{SHADE}"/>'
            f'<polyline points="{line}" fill="none" stroke="#333" stroke-width="2"/>'
            f'<line x1="{cx - w / 2}" y1="{cy + h / 2}" x2="{cx + w / 2}" y2="{cy + h / 2}" stroke="#333" stroke-width="1.5"/>')


def flow_svg(backwards=False, lookup=None):
    """Three boxes x, z, area joined by arrows, pointing right or left.

    lookup replaces the label on the arrow between z and area, e.g. "NORMSINV".
    """
    xs = (40, (FLOW_W - BOX_W) / 2, FLOW_W - 40 - BOX_W)
    boxes = (("x-value", CENTER), ("z-value", COLOR), ("area", "#333"))
    steps = (("x = μ + zσ", "z = (x − μ) / σ"), (lookup or "z-table backwards", lookup or "z-table"))
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {FLOW_W} {FLOW_H}" '
        f'width="{FLOW_W}" height="{FLOW_H}" font-family="sans-serif">',
        f'<rect width="{FLOW_W}" height="{FLOW_H}" fill="white"/>',
        f'<defs><marker id="head" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        f'<path d="M 0 0 L 10 5 L 0 10 Z" fill="#333"/></marker></defs>',
    ]
    for x, (label, color) in zip(xs, boxes):
        parts.append(f'<rect x="{x}" y="{BOX_Y}" width="{BOX_W}" height="{BOX_H}" rx="10" fill="white" stroke="{color}" stroke-width="3"/>')
        if label == "area":
            parts.append(mini_curve(x + BOX_W / 2, BOX_Y + BOX_H / 2 - 2, BOX_W - 50, BOX_H - 30))
            parts.append(f'<text x="{x + BOX_W / 2}" y="{BOX_Y + BOX_H + 26}" font-size="20" font-weight="bold" text-anchor="middle" fill="{color}">area</text>')
        else:
            parts.append(f'<text x="{x + BOX_W / 2}" y="{BOX_Y + BOX_H / 2 + 9}" font-size="26" font-weight="bold" text-anchor="middle" fill="{color}">{label}</text>')
    for i, (back, fwd) in enumerate(steps):
        a, b = xs[i] + BOX_W + 8, xs[i + 1] - 8
        if backwards:
            a, b = b, a
        y = BOX_Y + BOX_H / 2
        parts.append(f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}" stroke="#333" stroke-width="3" marker-end="url(#head)"/>')
        parts.append(f'<text x="{(a + b) / 2}" y="{BOX_Y - 16}" font-size="20" text-anchor="middle" fill="#333">{back if backwards else fwd}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def badge(x, y, n):
    """Numbered circle marking the order of a step."""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{COLOR}"/>'
            f'<text x="{x:.1f}" y="{y + 6:.1f}" font-size="17" font-weight="bold" text-anchor="middle" fill="white">{n}</text>')


def steps_svg(rows, caption, row=None, col=None, order=None, dashed=()):
    """z-table excerpt with a caption under it.

    With row and col set, that row, column and cell are highlighted, and
    order maps "row", "col" and "cell" to step numbers shown in badges.
    Each (row, col) in dashed gets a dashed outline, for the close areas.
    """
    table = table_svg(rows, row, col, show_answer=row is not None)
    inner = table[table.index("\n") + 1:table.rindex("</svg>")]
    height = ROW_H * (len(rows) + 1)
    # Room on the left and top for the row and column badges
    pad = 34
    total = height + 70 + pad
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {WIDTH + pad + 10} {total}" '
        f'width="{WIDTH + pad + 10}" height="{total}" font-family="sans-serif">',
        f'<rect x="{-pad}" y="{-pad}" width="{WIDTH + pad + 10}" height="{total}" fill="white"/>',
        inner,
    ]
    for drow, dcol in dashed:
        y = (rows.index(drow) + 1) * ROW_H
        parts.append(f'<rect x="{FIRST_W + dcol * CELL_W:.1f}" y="{y}" width="{CELL_W:.1f}" height="{ROW_H}" fill="none" stroke="{COLOR}" stroke-width="3" stroke-dasharray="6 4"/>')
    if order:
        r = rows.index(row) + 1
        cell_x = FIRST_W + col * CELL_W
        spots = {"row": (-pad / 2, (r + 0.5) * ROW_H), "col": (cell_x + CELL_W / 2, -pad / 2),
                 "cell": (cell_x + CELL_W - 2, r * ROW_H + 2)}
        for spot, n in order.items():
            parts.append(badge(*spots[spot], n))
    parts.append(f'<text x="{WIDTH / 2}" y="{height + 42}" font-size="24" font-weight="bold" text-anchor="middle" fill="#333">{caption}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def cell(z):
    """Row label and column of z in the table."""
    return f"{z:.2f}"[:-1], round(abs(z) * 100) % 10


def table(name, area, z, other, rows):
    """Write the z-table excerpt three ways for finding z from area: plain,
    with the two areas around it outlined, and with the closest one (z)
    highlighted and the other one (other) still outlined.
    """
    row, col = cell(z)
    a, b = sorted((area_left(z), area_left(other)))
    around = (cell(z), cell(other))
    write(f"ztable-back-{name}.svg", steps_svg(rows, f"Look for the area closest to {area:g}"))
    write(f"ztable-back-{name}-around.svg", steps_svg(rows, f"{area:g} is between {a:.4f} and {b:.4f}".replace("0.", "."), dashed=around))
    write(f"ztable-back-{name}-answer.svg", steps_svg(
        rows, f"area {area_left(z):.4f}  →  row {row}, column .0{col}  →  z = {z:g}".replace("area 0.", "area ."),
        row, col, dashed=around[1:]))
    print(f"  {area:g}: z = {z:g} area {area_left(z):.4f} off {abs(area_left(z) - area):.4f},"
          f" z = {other:g} area {area_left(other):.4f} off {abs(area_left(other) - area):.4f}")


write("backwards-flow-forwards.svg", flow_svg())
write("backwards-flow-backwards.svg", flow_svg(backwards=True))
write("backwards-flow-normsinv.svg", flow_svg(backwards=True, lookup="NORMSINV"))

# Reading the table forwards, for z = 1.37
write("backwards-table-forwards.svg", steps_svg(
    ("1.2", "1.3", "1.4"), "z = 1.37  →  row 1.3, column .07  →  area .9147",
    "1.3", 7, {"row": 1, "col": 2, "cell": 3}))

# Reading the table backwards, for an area of 0.70: look, find the two
# areas around it, pick the closest, then read off z = 0.52
ROWS = ("0.4", "0.5", "0.6")
AROUND = (("0.5", 2), ("0.5", 3))
write("backwards-table-look.svg", steps_svg(ROWS, "Look inside the table for the area closest to 0.70"))
write("backwards-table-around.svg", steps_svg(ROWS, "0.70 is between .6985 and .7019", dashed=AROUND))
write("backwards-table-closest.svg", steps_svg(ROWS, ".6985 is closest to 0.70", "0.5", 2, dashed=AROUND[1:]))
write("backwards-table-backwards.svg", steps_svg(
    ROWS, "area .6985  →  row 0.5, column .02  →  z = 0.52", "0.5", 2, {"cell": 1, "row": 2, "col": 3}))

# Find z: name, side, left tail area looked for, z read from the table,
# the z of the other area it is between, rows shown in the table
for name, side, area, z, other, rows in (
    ("left-25", "left", 0.25, -0.67, -0.68, ("-0.7", "-0.6", "-0.5")),
    ("right-18", "right", 0.82, 0.92, 0.91, ("0.8", "0.9", "1.0")),
):
    shade = {"hi": z} if side == "left" else {"lo": z}
    write(f"normal-back-{name}.svg", normal_svg(**shade, ticks=(z,), labels=("z = ?",)))
    write(f"normal-back-{name}-answer.svg", normal_svg(**shade, ticks=(z,), named=True))
    table(name, area, z, other, rows)

# Find x: the same, plus mu and sigma
for name, side, mu, sigma, area, z, other, rows in (
    ("x-left-25", "left", 18, 3, 0.25, -0.67, -0.68, ("-0.7", "-0.6", "-0.5")),
    ("x-right-15", "right", 23, 4, 0.85, 1.04, 1.03, ("0.9", "1.0", "1.1")),
    ("x-left-10", "left", 257, 45, 0.10, -1.28, -1.29, ("-1.3", "-1.2", "-1.1")),
    ("x-left-95", "left", 340, 80, 0.95, 1.64, 1.65, ("1.5", "1.6", "1.7")),
):
    x = round(mu + z * sigma, 2)
    zshade = {"hi": z} if side == "left" else {"lo": z}
    xshade = {"hi": x} if side == "left" else {"lo": x}
    write(f"normal-back-{name}.svg", normal_svg(**xshade, ticks=(x,), mu=mu, sigma=sigma, labels=("x = ?",)))
    write(f"normal-back-{name}-z.svg", normal_svg(**zshade, ticks=(z,), labels=("z = ?",)))
    write(f"normal-back-{name}-answer.svg", normal_svg(**xshade, ticks=(x,), mu=mu, sigma=sigma))
    print(f"{name}: z = {z:g}, x = {x:g}")
    table(name, area, z, other, rows)
