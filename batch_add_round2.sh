#!/bin/bash
# Batch add verified HCI and LLM papers (Round 2)
# These IDs are verified from academic sources

cd /home/rjs/Workspace/codebase/Awesome-HCI-LLM

echo "Adding more verified arXiv papers..."

# === 2024-2025 HCI/VR/AR Papers ===
python -m paper_cli add "2503.14144" HCI -t "VR, AR, egocentric, motion capture, FRAME" --no-git 2>&1 | head -20

python -m paper_cli add "2404.15549" HCI -t "IMU, RGB, HOI, dataset, tracking" --no-git 2>&1 | head -20

python -m paper_cli add "2403.18309" HCI -t "VR, AR, simulated avatar, headset" --no-git 2>&1 | head -20

# === 2024-2025 LLM/Agent Papers ===
python -m paper_cli add "2405.11718" Agent -t "LLM, agent, UI, LAUI, interface" --no-git 2>&1 | head -20

python -m paper_cli add "2409.12269" LLM -t "LLM, GUI, agent, survey" --no-git 2>&1 | head -20

python -m paper_cli add "2410.23218" Agent -t "LLM, GUI, agent, OS-ATLAS, foundation" --source "arXiv(v1) 2024" --no-git 2>&1 | head -20

python -m paper_cli add "2412.05241" Agent -t "LLM, agent, computer use, evaluation" --no-git 2>&1 | head -20

# === Ubicomp/CHI 2024 papers (via DOI) ===
python -m paper_cli add "10.1145/3654781" HCI -t "smartwatch, LLM, wearable" --no-git 2>&1 | head -20

python -m paper_cli add "10.1145/3613904.3642181" HCI -t "LLM, HCI, CHI, interaction" --no-git 2>&1 | head -20

echo "✓ Round 2 completed!"
