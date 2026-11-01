"""Draw the SVGs used in the Types of Normal Problems lecture.

Run from this folder: python3 make_problem_types.py
"""
from make_normal import AXIS_Y, normal_svg, px, write

LABEL = "#333"


def problem_svg(side, mu, sigma, x, area=None):
    """x-curve with one tail shaded and a tag pointing into the shaded area.

    Forwards problems pass area=None: x is known and the tag reads
    "left tail area = ?" (or right).
    Backwards problems pass the area: the tick reads "x = ?" instead of x.
    """
    shade = {"hi": x} if side == "left" else {"lo": x}
    labels = None if area is None else ("x = ?",)
    svg = normal_svg(**shade, ticks=(x,), mu=mu, sigma=sigma, labels=labels)
    z = (x - mu) / sigma
    step = -1 if side == "left" else 1
    # A point inside the shaded tail, clear of the x tag on the boundary,
    # and the area tag up and away from the curve
    tip_x = px(z + 0.65 * step)
    tip_y = AXIS_Y - 6
    text = f"{side} tail area = " + ("?" if area is None else f"{area:.2f}")
    w = 11 * len(text) + 24
    tag_x = min(max(px(z + 1.4 * step), w / 2 + 10), 890 - w / 2)
    tag = (
        f'<line x1="{tag_x:.1f}" y1="112" x2="{tip_x:.1f}" y2="{tip_y}" stroke="{LABEL}" stroke-width="2"/>'
        f'<circle cx="{tip_x:.1f}" cy="{tip_y}" r="4" fill="{LABEL}"/>'
        f'<rect x="{tag_x - w / 2:.1f}" y="80" width="{w}" height="34" rx="6" fill="white" stroke="{LABEL}" stroke-width="2"/>'
        f'<text x="{tag_x:.1f}" y="105" font-size="22" font-weight="bold" text-anchor="middle" fill="{LABEL}">{text}</text>'
    )
    return svg.replace("</svg>", tag + "\n</svg>")


# name, side, mu, sigma, x, and the area for backwards problems
PROBLEMS = (
    ("fwd-left-1", "left", 230, 25, 200, None),
    ("fwd-left-2", "left", 4.2, 0.8, 3, None),
    ("fwd-right-1", "right", 480, 60, 550, None),
    ("fwd-right-2", "right", 65, 15, 90, None),
    ("back-left-1", "left", 120, 18, 97, 0.10),
    ("back-left-2", "left", 5, 1.2, 3, 0.05),
    ("back-right-1", "right", 230, 25, 271, 0.05),
    ("back-right-2", "right", 65, 15, 78, 0.20),
)

if __name__ == "__main__":
    for name, side, mu, sigma, x, area in PROBLEMS:
        write(f"types-{name}.svg", problem_svg(side, mu, sigma, x, area))
