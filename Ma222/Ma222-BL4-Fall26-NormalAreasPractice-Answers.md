---
format:
  html: default
  pdf:
    geometry:
      - margin=0.7in
    fontsize: 10pt
---

# Answers: Standard Normal Areas Practice

Find each area under the standard normal curve. Use the standard normal table, or a spreadsheet with `NORMSDIST`. The same problems are in this spreadsheet: [NormalAreasPractice-Answers.xlsx](data/NormalAreasPractice-Answers.xlsx).

| Area | Spreadsheet formula |
|:--|:--|
| Left tail area | `=NORMSDIST(z)` |
| Right tail area | `=1.0-NORMSDIST(z)` |
| Area between $z_1$ and $z_2$ | `=NORMSDIST(z2)-NORMSDIST(z1)` |

## Left Tail Areas

| # | $z$ | Left Tail Area | Formula |
|:-:|--:|:-:|:--|
| 1 | -1.33 | 0.0918 | `=NORMSDIST(-1.33)` |
| 2 | 0.52 | 0.6985 | `=NORMSDIST(0.52)` |
| 3 | -0.33 | 0.3707 | `=NORMSDIST(-0.33)` |
| 4 | 1.86 | 0.9686 | `=NORMSDIST(1.86)` |
| 5 | -2.15 | 0.0158 | `=NORMSDIST(-2.15)` |
| 6 | 0.08 | 0.5319 | `=NORMSDIST(0.08)` |
| 7 | -0.91 | 0.1814 | `=NORMSDIST(-0.91)` |
| 8 | 2.34 | 0.9904 | `=NORMSDIST(2.34)` |
| 9 | -1.62 | 0.0526 | `=NORMSDIST(-1.62)` |
| 10 | 1.25 | 0.8944 | `=NORMSDIST(1.25)` |


## Right Tail Areas

| # | $z$ | Right Tail Area | Formula |
|:-:|--:|:-:|:--|
| 1 | 1.42 | 0.0778 | `=1.0-NORMSDIST(1.42)` |
| 2 | -0.64 | 0.7389 | `=1.0-NORMSDIST(-0.64)` |
| 3 | 2.05 | 0.0202 | `=1.0-NORMSDIST(2.05)` |
| 4 | -1.38 | 0.9162 | `=1.0-NORMSDIST(-1.38)` |
| 5 | 0.47 | 0.3192 | `=1.0-NORMSDIST(0.47)` |
| 6 | -2.21 | 0.9864 | `=1.0-NORMSDIST(-2.21)` |
| 7 | 1.73 | 0.0418 | `=1.0-NORMSDIST(1.73)` |
| 8 | -0.15 | 0.5596 | `=1.0-NORMSDIST(-0.15)` |
| 9 | 0.96 | 0.1685 | `=1.0-NORMSDIST(0.96)` |
| 10 | -1.09 | 0.8621 | `=1.0-NORMSDIST(-1.09)` |


## Areas Between

| # | $z_1$ | $z_2$ | Area Between | Formula |
|:-:|--:|--:|:-:|:--|
| 1 | -0.94 | 1.27 | 0.7243 | `=NORMSDIST(1.27)-NORMSDIST(-0.94)` |
| 2 | -1.96 | 1.96 | 0.9500 | `=NORMSDIST(1.96)-NORMSDIST(-1.96)` |
| 3 | 0.25 | 1.75 | 0.3612 | `=NORMSDIST(1.75)-NORMSDIST(0.25)` |
| 4 | -2.30 | -0.40 | 0.3339 | `=NORMSDIST(-0.40)-NORMSDIST(-2.30)` |
| 5 | -1.15 | 0.65 | 0.6171 | `=NORMSDIST(0.65)-NORMSDIST(-1.15)` |
| 6 | 0.60 | 2.45 | 0.2671 | `=NORMSDIST(2.45)-NORMSDIST(0.60)` |
| 7 | -0.72 | 0.38 | 0.4123 | `=NORMSDIST(0.38)-NORMSDIST(-0.72)` |
| 8 | -1.80 | -1.05 | 0.1109 | `=NORMSDIST(-1.05)-NORMSDIST(-1.80)` |
| 9 | 1.12 | 2.60 | 0.1267 | `=NORMSDIST(2.60)-NORMSDIST(1.12)` |
| 10 | -2.58 | 1.44 | 0.9201 | `=NORMSDIST(1.44)-NORMSDIST(-2.58)` |


Answers come from the spreadsheet. With the printed table you may get a last digit that differs by 1 (for example $0.7244$ for #1 of the areas between).
