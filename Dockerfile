FROM python:3.13.11-slim

# copies the uv library image from docker hub
COPY --from=docker.io/astral/uv:0.9.26 /uv /uvx /bin/

# project's default directory in the container
WORKDIR /app

# add virtual env path to container PATH, this shortens the entrypoint arguments
ENV PATH="/app/.venv/bin:$PATH"

# Copy project dependencies into image (same as copying requiremnts.txt)
COPY pyproject.toml .python-version uv.lock pipeline.py ./

# run uv locked to install all project dependencies into venv
RUN uv sync --locked

# configure project entrypoint in the container, however program exits after execution.
ENTRYPOINT ["python", "pipeline.py"]