#!/usr/bin/env bash

set -euo pipefail

uv run ruff check solutions/ tests/
uv run mypy --strict solutions/ tests/
uv run pyright --warnings solutions/ tests/
uv run isort --profile black --check solutions/ tests/
find solutions/ tests/ -name "*.py" -exec ./check_python_file.sh {} +
