"""Draw the SVGs used in the Backwards Problems lecture.

Run from this folder: python3 make_backwards.py
"""
from make_normal import area_left, normal_svg, write
from make_normal_table import table_svg


def table(name, z, rows):
    """Write the z-table excerpt plain, then with the closest area highlighted."""
    row = f"{z:.2f}"[:-1]
    col = round(abs(z) * 100) % 10
    write(f"ztable-back-{name}.svg", table_svg(rows))
    write(f"ztable-back-{name}-answer.svg", table_svg(rows, row, col, show_answer=True))
    print(f"  table z = {z:g}: row {row}, column .0{col}, area {area_left(z):.4f}")


# Find z: name, side, z read from the table, rows shown in the table
for name, side, z, rows in (
    ("left-25", "left", -0.67, ("-0.7", "-0.6", "-0.5")),
    ("right-18", "right", 0.92, ("0.8", "0.9", "1.0")),
):
    shade = {"hi": z} if side == "left" else {"lo": z}
    write(f"normal-back-{name}.svg", normal_svg(**shade, ticks=(z,), labels=("z = ?",)))
    write(f"normal-back-{name}-answer.svg", normal_svg(**shade, ticks=(z,), named=True))
    table(name, z, rows)

# Find x: name, side, mu, sigma, z read from the table, rows shown in the table
for name, side, mu, sigma, z, rows in (
    ("x-left-25", "left", 18, 3, -0.67, ("-0.7", "-0.6", "-0.5")),
    ("x-right-15", "right", 23, 4, 1.04, ("0.9", "1.0", "1.1")),
    ("x-left-10", "left", 257, 45, -1.28, ("-1.3", "-1.2", "-1.1")),
    ("x-left-95", "left", 340, 80, 1.64, ("1.5", "1.6", "1.7")),
):
    x = round(mu + z * sigma, 2)
    zshade = {"hi": z} if side == "left" else {"lo": z}
    xshade = {"hi": x} if side == "left" else {"lo": x}
    write(f"normal-back-{name}.svg", normal_svg(**xshade, ticks=(x,), mu=mu, sigma=sigma, labels=("x = ?",)))
    write(f"normal-back-{name}-z.svg", normal_svg(**zshade, ticks=(z,), labels=("z = ?",)))
    write(f"normal-back-{name}-answer.svg", normal_svg(**xshade, ticks=(x,), mu=mu, sigma=sigma))
    print(f"{name}: z = {z:g}, x = {x:g}")
    table(name, z, rows)
