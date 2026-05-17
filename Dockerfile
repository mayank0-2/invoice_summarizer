FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim
WORKDIR /workspace

#Enable bytecode compilation
ENV uv_COMPILE_BYTECODE=1

#copy from the cache instead of linkin since it's a mounted volume
ENV UV_LINK_MODE=copy

# omit development dependencies 
ENV UV_NO_DEV=1

# Ensure installed tools can be executed out of the box.
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# Install certificate
RUN apt-get install ca-certificates

# env var used by request module
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
     uv sync --locked --no-install-project
 
COPY . /workspace
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
ENV PATH="/workspace/.venv/bin:$PATH"
