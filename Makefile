.phony: build run docker-build docker-run

build:
	uv sync --locked 
run: build
	uv run invoice-summarizer
docker-build:
	docker build -t invoice-summarizer:latest .
docker-run:
	docker run -e ENV=prod -e EMAIL="${EMAIL_ADDRESS}" -e APP_PASSWORD="${APP_PASSWORD}" invoice-summarizer:latest uv run invoice-summarizer
	docker run -e ENV=prod -e EMAIL="${EMAIL}" -e APP_PASSWORD="${APP_PASSWORD}" invoice-summarizer:latest uv run invoice-summarizer
