#!/bin/bash
source .venv/bin/activate
python3 src/fileasy.py "$@"
deactivate