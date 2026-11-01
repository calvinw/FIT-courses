"""Draw the SVGs used in the Backwards Problems and Spreadsheets lecture.

The pictures with "x = ?" or "z = ?" come from make_backwards.py; these are
the answers, with the exact z from NORMSINV instead of the table's.

Run from this folder: python3 make_backwards_spreadsheet.py
"""
from statistics import NormalDist

from make_normal import normal_svg, write

# Find z: name, side, tail area
for name, side, area in (
    ("left-25", "left", 0.25),
    ("right-18", "right", 0.18),
):
    z = round(NormalDist().inv_cdf(area if side == "left" else 1 - area), 4)
    shade = {"hi": z} if side == "left" else {"lo": z}
    write(f"normal-backss-{name}-answer.svg", normal_svg(**shade, ticks=(z,), named=True))
    print(f"{name}: z = {z:g}")

# Find x: name, side, mu, sigma, tail area
for name, side, mu, sigma, area in (
    ("x-left-25", "left", 18, 3, 0.25),
    ("x-right-15", "right", 23, 4, 0.15),
    ("x-left-10", "left", 257, 45, 0.10),
):
    z = round(NormalDist().inv_cdf(area if side == "left" else 1 - area), 4)
    x = round(mu + z * sigma, 2)
    shade = {"hi": x} if side == "left" else {"lo": x}
    write(f"normal-backss-{name}-answer.svg", normal_svg(**shade, ticks=(x,), mu=mu, sigma=sigma))
    print(f"{name}: z = {z:g}, x = {x:g}")
