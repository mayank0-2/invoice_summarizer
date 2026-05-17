.phony: build

build:
	uv sync --locked 
run: build
	uv run invoice-summarizer

