# Cookbooks

This repository is intended for proof-of-concept (POC) development and testing features.

## Recommended Development Environment

It is recommended to use [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) to launch an isolated development environment.  
Please install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in Visual Studio Code to enable devcontainer support.

## Usage

1. Open this repository in [Visual Studio Code](https://code.visualstudio.com/).
2. Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension from the VS Code marketplace if you have not already.
3. You will be prompted to reopen the project in a container.
4. Follow the prompts to build and start the devcontainer environment.

## Notes

- The devcontainer setup provides an isolated environment for safe and reproducible POC and testing.
- For more details, refer to the `.devcontainer` directory.
- [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) is pre-installed in the devcontainer. You can use the following command to generate a new project from any template under the `boilerplates` directory:

  ```bash
  cookiecutter boilerplates/<template_folder>
  ```

  For example:
  ```bash
  cookiecutter boilerplates/openai
  ```

  This will interactively generate a new project based on the selected template.
