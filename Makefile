.phony: build

build:
	uv sync --locked && uv run invoice-summarizer
