# FROM mcr.microsoft.com/devcontainers/python:dev-3.12-bookworm
FROM python:3.12-slim-bookworm

# Install venv and system dependencies
RUN apt-get update && \
    apt-get install -y python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment
ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH

# Create a new non-root user 'developer' with passwordless sudo and set permissions after venv exists
RUN apt-get update && \
    apt-get install -y sudo && \
    useradd -m -s /bin/bash developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    chown -R developer:developer /opt/venv && \
    mkdir -p /workspace && chown -R developer:developer /workspace

# Upgrade pip in venv and install packages in venv
RUN $VENV_PATH/bin/pip install --upgrade pip && \
    $VENV_PATH/bin/pip install ipykernel jupyter python-dotenv cookiecutter

# Ensure venv is used by default
ENV PATH="$VENV_PATH/bin:$PATH"

# Switch to non-root user
USER developer

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.token=", "--ServerApp.password="]