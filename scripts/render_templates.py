#!/usr/bin/env python3

import sys
from pathlib import Path

import data_sources
from jinja2 import Environment, FileSystemLoader


def main():
    src_dir, build_dir = sys.argv[1:3]

    env = Environment(loader=FileSystemLoader([".", src_dir]))
    for name, func in data_sources.__dict__.items():
        env.globals[name] = func
    env.globals["len"] = len

    src_path = Path(src_dir)
    build_path = Path(build_dir)
    for tex_file in src_path.rglob("*.tex.j2"):
        relative_path = tex_file.relative_to(src_path)
        template = env.get_template(str(relative_path))
        rendered = template.render()
        output_file = build_path / relative_path.with_suffix("")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
