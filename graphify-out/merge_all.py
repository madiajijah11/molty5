import json
from pathlib import Path

# Check if cached results exist
cached_file = Path('graphify-out/.graphify_cached.json')
if cached_file.exists():
    cached = json.loads(cached_file.read_text())
    print(f'Found cached: {len(cached.get("nodes", []))} nodes')
else:
    cached = {'nodes':[],'edges':[],'hyperedges':[]}
    print('No cached results found')

# Read new results
new = json.loads(Path('graphify-out/.graphify_semantic_new.json').read_text())

# Merge
all_nodes = cached['nodes'] + new.get('nodes', [])
all_edges = cached['edges'] + new.get('edges', [])
all_hyperedges = cached.get('hyperedges', []) + new.get('hyperedges', [])

# Deduplicate nodes by id
seen = set()
deduped = []
for n in all_nodes:
    if n['id'] not in seen:
        seen.add(n['id'])
        deduped.append(n)

merged = {
    'nodes': deduped,
    'edges': all_edges,
    'hyperedges': all_hyperedges,
    'input_tokens': new.get('input_tokens', 0),
    'output_tokens': new.get('output_tokens', 0),
}
Path('graphify-out/.graphify_semantic.json').write_text(json.dumps(merged, indent=2))
print(f'Semantic merged: {len(deduped)} nodes, {len(all_edges)} edges ({len(cached["nodes"])} from cache, {len(new.get("nodes",[]))} new)')
