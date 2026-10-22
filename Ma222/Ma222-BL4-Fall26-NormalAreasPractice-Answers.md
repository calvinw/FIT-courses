---
format:
  html: default
  pdf:
    geometry:
      - margin=0.6in
    fontsize: 10pt
---

# Answers: Standard Normal Areas Practice

Each answer comes from the spreadsheet formula shown under it. The same answers are in [NormalAreasPractice-Answers.xlsx](data/NormalAreasPractice-Answers.xlsx). With the printed table you may get a last digit that is off by 1.

| Area | Spreadsheet formula |
|:--|:--|
| Left tail area | `=NORMSDIST(z)` |
| Right tail area | `=1.0-NORMSDIST(z)` |
| Area between $z_1$ and $z_2$ | `=NORMSDIST(z2)-NORMSDIST(z1)` |

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

Area $= 0.0418$ \
`=1.0-NORMSDIST(1.73)`

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

Area $= 0.2671$ \
`=NORMSDIST(2.45)-NORMSDIST(0.6)`

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

Area $= 0.9162$ \
`=1.0-NORMSDIST(-1.38)`

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

Area $= 0.5596$ \
`=1.0-NORMSDIST(-0.15)`

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

Area $= 0.0158$ \
`=NORMSDIST(-2.15)`

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

Area $= 0.0202$ \
`=1.0-NORMSDIST(2.05)`

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

Area $= 0.7389$ \
`=1.0-NORMSDIST(-0.64)`

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

Area $= 0.5319$ \
`=NORMSDIST(0.08)`

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

Area $= 0.3612$ \
`=NORMSDIST(1.75)-NORMSDIST(0.25)`

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

Area $= 0.0526$ \
`=NORMSDIST(-1.62)`

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

Area $= 0.0778$ \
`=1.0-NORMSDIST(1.42)`

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

Area $= 0.9500$ \
`=NORMSDIST(1.96)-NORMSDIST(-1.96)`

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

Area $= 0.9201$ \
`=NORMSDIST(1.44)-NORMSDIST(-2.58)`

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

Area $= 0.1814$ \
`=NORMSDIST(-0.91)`

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

Area $= 0.1685$ \
`=1.0-NORMSDIST(0.96)`

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
