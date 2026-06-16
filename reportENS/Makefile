TEXFILE = main
OUTDIR = build
CLSFILE = rapportECLENSKitware.cls
SRCFOLDER = src
SRCFILES = $(wildcard $(SRCFOLDER)/*)
BUILT_SRCFILES = $(patsubst $(SRCFOLDER)/%, $(OUTDIR)/%, $(DEPFILES))
VENV_PYTHON = ../.venv

# FAST= -usepretex -bibtex-
FAST=

.PHONY: clean

$(OUTDIR)/$(TEXFILE).pdf: $(OUTDIR)/$(TEXFILE).tex $(BUILT_DEPFILES)
	latexmk -f -lualatex -silent $(FAST) -outdir=$(OUTDIR) $(OUTDIR)/$(TEXFILE).tex

$(OUTDIR)/$(TEXFILE).tex: $(TEMPLATEFILE) $(DEPFILES)
	@mkdir -p $(OUTDIR)
	$(VENV_PYTHON)/bin/python latexbuilder.py $(SRCFOLDER) $(OUTDIR)

clean:
	latexmk -C -outdir=$(OUTDIR)
	@rm -rf $(OUTDIR)/*