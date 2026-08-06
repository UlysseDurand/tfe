# Internship at Kitware

I did this internship from April to August 2026 under the supervision of Julien Finet in the
Software Development team at Kiware Europe in Villeurbanne, with ENS and ECL as schools.

## Problematic

How is collaborative software development organized in the production of a
Python framework: trame.

## Deliverables

### Premilinary report (15/4)

### ENS Report (26/6)

### ENS Defense (10/7)

### ECL Report (1/9)

### ECL Defense (?? 14/9 <-> 19/9)

## Structure

- `assets/`: shared images, logos and graph sources (`.mmd`).
- `scripts/`: shared build machinery (`render_templates.py`, `build_timeline.py`,
  and the `data_sources/` package: GitHub, calendar and metadata accessors).
- `config/`: shared metadata (`metadata.yml`, `contributions.yml`) and
  `references.bib`.
- `reportENS/`: ENS report content (`src/*.tex.j2`) and its LaTeX class.
- `slidesENS/`: ENS defense slides content (`src/*.tex.j2`) and its LaTeX class.
- `Makefile.common`: shared make rules, included by each deliverable's Makefile.

## Building

Each deliverable builds itself with its own thin `Makefile`:

```sh
make -C reportENS all   # full build: clean + assets + pdf
make -C reportENS fast  # incremental, no asset regeneration
make -C slidesENS all
```

`build_assets` (graphs + timeline) is shared: mermaid `.mmd` files in `assets/graphs/`
are rendered to `assets/images/` and the timeline is regenerated into
`assets/images/timeline.png`.

