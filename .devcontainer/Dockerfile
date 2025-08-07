# FROM mcr.microsoft.com/devcontainers/python:dev-3.12-bookworm
FROM python:3.12-slim-bookworm

# Install venv and system dependencies
RUN apt-get update && \
    apt-get install -y python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment
ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH

# Upgrade pip in venv and install packages in venv
RUN $VENV_PATH/bin/pip install --upgrade pip && \
    $VENV_PATH/bin/pip install ipykernel jupyter python-dotenv cookiecutter

# Ensure venv is used by default
ENV PATH="$VENV_PATH/bin:$PATH"

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.token=", "--ServerApp.password="]