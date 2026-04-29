#!/usr/bin/env bash

set -euo pipefail

uv run --frozen --no-build ruff check solutions/ tests/
uv run --frozen --no-build mypy --strict solutions/ tests/
uv run --frozen --no-build pyright --warnings solutions/ tests/
uv run --frozen --no-build isort --profile black --check solutions/ tests/
find solutions/ tests/ -name "*.py" -exec ./check_python_file.sh {} +
