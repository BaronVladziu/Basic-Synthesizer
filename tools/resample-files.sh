#!/bin/bash
#coding=utf-8

set -euo pipefail

# to enable remote execution
cd "$(dirname "$0")"
cd ..

# Parse arguments
if [ $# -lt 1 ] || [ $# -gt 1 ]; then
    echo "Usage: $0 <directory>"
    exit 2
fi

DIRECTORY=$1

# Resample all files in the directory
cd "${DIRECTORY}"
if [ -d "../resampled" ]; then
    rm -r "../resampled"
fi
mkdir ../resampled
for file in *; do sox ${file} -r 8000 ../resampled/${file}; done
