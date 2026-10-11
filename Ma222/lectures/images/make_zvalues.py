"""Draw the SVGs used in the Z-Values lecture.

Run from this folder: python3 make_zvalues.py
"""
WIDTH = 900
MARGIN = 60
COLOR = "#b5121b"
CENTER = "#1f5fa8"
MARK = "#2a8a3e"


def header(height):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" '
        f'width="{WIDTH}" height="{height}" font-family="sans-serif">',
        f'<rect width="{WIDTH}" height="{height}" fill="white"/>',
    ]


def z_line_svg(mu, sigma, zmax, x_labels=None, mark=None):
    """Number line with x-values above and the matching z-values below.

    With x_labels ({z: text}) only those x labels are drawn, for a question.
    With mark (an x-value) that x gets a dot and its z-score in the z row.
    """
    axis_y = 90
    height = 150 if mark is None else 185
    zs = range(-zmax, zmax + 1)

    def x(z):
        return MARGIN + (z + zmax) / (2 * zmax) * (WIDTH - 2 * MARGIN)

    parts = header(height)
    parts.append(f'<text x="20" y="{axis_y - 25}" font-size="20" fill="{COLOR}">x</text>')
    parts.append(f'<text x="20" y="{axis_y + 45}" font-size="20" fill="{CENTER}">z</text>')
    parts.append(f'<line x1="{MARGIN - 20}" y1="{axis_y}" x2="{WIDTH - MARGIN + 20}" y2="{axis_y}" stroke="#333" stroke-width="2"/>')
    # Every integer x gets a small tick, and a label unless this is a question
    for v in range(mu - zmax * sigma, mu + zmax * sigma + 1):
        px = x((v - mu) / sigma)
        parts.append(f'<line x1="{px:.1f}" y1="{axis_y - 5}" x2="{px:.1f}" y2="{axis_y + 5}" stroke="#333" stroke-width="1.5"/>')
        if x_labels is None:
            parts.append(f'<text x="{px:.1f}" y="{axis_y - 25}" font-size="20" text-anchor="middle" fill="{COLOR}">{v}</text>')
    # Whole standard deviations get a tall tick and a z label
    for z in zs:
        parts.append(f'<line x1="{x(z):.1f}" y1="{axis_y - 12}" x2="{x(z):.1f}" y2="{axis_y + 12}" stroke="#333" stroke-width="3"/>')
        parts.append(f'<text x="{x(z):.1f}" y="{axis_y + 45}" font-size="22" text-anchor="middle" fill="{CENTER}">{z}</text>')
        if x_labels and z in x_labels:
            parts.append(f'<text x="{x(z):.1f}" y="{axis_y - 25}" font-size="22" text-anchor="middle" fill="{COLOR}">{x_labels[z]}</text>')
    if mark is not None:
        z = (mark - mu) / sigma
        parts.append(f'<circle cx="{x(z):.1f}" cy="{axis_y}" r="9" fill="{MARK}"/>')
        parts.append(f'<line x1="{x(z):.1f}" y1="{axis_y + 10}" x2="{x(z):.1f}" y2="{axis_y + 62}" stroke="{MARK}" stroke-width="2" stroke-dasharray="4 4"/>')
        parts.append(f'<text x="{x(z):.1f}" y="{axis_y + 85}" font-size="22" font-weight="bold" text-anchor="middle" fill="{MARK}">z = {z:g}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


with open("zvalues-number-line.svg", "w") as f:
    f.write(z_line_svg(12, 4, 2))

with open("zvalues-number-line-question.svg", "w") as f:
    f.write(z_line_svg(12, 4, 2, {-2: "?", -1: "?", 0: 12, 1: "?", 2: "?"}))

with open("zvalues-number-line-answer.svg", "w") as f:
    f.write(z_line_svg(12, 4, 2, {-2: 4, -1: 8, 0: 12, 1: 16, 2: 20}))

with open("zvalues-number-line-21.svg", "w") as f:
    f.write(z_line_svg(21, 5, 2))

with open("zvalues-number-line-21-question.svg", "w") as f:
    f.write(z_line_svg(21, 5, 2, {-2: "?", -1: "?", 0: 21, 1: "?", 2: "?"}))

with open("zvalues-number-line-21-answer.svg", "w") as f:
    f.write(z_line_svg(21, 5, 2, {-2: 11, -1: 16, 0: 21, 1: 26, 2: 31}))

# One number line per worked z-score, with the answer marked
for mu, sigma, xs in ((12, 4, (18, 17, 7, 13)), (21, 5, (28, 23, 17, 12))):
    for v in xs:
        with open(f"zvalues-z-{mu}-{v}.svg", "w") as f:
            f.write(z_line_svg(mu, sigma, 2, mark=v))
