#!/bin/bash
#coding=utf-8

set -euo pipefail

# to enable remote execution
cd "$(dirname "$0")"
cd ..

# Parse arguments
if [ $# -lt 2 ] || [ $# -gt 2 ]; then
    echo "Usage: $0 <directory> <out_frequency>"
    exit 2
fi

DIRECTORY=$1
OUT_FREQUENCY=$2

# Resample all files in the directory
cd "${DIRECTORY}"
if [ -d "../resampled" ]; then
    rm -r "../resampled"
fi
mkdir ../resampled
for file in *; do
    sox "${file}" -r "${OUT_FREQUENCY}" "../resampled/${file}";
done
