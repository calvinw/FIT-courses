# FIT Courses

Course syllabuses (and other course material) organized by course, then semester:

```
CS211/
  Fall26/    CS211-301-Fall26.md -> .html, .pdf
  Spring26/
Ma153/
Ma321/
Ma322/
shared/      InstitutionalPoliciesAndResources.md
tools/       make-index.sh
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

## Adding a semester

Copy the most recent semester folder for that course and rename the files, e.g.

```
cp -r CS211/Spring26 CS211/Fall26
# rename the .md, update the title/dates inside, then: make
```

## History

Earlier semesters (Fall 24 through Summer 26) live in the previous repo,
<https://github.com/calvinw/FIT-syllabuses>, along with the older lecture material.
