import json
import glob
import os

notebooks = glob.glob(r'c:\RAG_Article\*.ipynb')
print(f"Found {len(notebooks)} notebooks\n")

for nb_path in notebooks:
    name = os.path.basename(nb_path)
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    metadata = nb.get('metadata', {})
    widgets = metadata.get('widgets', None)
    
    if widgets is None:
        print(f"  {name}: No widgets metadata - SKIP")
        continue
    
    widget_key = 'application/vnd.jupyter.widget-state+json'
    if widget_key not in widgets:
        print(f"  {name}: No widget-state+json key - SKIP")
        continue
    
    w = widgets[widget_key]
    if 'state' in w:
        print(f"  {name}: Already has 'state' key - OK")
        continue
    
    # Fix: wrap widget entries in a "state" key
    nb['metadata']['widgets'][widget_key] = {
        "state": w,
        "version_major": 2,
        "version_minor": 0
    }
    
    with open(nb_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
        f.write('\n')
    
    print(f"  {name}: FIXED (wrapped {len(w)} widget entries in 'state' key)")

print("\nDone!")
