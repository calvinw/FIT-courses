# Sources are the .md files under <Course>/<Semester>/ and shared/.
MD_FILES  := $(shell find . -name '*.md' -not -name 'README.md')
# Lecture slide decks render to HTML only, in whatever format their YAML sets
# (revealjs for slides) -- so no --to flag here
QMD_FILES := $(shell find . -name '*.qmd')

HTML_TARGETS := $(MD_FILES:.md=.html) $(QMD_FILES:.qmd=.html)
PDF_TARGETS  := $(MD_FILES:.md=.pdf)

# Keeps \% robust so headings with a percent sign survive the .aux round trip
PDF_HEADER := $(CURDIR)/shared/latex-percent-fix.tex

# Default: build HTML + PDF for everything, then refresh the index page
all: $(HTML_TARGETS) $(PDF_TARGETS) index

%.html: %.md
	quarto render $< --to html

%.html: %.qmd
	quarto render $<

%.pdf: %.md $(PDF_HEADER)
	quarto render $< --to pdf --include-in-header=$(PDF_HEADER)

# Regenerate index.html from whatever is currently on disk
index:
	./tools/make-index.sh > index.html

clean:
	rm -f $(HTML_TARGETS) $(PDF_TARGETS)
	find . -type d -name '*_files' -exec rm -rf {} +

.PHONY: all index clean
