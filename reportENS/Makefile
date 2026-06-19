TEXFILE = main
OUTDIR = build
CLSFILE = rapportECLENSKitware.cls
SRCFOLDER = src
SRCFILES = $(shell find $(SRCFOLDER) -type f)
VENV_PYTHON = ../.venv

# FAST= -usepretex -bibtex-
FAST=

.PHONY: clean build_assets all fast generate-graphs

fast: $(OUTDIR)/$(TEXFILE).pdf

all: clean build_assets $(OUTDIR)/$(TEXFILE).pdf

$(OUTDIR)/$(TEXFILE).pdf: $(OUTDIR)/$(TEXFILE).tex
	latexmk -f -lualatex -silent $(FAST) -outdir=$(OUTDIR) $(OUTDIR)/$(TEXFILE).tex

generate-graphs: $(patsubst assets/graphs/%.md, assets/images/%.png, $(wildcard assets/graphs/*.md))

assets/images/%.png: assets/graphs/%.md
	@mkdir -p assets/images
	mmdc -i $< -o $@ --scale 3

build_assets: generate-graphs
	$(VENV_PYTHON)/bin/python build_scripts/build_assets.py

$(OUTDIR)/$(TEXFILE).tex: $(SRCFILES)
	@mkdir -p $(OUTDIR)
	$(VENV_PYTHON)/bin/python build_scripts/build_tex.py $(SRCFOLDER) $(OUTDIR)

clean:
	latexmk -C -outdir=$(OUTDIR)
	@rm -rf $(OUTDIR)/*