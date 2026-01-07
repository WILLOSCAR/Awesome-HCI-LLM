#!/bin/bash
# Batch add HCI and LLM papers
# Usage: bash batch_add_papers.sh

cd /home/rjs/Workspace/codebase/Awesome-HCI-LLM

# === Ubicomp/IMWUT 2024-2025 Papers ===
echo "Adding Ubicomp/IMWUT papers..."

# Mental Health
python -m paper_cli add "https://dl.acm.org/doi/10.1145/3643547" HCI -t "mental health, LLM, text data" --no-git

# VitalInsight - LLM visualization
python -m paper_cli add "https://dl.acm.org/doi/10.1145/3643832" HCI -t "LLM, visualization, personal tracking, multimodal" --no-git

# GLOSS - LLM sensemaking
python -m paper_cli add "https://dl.acm.org/doi/10.1145/3643511" HCI -t "LLM, passive sensing, sensemaking" --no-git

# === arXiv HCI Papers (2024-2025) ===
echo "Adding arXiv HCI papers..."

# WheelPoser - IMU wheelchair users
python -m paper_cli add "2409.08494" HCI -t "IMU, pose estimation, wheelchair, accessibility" --no-git

# FRAME - egocentric VR/AR motion capture
python -m paper_cli add "2403.14509" HCI -t "VR, AR, motion capture, egocentric, stereo camera" --no-git

# HOI-M3 - Human-Object Interaction dataset
python -m paper_cli add "2404.01202" HCI -t "IMU, RGB, human object interaction, dataset, 3D tracking" --no-git

# SimXR - VR avatar control
python -m paper_cli add "2403.06194" HCI -t "VR, AR, avatar, pose estimation, headset" --no-git

# === arXiv LLM Agent Papers (2024-2025) ===
echo "Adding arXiv LLM Agent papers..."

# LAUI - LLM-Agent User Interface
python -m paper_cli add "2405.10718" LLM -t "LLM, agent, user interface, HCI, interaction" --no-git

# GUI Odyssey - LLM GUI agent survey
python -m paper_cli add "2411.10440" LLM -t "LLM, GUI agent, survey, computer use" --no-git

# GOI - Goal-Oriented Interface for LLM agents
python -m paper_cli add "2410.11905" LLM -t "LLM, agent, GUI, computer use, interface" --no-git

# ShowUI - vision-language model for UI understanding
python -m paper_cli add "2411.17465" LLM -t "LLM, UI, vision-language, GUI" --no-git

# OS-Atlas - foundation action model
python -m paper_cli add "2410.23218" LLM -t "LLM, agent, computer use, GUI, foundation model" --no-git

# === More HCI/IMU Papers ===
echo "Adding more HCI/IMU papers..."

# Transformer-based IMU pose estimation
python -m paper_cli add "2408.08374" HCI -t "IMU, transformer, pose estimation, calibration" --no-git

# Diffusion for loose IMU
python -m paper_cli add "2410.13788" HCI -t "IMU, diffusion, pose estimation, loose sensor" --no-git

echo "✓ Batch add completed!"
echo "Run: python -m paper_cli sync to update README and push to git"
