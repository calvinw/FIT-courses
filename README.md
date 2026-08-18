# FIT Courses

Course syllabuses (and other course material) organized by course, with the
semester in the filename:

```
CS211/
  CS211-301-Fall26.md -> .html, .pdf
  CS211-301-Spring26.md
  lectures/    slide.qmd -> slide.html
Ma153/
Ma321/         Ma321-85B-Fall26.md, Ma321-OL1-Fall26.md, ...
Ma322/
shared/        InstitutionalPoliciesAndResources.md
tools/         make-index.sh
```

`.md` files are the sources; Quarto renders `.html` and `.pdf` next to each source,
and the `_files/` directories next to them hold the HTML assets. All of it is
committed so GitHub Pages can serve it.

## Building

```
make            # render every .md to HTML + PDF, then regenerate index.html
make index      # regenerate index.html only
make clean      # remove generated .html, .pdf, and *_files
```

## Course sites

`course-sites.txt` maps a syllabus name to its Google Site, one per line:

```
CS211-301-Fall26   https://sites.google.com/fitnyc.edu/cs211-801-fall26
```

Any syllabus listed there gets a "Course Site" link in `index.html`; the rest
just show HTML/PDF/Markdown. Add a line and run `make index`.

## Adding a semester

Copy the most recent syllabus for that course and rename it, e.g.

```
cp CS211/CS211-301-Spring26.md CS211/CS211-301-Fall26.md
# update the title, meeting time, and room inside, then: make
```

Lecture decks are `.qmd` files under a course's `lectures/` folder; they render
to revealjs HTML only (no PDF).

## History

Earlier semesters (Fall 24 through Summer 26) live in the previous repo,
<https://github.com/calvinw/FIT-syllabuses>, along with the older lecture material.
