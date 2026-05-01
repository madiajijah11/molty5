import sys, json
from graphify.build import build_from_json
from graphify.cluster import score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from pathlib import Path

extraction = json.loads(Path('graphify-out/.graphify_extract.json').read_text())
detection  = json.loads(Path('graphify-out/.graphify_detect.json').read_text())
analysis   = json.loads(Path('graphify-out/.graphify_analysis.json').read_text())

G = build_from_json(extraction)
communities = {int(k): v for k, v in analysis['communities'].items()}
cohesion = {int(k): v for k, v in analysis['cohesion'].items()}
tokens = {'input': extraction.get('input_tokens', 0), 'output': extraction.get('output_tokens', 0)}

# Labels based on community content analysis
labels = {
    0: "Core Game Loop",
    1: "API & Wallet Management",
    2: "Config & Documentation",
    3: "Combat Strategy AI",
    4: "Game Concepts & Systems",
    5: "Action & WebSocket Engine",
    6: "Web3 & Smart Contracts",
    7: "Setup & Configuration",
    8: "Dashboard Frontend",
    9: "Config & Logging",
    10: "Dashboard State",
    11: "Railway Deployment",
    12: "Runtime Modes",
    13: "Rate Limiting",
    14: "Bot Initialization",
    15: "Web3 Contracts Init",
    16: "Dashboard Init",
    17: "Game Init",
    18: "Memory Init",
    19: "Strategy Init",
    20: "Utils Init",
    21: "Web3 Init",
    22: "API Client Module",
    23: "State Router",
    24: "Dashboard State Module",
    25: "Action Sender Module",
    26: "Free Join Module",
    27: "Paid Join Module",
    28: "Room Selector",
    29: "Settlement Module",
    30: "WebSocket Engine",
    31: "Agent Memory",
    32: "Account Setup",
    33: "Identity Setup",
    34: "Wallet Setup",
    35: "Dashboard App JS",
    36: "Ethers JS",
    37: "Eth Account Setup",
    38: "Web3 Python",
}

# Regenerate questions with real community labels
questions = suggest_questions(G, communities, labels)

report = generate(G, communities, cohesion, labels, analysis['gods'], analysis['surprises'], detection, tokens, 'F:\Website\molty5', suggested_questions=questions)
Path('graphify-out/GRAPH_REPORT.md').write_text(report, encoding='utf-8')
Path('graphify-out/.graphify_labels.json').write_text(json.dumps({str(k): v for k, v in labels.items()}, indent=2))
print('Report updated with community labels')
print(f'Labels assigned to {len(labels)} communities')
