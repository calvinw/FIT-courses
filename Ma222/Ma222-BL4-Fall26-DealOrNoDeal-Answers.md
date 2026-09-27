---
format:
  html: default
  pdf:
    geometry:
      - margin=0.7in
    fontsize: 10pt
---

# Answers: Mean vs Median: Deal or No Deal

On the show *Deal or No Deal*, contestants choose from 26 suitcases. These are the amounts inside them (\$0.01 is one cent):

| | | | | | | | | |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| \$0.01 | \$1 | \$5 | \$10 | \$25 | \$50 | \$75 | \$100 | \$200 |
| \$300 | \$400 | \$500 | \$750 | \$1,000 | \$5,000 | \$10,000 | \$25,000 | \$50,000 |
| \$75,000 | \$100,000 | \$200,000 | \$300,000 | \$400,000 | \$500,000 | \$750,000 | \$1,000,000 | |

**a) What is the median amount?**

The amounts are already in order. There are $n = 26$ amounts, an even number, so the median is the average of the 13th and 14th values:

$$
\text{median} = \frac{750 + 1000}{2} = \$875
$$

**b) What is the mean amount?**

$$
\bar{x} = \frac{\sum x}{n} = \frac{3{,}418{,}416.01}{26} \approx \$131{,}477.54
$$

**c) Are the median and the mean close to each other? Why or why not?**

No. The mean (\$131,477.54) is about 150 times the median (\$875). A few very large amounts (\$500,000, \$750,000, \$1,000,000) pull the mean up. The median is not affected by how large those values are.

**d) What proportion of the prize amounts are bigger than the mean?**

Only 6 amounts are bigger than \$131,477.54 (\$200,000 through \$1,000,000):

$$
\frac{6}{26} \approx 0.23 \ (23\%)
$$

**e) What proportion of the prize amounts are bigger than the median?**

13 amounts are bigger than \$875 (\$1,000 through \$1,000,000):

$$
\frac{13}{26} = 0.5 \ (50\%)
$$

The median always splits the data in half. The mean does not.
