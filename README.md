# FIT Courses

Course syllabuses (and other course material) organized by course, with the
semester in the filename:

```
CS211/
  CS211-301-Fall26.md -> .html, .pdf
  CS211-302-Fall26.md -> .html, .pdf
  lectures/    slide.qmd -> slide.html
Ma321/         Ma321-85B-Fall26.md -> .html, .pdf
Ma322/         Ma322-802-Fall26.md -> .html, .pdf
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

## Course list

`courses.txt` decides which syllabuses appear on `index.html`, in that order.
Each line is a syllabus name and an optional Google Site URL:

```
CS211-301-Fall26   https://sites.google.com/fitnyc.edu/cs211-801-fall26
CS211-302-Fall26
```

A syllabus with a URL gets a "Course Site" link; one without just shows
HTML/PDF/Markdown. Anything not listed stays in the repo but is left off the
page entirely. Add or remove a line and run `make index`.

## Adding a semester

Copy the most recent syllabus for that course and rename it, e.g.

```
cp CS211/CS211-301-Fall26.md CS211/CS211-301-Spring27.md
# update the title, meeting time, and room inside, add it to courses.txt, then: make
```

Lecture decks are `.qmd` files under a course's `lectures/` folder; they render
to revealjs HTML only (no PDF).

## History

Earlier semesters (Fall 24 through Summer 26) live in the previous repo,
<https://github.com/calvinw/FIT-syllabuses>, along with the older lecture material.
