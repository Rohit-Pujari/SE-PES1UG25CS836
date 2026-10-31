#!/usr/bin/env bash
set -euo pipefail

python3 -m venv venv
# shellcheck disable=SC1091
source venv/bin/activate
python -m pip install flask pyyaml pylint bandit flake8

# Baseline reports (the original assigned program is preserved in this folder).
python -m pylint hostel_allocation_original.py > pylint_before.txt 2>&1 || true
python -m bandit -r hostel_allocation_original.py > bandit_before.txt 2>&1 || true
python -m flake8 hostel_allocation_original.py > flake8_before.txt 2>&1 || true

# Reports for the corrected program.
python -m pylint hostel_allocation.py > pylint_after.txt 2>&1 || true
python -m bandit -r hostel_allocation.py > bandit_after.txt 2>&1 || true
python -m flake8 hostel_allocation.py > flake8_after.txt 2>&1 || true

printf 'Reports generated. Review the findings and Pylint score before submitting.\n'
