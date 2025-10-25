#!/usr/bin/env python3
"""Normalize notebook cell metadata for this repo's notebooks.

For each cell in the given notebook file, this script will:
- If a top-level `id` exists on the cell, move it into `cell['metadata']['id']`.
- Ensure `cell['metadata']['language']` exists and is set to 'python' for code cells and 'markdown' for markdown cells.

Usage: python scripts/fix_notebook_metadata.py fpd_rule_mining.ipynb
"""
import json
import sys
from pathlib import Path

def fix(path: Path):
    obj = json.loads(path.read_text())
    changed = False
    for cell in obj.get('cells', []):
        md = cell.get('metadata')
        if md is None or not isinstance(md, dict):
            md = {}
            cell['metadata'] = md
            changed = True

        # Move top-level id into metadata.id if present
        if 'id' in cell and 'id' not in md:
            md['id'] = cell.pop('id')
            changed = True

        # Ensure metadata.language exists
        if 'language' not in md:
            if cell.get('cell_type') == 'code':
                md['language'] = 'python'
            else:
                md['language'] = 'markdown'
            changed = True

    if changed:
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=1))
        print(f"Updated notebook metadata: {path}")
    else:
        print(f"No changes needed for: {path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: fix_notebook_metadata.py <notebook.ipynb>")
        sys.exit(1)
    fix(Path(sys.argv[1]))
