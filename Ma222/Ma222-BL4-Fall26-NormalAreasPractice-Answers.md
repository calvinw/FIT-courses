---
format:
  html: default
  pdf:
    geometry:
      - margin=0.6in
    fontsize: 10pt
---

# Answers: Standard Normal Areas Practice

Each answer shows the table lookups. A spreadsheet gives the same answers, sometimes with the last digit off by 1: [NormalAreasPractice-Answers.xlsx](data/NormalAreasPractice-Answers.xlsx). The students' Google Sheet is [here](https://docs.google.com/spreadsheets/d/11qsF05W6QAo2uwGFEVLUvmm2FdG3jo2u2emO1yQJRFM/edit?gid=0#gid=0).

## Example: Using the Table

**Find the left tail area for $z = -1.25$.**

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; align-items:center">
<div>
```

```{=latex}
\noindent\begin{minipage}[c]{0.47\textwidth}
```

![](lectures/images/normal-left--1.25.svg){width=100%}

```{=html}
</div>
<div>
```

```{=latex}
\end{minipage}\hfill\begin{minipage}[c]{0.47\textwidth}
```

![](lectures/images/ztable--1.25-answer.svg){width=100%}

```{=latex}
\end{minipage}
```

```{=html}
</div>
</div>
```

Split $z = -1.25$ into the **row** $-1.2$ (the ones digit and first decimal place) and the **column** $.05$ (the second decimal place). Where they meet:

$$
\text{left tail area} = 0.1056 \approx 11\%
$$

Our table has only **left tail areas**. For the other areas, look up left tail areas first:

- **Right tail area** $= 1.0 - \text{left tail area}$
- **Area between** $z_1$ and $z_2$ $=$ (left tail area for $z_2$) $-$ (left tail area for $z_1$)

## Problems

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; margin-bottom:1.5em">
```

```{=latex}
\noindent\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**1.** Find the right tail area for $z = 1.73$

![](images/NormalAreasPractice-01.svg){width=100%}

Row $1.7$, column $.03$: left tail area $= 0.9582$ \
Right tail area $= 1.0 - 0.9582 = 0.0418$

```{=html}
</div>
```

```{=latex}
\end{minipage}\hfill\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**2.** Find the area between $z = 0.6$ and $z = 2.45$

![](images/NormalAreasPractice-02.svg){width=100%}

$z = 2.45$: row $2.4$, column $.05$ gives $0.9929$ \
$z = 0.6$: row $0.6$, column $.00$ gives $0.7257$ \
Area between $= 0.9929 - 0.7257 = 0.2672$

```{=html}
</div>
```

```{=latex}
\end{minipage}
\vspace{1.2em}
```

```{=html}
</div>
```

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; margin-bottom:1.5em">
```

```{=latex}
\noindent\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**3.** Find the area to the right of $z = -1.38$

![](images/NormalAreasPractice-03.svg){width=100%}

Row $-1.3$, column $.08$: left tail area $= 0.0838$ \
Right tail area $= 1.0 - 0.0838 = 0.9162$

```{=html}
</div>
```

```{=latex}
\end{minipage}\hfill\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**4.** Find the area where $z > -0.15$

![](images/NormalAreasPractice-04.svg){width=100%}

Row $-0.1$, column $.05$: left tail area $= 0.4404$ \
Right tail area $= 1.0 - 0.4404 = 0.5596$

```{=html}
</div>
```

```{=latex}
\end{minipage}
\vspace{1.2em}
```

```{=html}
</div>
```

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; margin-bottom:1.5em">
```

```{=latex}
\noindent\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**5.** Find the left tail area for $z = -2.15$

![](images/NormalAreasPractice-05.svg){width=100%}

Row $-2.1$, column $.05$: left tail area $= 0.0158$

```{=html}
</div>
```

```{=latex}
\end{minipage}\hfill\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**6.** Find the area for $z$ greater than $2.05$

![](images/NormalAreasPractice-06.svg){width=100%}

Row $2.0$, column $.05$: left tail area $= 0.9798$ \
Right tail area $= 1.0 - 0.9798 = 0.0202$

```{=html}
</div>
```

```{=latex}
\end{minipage}
\vspace{1.2em}
```

```{=html}
</div>
```

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; margin-bottom:1.5em">
```

```{=latex}
\noindent\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**7.** Find the right tail area for $z = -0.64$

![](images/NormalAreasPractice-07.svg){width=100%}

Row $-0.6$, column $.04$: left tail area $= 0.2611$ \
Right tail area $= 1.0 - 0.2611 = 0.7389$

```{=html}
</div>
```

```{=latex}
\end{minipage}\hfill\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**8.** Find the area to the left of $z = 0.08$

![](images/NormalAreasPractice-08.svg){width=100%}

Row $0.0$, column $.08$: left tail area $= 0.5319$

```{=html}
</div>
```

```{=latex}
\end{minipage}
\vspace{1.2em}
```

```{=html}
</div>
```

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; margin-bottom:1.5em">
```

```{=latex}
\noindent\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**9.** Find the area where $0.25 < z < 1.75$

![](images/NormalAreasPractice-09.svg){width=100%}

$z = 1.75$: row $1.7$, column $.05$ gives $0.9599$ \
$z = 0.25$: row $0.2$, column $.05$ gives $0.5987$ \
Area between $= 0.9599 - 0.5987 = 0.3612$

```{=html}
</div>
```

```{=latex}
\end{minipage}\hfill\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**10.** Find the area where $z < -1.62$

![](images/NormalAreasPractice-10.svg){width=100%}

Row $-1.6$, column $.02$: left tail area $= 0.0526$

```{=html}
</div>
```

```{=latex}
\end{minipage}
\vspace{1.2em}
```

```{=html}
</div>
```

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; margin-bottom:1.5em">
```

```{=latex}
\noindent\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**11.** Find the area to the right of $z = 1.42$

![](images/NormalAreasPractice-11.svg){width=100%}

Row $1.4$, column $.02$: left tail area $= 0.9222$ \
Right tail area $= 1.0 - 0.9222 = 0.0778$

```{=html}
</div>
```

```{=latex}
\end{minipage}\hfill\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**12.** Find the area for $z$ between $-1.96$ and $1.96$

![](images/NormalAreasPractice-12.svg){width=100%}

$z = 1.96$: row $1.9$, column $.06$ gives $0.9750$ \
$z = -1.96$: row $-1.9$, column $.06$ gives $0.0250$ \
Area between $= 0.9750 - 0.0250 = 0.9500$

```{=html}
</div>
```

```{=latex}
\end{minipage}
\vspace{1.2em}
```

```{=html}
</div>
```

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; margin-bottom:1.5em">
```

```{=latex}
\noindent\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**13.** Find the area for $z$ greater than $-2.58$ and less than $1.44$

![](images/NormalAreasPractice-13.svg){width=100%}

$z = 1.44$: row $1.4$, column $.04$ gives $0.9251$ \
$z = -2.58$: row $-2.5$, column $.08$ gives $0.0049$ \
Area between $= 0.9251 - 0.0049 = 0.9202$

```{=html}
</div>
```

```{=latex}
\end{minipage}\hfill\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**14.** Find the area for $z$ less than $-0.91$

![](images/NormalAreasPractice-14.svg){width=100%}

Row $-0.9$, column $.01$: left tail area $= 0.1814$

```{=html}
</div>
```

```{=latex}
\end{minipage}
\vspace{1.2em}
```

```{=html}
</div>
```

```{=html}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:0 2em; margin-bottom:1.5em">
```

```{=latex}
\noindent\begin{minipage}[t]{0.47\textwidth}
```

```{=html}
<div>
```

**15.** Find the area where $z > 0.96$

![](images/NormalAreasPractice-15.svg){width=100%}

Row $0.9$, column $.06$: left tail area $= 0.8315$ \
Right tail area $= 1.0 - 0.8315 = 0.1685$

```{=html}
</div>
```

```{=latex}
\end{minipage}
\vspace{1.2em}
```

```{=html}
</div>
```
