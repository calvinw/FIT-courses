"""Draw the SVGs used in the Normal Areas and Normal Area Applications lectures.

Run from this folder: python3 make_normal_areas.py
"""
from make_normal import area_left, normal_svg, write
from make_normal_table import table_svg


def table(z, rows):
    """Write the z-table excerpt for z with its row, column and cell highlighted."""
    row = f"{z:.2f}"[:-1]
    col = round(abs(z) * 100) % 10
    write(f"ztable-{z:g}-answer.svg", table_svg(rows, row, col, show_answer=True))
    print(f"  table z = {z:g}: row {row}, column .0{col}, area {area_left(z):.4f}")


# Left tails: mu, sigma, x, z rounded to two places, rows shown in the table
for mu, sigma, x, z, rows in (
    (3.3, 2.4, 1.23, -0.86, ("-0.9", "-0.8", "-0.7")),
    (1.2, 0.5, 1.72, 1.04, ("0.9", "1.0", "1.1")),
    (48, 10, 30, -1.8, ("-1.9", "-1.8", "-1.7")),
):
    write(f"normal-x-left-{x:g}.svg", normal_svg(hi=x, ticks=(x,), mu=mu, sigma=sigma))
    write(f"normal-left-{z:g}.svg", normal_svg(hi=z, ticks=(z,), named=True))
    print(f"left of x = {x:g}: z = {(x - mu) / sigma:.4f}")
    table(z, rows)

# Right tails
for mu, sigma, x, z, rows in (
    (42, 12, 53, 0.92, ("0.8", "0.9", "1.0")),
    (2.8, 1.5, 2.3, -0.33, ("-0.4", "-0.3", "-0.2")),
    (230, 25, 265, 1.4, ("1.3", "1.4", "1.5")),
    (120, 15, 140, 1.33, ("1.2", "1.3", "1.4")),
    (60, 5, 59, -0.2, ("-0.3", "-0.2", "-0.1")),
):
    write(f"normal-x-right-{x:g}.svg", normal_svg(lo=x, ticks=(x,), mu=mu, sigma=sigma))
    write(f"normal-right-{z:g}.svg", normal_svg(lo=z, ticks=(z,), named=True))
    print(f"right of x = {x:g}: z = {(x - mu) / sigma:.4f}")
    table(z, rows)

# Areas between
for mu, sigma, (x1, x2), (z1, z2), (rows1, rows2) in (
    (23, 8, (10, 27), (-1.63, 0.5), (("-1.7", "-1.6", "-1.5"), ("0.4", "0.5", "0.6"))),
    (1.3, 0.8, (1.6, 2.8), (0.38, 1.88), (("0.2", "0.3", "0.4"), ("1.7", "1.8", "1.9"))),
):
    write(f"normal-x-between-{x1:g}-{x2:g}.svg", normal_svg(lo=x1, hi=x2, ticks=(x1, x2), mu=mu, sigma=sigma))
    write(f"normal-between-{z1:g}-{z2:g}.svg", normal_svg(lo=z1, hi=z2, ticks=(z1, z2), named=True))
    print(f"between x = {x1:g} and {x2:g}: z1 = {(x1 - mu) / sigma:.4f}, z2 = {(x2 - mu) / sigma:.4f}")
    table(z1, rows1)
    table(z2, rows2)

# What an area means: x-curves only
write("normal-x-left-234.svg", normal_svg(hi=234, ticks=(234,), mu=230, sigma=25))
write("normal-x-right-250.svg", normal_svg(lo=250, ticks=(250,), mu=230, sigma=25))
print(f"left of x = 234: area {area_left((234 - 230) / 25):.4f}")
print(f"right of x = 250: area {1 - area_left((250 - 230) / 25):.4f}")
write("normal-x-left-203.svg", normal_svg(hi=203, ticks=(203,), mu=230, sigma=25))
write("normal-x-right-263.svg", normal_svg(lo=263, ticks=(263,), mu=230, sigma=25))
write("normal-x-between-215-245.svg", normal_svg(lo=215, hi=245, ticks=(215, 245), mu=230, sigma=25))
