import json
from pathlib import Path

# Read all chunk files and merge
chunks = []
for i in range(1, 5):
    chunk_file = Path('graphify-out/.graphify_chunk_0' + str(i) + '.json')
    if chunk_file.exists():
        try:
            data = json.loads(chunk_file.read_text())
            if 'nodes' in data and 'edges' in data:
                chunks.append(data)
                print(f'Loaded chunk {i}: {len(data.get("nodes", []))} nodes, {len(data.get("edges", []))} edges')
            else:
                print(f'Warning: chunk {i} missing nodes/edges')
        except json.JSONDecodeError:
            print(f'Warning: chunk {i} has invalid JSON')
    else:
        print(f'Warning: chunk {i} missing from disk')

# Merge all chunks
merged_nodes = []
merged_edges = []
merged_hyperedges = []
seen_nodes = set()

for chunk in chunks:
    for n in chunk.get('nodes', []):
        if n['id'] not in seen_nodes:
            seen_nodes.add(n['id'])
            merged_nodes.append(n)
    merged_edges.extend(chunk.get('edges', []))
    merged_hyperedges.extend(chunk.get('hyperedges', []))

# Save merged semantic results
result = {
    'nodes': merged_nodes,
    'edges': merged_edges,
    'hyperedges': merged_hyperedges,
    'input_tokens': sum(c.get('input_tokens', 0) for c in chunks),
    'output_tokens': sum(c.get('output_tokens', 0) for c in chunks),
}
Path('graphify-out/.graphify_semantic_new.json').write_text(json.dumps(result, indent=2))
print(f'Merged semantic: {len(merged_nodes)} nodes, {len(merged_edges)} edges, {len(merged_hyperedges)} hyperedges')
