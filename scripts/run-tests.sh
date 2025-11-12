#!/usr/bin/env bash

echo ""
echo "Format code:"
uv run ruff format .
echo ""

echo "Lint code:"
uv run ruff check .
echo ""

echo "Type check:"
uv run mypy src/
echo ""

echo "Run tests:"
uv run pytest
echo ""

echo "Run tests with coverage:"
uv run pytest --cov
echo ""
