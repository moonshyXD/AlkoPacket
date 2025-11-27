PYTHON = python3

.PHONY: lint
lint:
	ruff format .
	ruff check --fix
	ruff check .
	mypy .

.PHONY: run
run:
	uv run main.py

.PHONY: setup
setup:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync

.PHONY: testcover
testcover:
	pytest --cov=src --cov-report=term-missing