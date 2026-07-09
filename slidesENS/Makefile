TEXFILE = main
OUTDIR = build
SRCFOLDER = src
ASSETSFOLDER = ../assets
CLSFILE = $(SRCFOLDER)/slidesECLENSKitware.cls
SRCFILES = $(shell find $(SRCFOLDER) -type f)
VENV_PYTHON = ../.venv

# FAST= -usepretex -bibtex-
FAST=

.PHONY: clean build_assets all fast generate-graphs

fast: $(OUTDIR)/$(TEXFILE).pdf

all: clean build_assets $(OUTDIR)/$(TEXFILE).pdf

$(OUTDIR)/$(TEXFILE).pdf: $(OUTDIR)/$(TEXFILE).tex
	latexmk -f -lualatex -silent $(FAST) -outdir=$(OUTDIR) $(OUTDIR)/$(TEXFILE).tex

generate-graphs: $(patsubst $(ASSETSFOLDER)/graphs/%.md, $(ASSETSFOLDER)/images/%.png, $(wildcard $(ASSETSFOLDER)/graphs/*.md))

$(ASSETSFOLDER)/images/%.png: $(ASSETSFOLDER)/graphs/%.md
	@mkdir -p $(ASSETSFOLDER)/images
	mmdc -i $< -o $@ --scale 3

build_assets: generate-graphs
	$(VENV_PYTHON)/bin/python build_scripts/build_assets.py

$(OUTDIR)/$(TEXFILE).tex: $(SRCFILES)
	@mkdir -p $(OUTDIR)
	cp $(CLSFILE) $(OUTDIR)
	cp -r $(ASSETSFOLDER) $(OUTDIR)
	$(VENV_PYTHON)/bin/python build_scripts/build_tex.py $(SRCFOLDER) $(OUTDIR)

clean:
	latexmk -C -outdir=$(OUTDIR)
	@rm -rf $(OUTDIR)/*