#!/bin/bash
#coding=utf-8

set -euo pipefail

# to enable remote execution
cd "$(dirname "$0")"
cd ..

# Parse arguments
if [ $# -lt 1 ] || [ $# -gt 1 ]; then
    echo "This script converts stereo wav file"
    echo "to mono wav file, by leaving only left channel."
    echo "Usage: $0 <directory>"
    exit 2
fi

DIRECTORY=$1

# Resample all files in the directory
cd "${DIRECTORY}"
if [ -d "../mono" ]; then
    rm -r "../mono"
fi
mkdir ../mono
for file in *; do
    sox "${file}" "../mono/${file}" remix 1;
done
