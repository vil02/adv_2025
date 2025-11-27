#!/usr/bin/env bash

set -euo pipefail

uv run ruff check solutions/ tests/
uv run mypy solutions/ tests/
find solutions/ tests/ -name "*.py" -exec ./check_python_file.sh {} +
