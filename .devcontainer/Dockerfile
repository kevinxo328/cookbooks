# FROM mcr.microsoft.com/devcontainers/python:dev-3.12-bookworm
FROM python:3.12-slim-bookworm

RUN apt-get update && \
    pip install --upgrade pip

# Install Basic Packages
RUN pip install ipykernel jupyter python-dotenv

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.token=", "--ServerApp.password="]