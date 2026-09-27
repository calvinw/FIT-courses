---
format:
  html: default
  pdf:
    geometry:
      - margin=0.7in
    fontsize: 10pt
---

# Answers: The Pennsylvania Turnpike

The Pennsylvania Turnpike runs from Ohio in the west to New Jersey in the east. The table gives the distance (in miles) from each exit to the one before it. For example, the distance from Ohio Gateway to New Castle is 8 miles, and the distance from New Castle to Beaver Valley is 3.4 miles.

| Exit | Name | Distance from previous exit |
|:--|:--|--:|
| 1 | Ohio Gateway | -- |
| 1A | New Castle | 8.0 |
| 2 | Beaver Valley | 3.4 |
| 3 | Cranberry | 15.6 |
| 4 | Butler Valley | 10.7 |
| 5 | Allegheny Valley | 8.6 |
| 6 | Pittsburgh | 8.9 |
| 7 | Irwin | 10.8 |
| 8 | New Stanton | 8.1 |
| 9 | Donegal | 15.2 |
| 10 | Somerset | 19.2 |
| 11 | Bedford | 35.6 |
| 12 | Breezewood | 15.9 |
| 13 | Fort Littleton | 18.1 |
| 14 | Willow Hill | 9.1 |
| 15 | Blue Mountain | 12.7 |
| 16 | Carlisle | 25.0 |
| 17 | Gettysburg Pike | 9.8 |
| 18 | Harrisburg West Shore | 5.9 |
| 19 | Harrisburg East | 5.4 |
| 20 | Lebanon-Lancaster | 19.0 |
| 21 | Reading | 19.1 |
| 22 | Morgantown | 12.8 |
| 23 | Downingtown | 13.7 |
| 24 | Valley Forge | 14.3 |
| 25 | Norristown | 6.8 |
| 26 | Fort Washington | 5.4 |
| 27 | Willow Grove | 4.4 |
| 28 | Philadelphia | 8.4 |
| 29 | Delaware Valley | 6.4 |
| 30 | Delaware River Bridge | 1.3 |

There are $n = 30$ distances. In order:

1.3, 3.4, 4.4, 5.4, 5.4, 5.9, 6.4, 6.8, 8.0, 8.1, 8.4, 8.6, 8.9, 9.1, **9.8, 10.7**, 10.8, 12.7, 12.8, 13.7, 14.3, 15.2, 15.6, 15.9, 18.1, 19.0, 19.1, 19.2, 25.0, 35.6

$$
\bar{x} = \frac{357.6}{30} = 11.92 \text{ miles} \qquad \text{median} = \frac{9.8 + 10.7}{2} = 10.25 \text{ miles}
$$

**a) Only enough gas for 20 miles?**

**Yes, they are very likely to make it.** Only 2 of the 30 distances are more than 20 miles (Carlisle, 25.0, and Bedford, 35.6). So 28 out of 30 trips are 20 miles or less:

$$
\frac{28}{30} \approx 0.93 \ (93\%)
$$

**b) Only enough gas for 10 miles?**

**It is about a coin flip.** The median is 10.25 miles, so about half of the distances are more than 10 miles. Counting, 15 of the 30 distances are 10 miles or less:

$$
\frac{15}{30} = 0.5 \ (50\%)
$$

The median tells us this directly: half of the trips are shorter than 10.25 miles and half are longer.
