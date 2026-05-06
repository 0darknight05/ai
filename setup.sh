#!/bin/bash

# --- Aesthetic Colors ---
CYAN='\033[0;36m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${CYAN}Starting AI Practical Setup...${NC}"

# 1. Extract uv if needed
if [ ! -f "./uv" ]; then
    echo -e "${GREEN}Extracting uv binary...${NC}"
    tar -xf uv.tar.xz
fi

chmod +x ./uv

# 2. Sync the environment (Crucial for Pr 5 Chatbot)
echo -e "${GREEN}Syncing dependencies (nltk, joblib, etc.)...${NC}"
./uv sync

# 3. NLTK Data Pre-load
# Practical 5 needs 'punkt' for the chatbot to tokenize text
echo -e "${GREEN}Pre-downloading NLTK data...${NC}"
./uv run python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

echo -e "${CYAN}==========================================${NC}"
echo -e "${GREEN}AI SETUP COMPLETE!${NC}"
echo -e "To run a practical, use:"
echo -e "${CYAN}./uv run python pracs/prX-name/file.py${NC}"
echo -e "${CYAN}==========================================${NC}"
