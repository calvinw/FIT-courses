"""Draw the SVGs used in the Standard Normal Table lecture.

Run from this folder: python3 make_normal_table.py
"""
from make_normal import COLOR, area_left, normal_svg, write

WIDTH = 900
ROW_H = 42
FIRST_W = 90
CELL_W = (WIDTH - FIRST_W) / 10
LINE = "#f3d9a4"
HIT = "#f2b84b"


def table_svg(rows, row=None, col=None, show_answer=False):
    """Excerpt of the z-table for the given row labels like "-1.2" or "0.0".

    With row and col set, that row and column are highlighted;
    show_answer also darkens the cell where they meet.
    """
    height = ROW_H * (len(rows) + 1)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" '
        f'width="{WIDTH}" height="{height}" font-family="sans-serif">',
        f'<rect width="{WIDTH}" height="{height}" fill="white"/>',
    ]

    def cx(c):
        return FIRST_W + c * CELL_W

    # Highlight the row and column first so the grid and text sit on top.
    # The row runs from its label over to the cell, and the column runs from
    # its header down to the cell, so both stop at the area being found.
    if row is not None:
        r = rows.index(row) + 1
        parts.append(f'<rect x="0" y="{r * ROW_H}" width="{cx(col) + CELL_W:.1f}" height="{ROW_H}" fill="{LINE}"/>')
        parts.append(f'<rect x="{cx(col):.1f}" y="0" width="{CELL_W:.1f}" height="{(r + 1) * ROW_H}" fill="{LINE}"/>')
        if show_answer:
            parts.append(f'<rect x="{cx(col):.1f}" y="{r * ROW_H}" width="{CELL_W:.1f}" height="{ROW_H}" fill="{HIT}" stroke="{COLOR}" stroke-width="3"/>')

    parts.append(f'<rect x="0" y="0" width="{WIDTH}" height="{height}" fill="none" stroke="#333" stroke-width="2"/>')
    parts.append(f'<line x1="0" y1="{ROW_H}" x2="{WIDTH}" y2="{ROW_H}" stroke="#333" stroke-width="2"/>')
    parts.append(f'<line x1="{FIRST_W}" y1="0" x2="{FIRST_W}" y2="{height}" stroke="#333" stroke-width="2"/>')
    parts.append(f'<text x="{FIRST_W / 2}" y="{ROW_H * 0.68}" font-size="20" font-weight="bold" text-anchor="middle" fill="{COLOR}">z</text>')
    for c in range(10):
        parts.append(f'<text x="{cx(c) + CELL_W / 2:.1f}" y="{ROW_H * 0.68}" font-size="20" font-weight="bold" text-anchor="middle" fill="{COLOR}">.0{c}</text>')
    for i, label in enumerate(rows, start=1):
        y = i * ROW_H + ROW_H * 0.68
        parts.append(f'<text x="{FIRST_W / 2}" y="{y}" font-size="20" font-weight="bold" text-anchor="middle" fill="{COLOR}">{label}</text>')
        base = float(label)
        for c in range(10):
            # Negative rows (including -0.0) go further left with each column
            z = base - c / 100 if label.startswith("-") else base + c / 100
            value = f"{area_left(z):.4f}".lstrip("0")
            parts.append(f'<text x="{cx(c) + CELL_W / 2:.1f}" y="{y}" font-size="20" text-anchor="middle" fill="#333">{value}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


# z, its table row, its column, and the rows shown around it, from the book
EXAMPLES = (
    (-1.25, "-1.2", 5, ("-1.5", "-1.4", "-1.3", "-1.2", "-1.1", "-1.0", "-0.9")),
    (1.32, "1.3", 2, ("1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6")),
    (0.07, "0.0", 7, ("-0.2", "-0.1", "-0.0", "0.0", "0.1", "0.2", "0.3")),
    # Two more for practice
    (0.84, "0.8", 4, ("0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1")),
    (-2.17, "-2.1", 7, ("-2.4", "-2.3", "-2.2", "-2.1", "-2.0", "-1.9", "-1.8")),
)

if __name__ == "__main__":
    for z, row, col, rows in EXAMPLES:
        write(f"normal-left-{z:g}.svg", normal_svg(hi=z, ticks=(z,)))
        write(f"ztable-{z:g}.svg", table_svg(rows))
        write(f"ztable-{z:g}-find.svg", table_svg(rows, row, col))
        write(f"ztable-{z:g}-answer.svg", table_svg(rows, row, col, show_answer=True))
        print(f"left of {z:g}: {area_left(z):.4f}")
