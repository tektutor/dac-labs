# Docs-as-Code lab targets. Run "make help" for a list.
.RECIPEPREFIX := >
SPHINXBUILD ?= sphinx-build
SPHINXOPTS  ?= -W --keep-going -q
SRC	    := docs
OUT	    := docs/_build

.PHONY: help clean html spelling linkcheck pdf check

help:
> @echo "make html		strict HTML build (warnings fail the build)"
> @echo "make spelling		spell check against docs/spelling_wordlist.txt"
> @echo "make linkcheck		check every external link"
> @echo "make pdf		build the PDF (needs LaTeX, Java and PlantUML)"
> @echo "make check		html + spelling (what CI runs on each push)"
> @echo "make clean		delete all generated output"

clean:
> rm -rf $(OUT)

# -E rebuilds every page, so link and status data never come from a cache.
html:
> $(SPHINXBUILD) -E -b html $(SPHINXOPTS) $(SRC) $(OUT)/html

spelling:
> $(SPHINXBUILD) -b spelling $(SPHINXOPTS) $(SRC) $(OUT)/spelling

linkcheck:
> $(SPHINXBUILD) -b linkcheck -q $(SRC) $(OUT)/linkcheck

pdf:
> $(SPHINXBUILD) -M latexpdf $(SRC) $(OUT) $(SPHINXOPTS) -t pdf

check: html spelling
