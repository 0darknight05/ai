#!/bin/bash

# --- Aesthetic Colors ---
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}Starting AI Practical Setup...${NC}"

# 1. System Dependency Check (Tkinter)
# This requires sudo. If you don't have it, this step will fail gracefully.
echo -e "${GREEN}Attempting to install system Tkinter...${NC}"
if command -v dnf &> /dev/null; then
    sudo -n dnf install -y python3-tkinter || echo -e "${RED}Warning: Sudo access denied. Tkinter must be installed manually.${NC}"
fi

# 2. Extract uv if needed
if [ ! -f "./uv" ]; then
    echo -e "${GREEN}Extracting uv binary...${NC}"
    tar -xf uv.tar.xz
fi

chmod +x ./uv

# 3. Sync the environment
echo -e "${GREEN}Syncing dependencies (nltk, joblib, etc.)...${NC}"
./uv sync

# 4. NLTK Data Pre-load
echo -e "${GREEN}Pre-downloading NLTK data...${NC}"
./uv run python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

echo -e "${CYAN}==========================================${NC}"
echo -e "${GREEN}AI SETUP COMPLETE!${NC}"
echo -e "To run a practical, use:"
echo -e "${CYAN}./uv run python pracs/prX-name/file.py${NC}"
echo -e "${CYAN}==========================================${NC}"
