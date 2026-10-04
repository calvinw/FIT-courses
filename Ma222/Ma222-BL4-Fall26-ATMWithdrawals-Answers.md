---
format:
  html: default
  pdf:
    geometry:
      - margin=0.7in
    fontsize: 10pt
---

# Answers: ATM Withdrawals at Three Machines

A bank wants to monitor the ATM withdrawals its customers make at three locations. The bank samples 50 withdrawals from each machine. For each machine, the table shows how many of the 50 withdrawals were for each amount, with the dotplot below it. The data is also in [ATMWithdrawals.csv](data/ATMWithdrawals.csv), one column per machine, so you can open it in Google Sheets.

### Machine 1

| Amount | \$20 | \$30 | \$40 | \$50 | \$60 | \$70 | \$80 | \$90 | \$100 | \$110 | \$120 |
|:----------|----:|----:|----:|----:|----:|----:|----:|----:|-----:|-----:|-----:|
| Count | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 |

![](images/ATMWithdrawals-1.svg){width=65%}

```{=html}
<div style="height: 3em"></div>
```

```{=latex}
\vspace{2em}
```

### Machine 2

| Amount | \$20 | \$30 | \$40 | \$50 | \$60 | \$70 | \$80 | \$90 | \$100 | \$110 | \$120 |
|:----------|----:|----:|----:|----:|----:|----:|----:|----:|-----:|-----:|-----:|
| Count | 2 | 8 | 1 | 9 | 2 | 6 | 2 | 9 | 1 | 8 | 2 |

![](images/ATMWithdrawals-2.svg){width=65%}

```{=html}
<div style="height: 3em"></div>
```

```{=latex}
\vspace{2em}
```

### Machine 3

| Amount | \$20 | \$30 | \$40 | \$50 | \$60 | \$70 | \$80 | \$90 | \$100 | \$110 | \$120 |
|:----------|----:|----:|----:|----:|----:|----:|----:|----:|-----:|-----:|-----:|
| Count | 9 | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 0 | 0 | 9 |

![](images/ATMWithdrawals-3.svg){width=65%}

**a) Is each dotplot distribution symmetric? (the same on the left and the right)**

**Yes**, all three are symmetric about \$70. Fold each dotplot at \$70 and the two sides match:

- Machine 1: 25 at \$40 (\$30 below) and 25 at \$100 (\$30 above).
- Machine 2: 2 at \$20 and \$120, 8 at \$30 and \$110, 1 at \$40 and \$100, 9 at \$50 and \$90, 2 at \$60 and \$80, with 6 in the middle at \$70.
- Machine 3: 9 at \$20 (\$50 below) and 9 at \$120 (\$50 above), with 32 in the middle at \$70.

**b) Calculate the mean and the standard deviation of each machine's withdrawals.**

With the data in columns A, B and C (rows 2 to 51), use `=AVERAGE(A2:A51)` and `=STDEV(A2:A51)`, and the same for columns B and C.

| | Mean | Standard deviation |
|:--|--:|--:|
| Machine 1 | \$70 | \$30.30 |
| Machine 2 | \$70 | \$30.30 |
| Machine 3 | \$70 | \$30.30 |

For example, for Machine 1:

$$
\bar{x} = \frac{25(40) + 25(100)}{50} = \frac{3500}{50} = 70
$$

Every withdrawal is \$30 away from the mean, so

$$
s = \sqrt{\frac{\sum (x-\bar{x})^2}{n-1}} = \sqrt{\frac{50(30)^2}{49}} = \sqrt{\frac{45000}{49}} \approx 30.30
$$

Machines 2 and 3 also have $\sum (x-\bar{x})^2 = 45000$. For Machine 3, the 32 withdrawals at \$70 add nothing and the 18 at \$20 or \$120 each add $50^2$: $18(2500) = 45000$.

**c) Are the dotplot distributions of withdrawal amounts the same for all three machines?**

**No**, they look very different:

- Machine 1 has two peaks, at \$40 and \$100, with nothing in between.
- Machine 2 is spread across all the amounts from \$20 to \$120.
- Machine 3 has one big peak at \$70 with smaller stacks at \$20 and \$120.

**d) True or false? "There are many different dotplot distributions with the same mean and standard deviation." Explain using your answers above.**

**True.** The three machines have the same mean (\$70) and the same standard deviation (\$30.30), but their dotplots are very different. The mean and standard deviation alone don't tell you the shape of the distribution, so it is always worth looking at the data.
