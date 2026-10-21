"""Draw the graphs for the Normal Areas Practice handout.

Run from this folder: python3 make_normal_areas_practice.py

Uses the same curve drawing as the lecture slides (lectures/images/make_normal.py).
The problems are mixed up with a fixed seed so the order never changes.
"""
import os
import random
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lectures", "images"))
from make_normal import area_left, normal_svg, write

LEFT = [-1.33, 0.52, -0.33, 1.86, -2.15, 0.08, -0.91, 2.34, -1.62, 1.25]
RIGHT = [1.42, -0.64, 2.05, -1.38, 0.47, -2.21, 1.73, -0.15, 0.96, -1.09]
BETWEEN = [(-0.94, 1.27), (-1.96, 1.96), (0.25, 1.75), (-2.30, -0.40), (-1.15, 0.65),
           (0.60, 2.45), (-0.72, 0.38), (-1.80, -1.05), (1.12, 2.60), (-2.58, 1.44)]

# Each problem is (kind, z1, z2); z2 is None for the tails
PROBLEMS = ([("left", z, None) for z in LEFT]
            + [("right", z, None) for z in RIGHT]
            + [("between", a, b) for a, b in BETWEEN])
random.Random(222).shuffle(PROBLEMS)


def area(kind, z1, z2):
    if kind == "left":
        return area_left(z1)
    if kind == "right":
        return 1 - area_left(z1)
    return area_left(z2) - area_left(z1)


def graph(kind, z1, z2):
    if kind == "left":
        return normal_svg(hi=z1, ticks=(z1,))
    if kind == "right":
        return normal_svg(lo=z1, ticks=(z1,))
    return normal_svg(lo=z1, hi=z2, ticks=(z1, z2))


def name(i):
    return f"NormalAreasPractice-{i:02d}.svg"


if __name__ == "__main__":
    for i, (kind, z1, z2) in enumerate(PROBLEMS, 1):
        write(name(i), graph(kind, z1, z2))
        # PNG copies for the Google Sheet, whose IMAGE() can't show SVGs
        subprocess.run(["rsvg-convert", "-w", "480", "-o", name(i).replace(".svg", ".png"), name(i)], check=True)
        print(f"{i:2d}. {kind:7s} {z1:g} {'' if z2 is None else f'{z2:g}'}: {area(kind, z1, z2):.4f}")
