FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim

COPY . /workspace

ENV UV_NO_DEV=1

WORKDIR /workspace

RUN uv sync --locked
