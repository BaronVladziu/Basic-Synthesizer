#!/bin/bash
#coding=utf-8

set -euo pipefail

# to enable remote execution
cd "$(dirname "$0")"

virtualenv -p /usr/bin/python3.6 env

source env/bin/activate
pip3 install --upgrade pip
python3 --version
pip3 --version
pip3 install -r requirements.txt
