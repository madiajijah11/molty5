import json
from pathlib import Path
from datetime import datetime, timezone
from graphify.detect import save_manifest

# Save manifest for --update
detect = json.loads(Path('graphify-out/.graphify_detect.json').read_text())
save_manifest(detect['files'])

# Update cumulative cost tracker
extract = json.loads(Path('graphify-out/.graphify_extract.json').read_text())
input_tok = extract.get('input_tokens', 0)
output_tok = extract.get('output_tokens', 0)

cost_path = Path('graphify-out/cost.json')
if cost_path.exists():
    cost = json.loads(cost_path.read_text())
else:
    cost = {'runs': [], 'total_input_tokens': 0, 'total_output_tokens': 0}

cost['runs'].append({
    'date': datetime.now(timezone.utc).isoformat(),
    'input_tokens': input_tok,
    'output_tokens': output_tok,
    'files': detect.get('total_files', 0),
})
cost['total_input_tokens'] += input_tok
cost['total_output_tokens'] += output_tok
cost_path.write_text(json.dumps(cost, indent=2))

print(f'This run: {input_tok:,} input tokens, {output_tok:,} output tokens')
print(f'All time: {cost["total_input_tokens"]:,} input, {cost["total_output_tokens"]:,} output ({len(cost["runs"])} runs)')

# Clean up temp files
import os
temp_files = [
    'graphify-out/.graphify_detect.json',
    'graphify-out/.graphify_extract.json',
    'graphify-out/.graphify_ast.json',
    'graphify-out/.graphify_semantic.json',
    'graphify-out/.graphify_analysis.json',
    'graphify-out/.graphify_labels.json',
    'graphify-out/.graphify_semantic_new.json',
    'graphify-out/.graphify_cached.json',
    'graphify-out/.graphify_uncached.txt',
]
for f in temp_files:
    try:
        Path(f).unlink()
        print(f'Removed {f}')
    except FileNotFoundError:
        pass

# Remove chunk files
for i in range(1, 5):
    chunk_file = Path(f'graphify-out/.graphify_chunk_0{i}.json')
    try:
        chunk_file.unlink()
        print(f'Removed chunk {i}')
    except FileNotFoundError:
        pass

print('\nGraph complete. Outputs in F:\\Website\\molty5\\graphify-out\\')
print()
print('  graph.html            - interactive graph, open in browser')
print('  GRAPH_REPORT.md       - audit report')
print('  graph.json            - raw graph data')
