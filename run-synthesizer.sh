#!/bin/bash
#coding=utf-8

set -euo pipefail

# to enable remote execution
cd "$(dirname "$0")"

# Parse arguments
if [ $# -lt 1 ] || [ $# -gt 1 ]; then
    echo "Usage: $0 <synthesis_command>"
    exit 2
fi

SYNTHESIS_COMMAND=$1

# Run synthesizer
source env/bin/activate
./main.py --command "${SYNTHESIS_COMMAND}"
