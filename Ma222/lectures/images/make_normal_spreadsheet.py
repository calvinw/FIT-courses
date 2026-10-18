"""Draw the SVGs used in the Standard Normal Spreadsheet lecture.

Run from this folder: python3 make_normal_spreadsheet.py
"""
from make_normal import area_left, normal_svg, write

for z in (-1.02, 1.79):
    write(f"normal-left-{z:g}.svg", normal_svg(hi=z, ticks=(z,)))
    print(f"left of {z:g}: {area_left(z):.4f}")

for z in (-1.48, 0.31):
    write(f"normal-right-{z:g}.svg", normal_svg(lo=z, ticks=(z,)))
    print(f"right of {z:g}: {1 - area_left(z):.4f}")

for a, b in ((-0.54, 1.24),):
    write(f"normal-between-{a:g}-{b:g}.svg", normal_svg(lo=a, hi=b, ticks=(a, b)))
    print(f"between {a:g} and {b:g}: {area_left(b) - area_left(a):.4f}")
