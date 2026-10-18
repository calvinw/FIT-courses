"""Draw the SVGs used in the Standard Normal Curve lecture.

Run from this folder: python3 make_normal.py
"""
import math

WIDTH = 900
HEIGHT = 340
MARGIN = 60
AXIS_Y = 270
TOP = 30
COLOR = "#b5121b"
CENTER = "#1f5fa8"
SHADE = "#9ab8de"
ZMAX = 3.5


def density(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def area_left(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def px(z):
    return MARGIN + (z + ZMAX) / (2 * ZMAX) * (WIDTH - 2 * MARGIN)


def py(z):
    return AXIS_Y - density(z) / density(0) * (AXIS_Y - TOP)


def curve_points(lo, hi, steps=200):
    return [(px(lo + (hi - lo) * i / steps), py(lo + (hi - lo) * i / steps)) for i in range(steps + 1)]


def normal_svg(lo=None, hi=None, ticks=(), mu=None, sigma=None, named=False):
    """Standard normal curve, shaded from z = lo to z = hi.

    lo=None shades the whole left tail and hi=None the whole right tail;
    both None (with no ticks) draws the plain curve. Each z in ticks is
    labeled in bold red under the axis.

    With named=True each tick label reads "z = -0.86" in a red tag under the
    axis, centered on its boundary line.

    With mu and sigma this is an x-curve instead: lo, hi and ticks are
    x-values, and the axis is labeled in x at each whole standard deviation.
    Each tick is labeled "x = 1.23" in a blue tag just above the axis,
    centered on its boundary line.

    z-values are always red and x-values always blue.
    """
    axis = "z" if mu is None else "x"
    color = COLOR if mu is None else CENTER
    labels = {z: f"{z}" for z in range(-3, 4)}
    tick_labels = [f"{axis} = {t:g}" if named or mu is not None else f"{t:g}" for t in ticks]
    if mu is not None:
        def to_z(v):
            return None if v is None else (v - mu) / sigma
        labels = {z: f"{round(mu + z * sigma, 6):g}" for z in range(-3, 4)}
        lo, hi, ticks = to_z(lo), to_z(hi), [to_z(t) for t in ticks]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'width="{WIDTH}" height="{HEIGHT}" font-family="sans-serif">',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="white"/>',
    ]
    if ticks:
        a = -ZMAX if lo is None else lo
        b = ZMAX if hi is None else hi
        pts = curve_points(a, b)
        path = f"M {px(a):.1f} {AXIS_Y} " + " ".join(f"L {x:.1f} {y:.1f}" for x, y in pts) + f" L {px(b):.1f} {AXIS_Y} Z"
        parts.append(f'<path d="{path}" fill="{SHADE}" stroke="none"/>')
        for z in ticks:
            parts.append(f'<line x1="{px(z):.1f}" y1="{AXIS_Y}" x2="{px(z):.1f}" y2="{py(z):.1f}" stroke="#333" stroke-width="2"/>')
    pts = curve_points(-ZMAX, ZMAX)
    parts.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" fill="none" stroke="#333" stroke-width="3"/>')
    parts.append(f'<line x1="{MARGIN - 20}" y1="{AXIS_Y}" x2="{WIDTH - MARGIN + 20}" y2="{AXIS_Y}" stroke="#333" stroke-width="2"/>')
    parts.append(f'<text x="{WIDTH - 25}" y="{AXIS_Y + 30}" font-size="22" font-style="italic" fill="{color}">{axis}</text>')
    for z in range(-3, 4):
        parts.append(f'<line x1="{px(z):.1f}" y1="{AXIS_Y - 6}" x2="{px(z):.1f}" y2="{AXIS_Y + 6}" stroke="#333" stroke-width="2"/>')
        parts.append(f'<text x="{px(z):.1f}" y="{AXIS_Y + 30}" font-size="20" text-anchor="middle" fill="{color}">{labels[z]}</text>')
    for z, label in zip(ticks, tick_labels):
        if mu is None and not named:
            parts.append(f'<text x="{px(z):.1f}" y="{AXIS_Y + 60}" font-size="22" font-weight="bold" text-anchor="middle" fill="{color}">{label}</text>')
            continue
        # A small white tag centered on the boundary line: x above the axis,
        # z below it with the z-values
        w = 13 * len(label) + 14
        top = AXIS_Y - 42 if mu is not None else AXIS_Y + 38
        parts.append(f'<rect x="{px(z) - w / 2:.1f}" y="{top}" width="{w}" height="30" rx="5" fill="white" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<text x="{px(z):.1f}" y="{top + 23}" font-size="22" font-weight="bold" text-anchor="middle" fill="{color}">{label}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def write(name, svg):
    with open(name, "w") as f:
        f.write(svg)


if __name__ == "__main__":
    write("normal-curve.svg", normal_svg())

    # Left tails, right tails, and areas between from the book's examples
    for z in (-1.43, 2.01, 0.18):
        write(f"normal-left-{z:g}.svg", normal_svg(hi=z, ticks=(z,)))
        print(f"left of {z:g}: {area_left(z):.4f}")

    for z in (-1.03, 0.31, 1.89):
        write(f"normal-right-{z:g}.svg", normal_svg(lo=z, ticks=(z,)))
        print(f"right of {z:g}: {1 - area_left(z):.4f}")

    for a, b in ((-1.53, -0.3), (-1.8, 2.01), (-1.05, 1.5)):
        write(f"normal-between-{a:g}-{b:g}.svg", normal_svg(lo=a, hi=b, ticks=(a, b)))
        print(f"between {a:g} and {b:g}: {area_left(b) - area_left(a):.4f}")
