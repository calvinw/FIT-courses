"""Draw the number lines for the Z-Values in class assignment.

Run from this folder: python3 make_zvalues_inclass.py
"""
WIDTH = 900
MARGIN = 60
COLOR = "#b5121b"
CENTER = "#1f5fa8"
MARK = "#2a8a3e"

MU = 33
SIGMA = 4
XS = (39, 31, 26, 36)


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


with open("ZValues-question.svg", "w") as f:
    f.write(z_line_svg(MU, SIGMA, 2, {-2: "?", -1: "?", 0: MU, 1: "?", 2: "?"}))

with open("ZValues-answer.svg", "w") as f:
    f.write(z_line_svg(MU, SIGMA, 2, {z: MU + z * SIGMA for z in range(-2, 3)}))

with open("ZValues-line.svg", "w") as f:
    f.write(z_line_svg(MU, SIGMA, 2))

# One number line per x, with its z-score marked, for the answers
for v in XS:
    with open(f"ZValues-{v}.svg", "w") as f:
        f.write(z_line_svg(MU, SIGMA, 2, mark=v))
