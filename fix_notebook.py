import json

with open(r'c:\RAG_Article\Self_RAG.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

widget_key = 'application/vnd.jupyter.widget-state+json'
w = nb['metadata']['widgets'][widget_key]

print("Keys in widget-state+json:", list(w.keys())[:5], "...")
print("'state' in w:", 'state' in w)

# The fix: GitHub expects {"state": {...widgets...}} but we have the widgets directly
# Wrap the current content in a "state" key
if 'state' not in w:
    nb['metadata']['widgets'][widget_key] = {"state": w, "version_major": 2, "version_minor": 0}
    print("Fixed: wrapped widget entries in 'state' key")
else:
    print("Already has 'state' key, no fix needed")

with open(r'c:\RAG_Article\Self_RAG.ipynb', 'w', encoding='utf-8', newline='\n') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("Saved!")
