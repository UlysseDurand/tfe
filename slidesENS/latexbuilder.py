#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import sys
from pathlib import Path

def main():
    src_folder, build_folder = sys.argv[1:3]
    
    env = Environment(loader=FileSystemLoader(['.', src_folder]))
    import manual_build
    for name, func in manual_build.__dict__.items():
        env.globals[name] = func
    env.globals['len'] = len
    
    src_path = Path(src_folder)
    build_path = Path(build_folder)
    for tex_file in src_path.rglob("*.tex.j2"):
        relative_path = tex_file.relative_to(src_path)
        template = env.get_template(str(relative_path).replace('\\', '/'))
        rendered = template.render()
        output_file = build_path / relative_path.with_suffix('')  # This removes .j2 but keeps .tex
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(rendered, encoding='utf-8')



if __name__ == "__main__":
    main()