# JupyDock

A reference deployment of JupyterHub, a multi-user Jupyter Notebook environment, using Docker is provided by JupyDock.

## Features

- Creating a quick-to-launch JupyterHub demo environment.
- Providing small groups, teams, or departments with a multi-user Jupyter Notebook environment.

## Quick Start

- Clone repo: git clone https://github.com/vkusnoperiod/JupyDock.git
- DockerSpawner is used to provide each user with ditstinguished container on the same host.

## Development

- You can easily use JupyterHub-Docker with custom directories, ports and other.
- To edit JupyterHub port, replace `80` with any other port number you need 'in' docker-compose.yml file.
- Im using JupyterHub Native Authenticator to authenticate users.

## Edit

- In build script you can change image name or add any needed flags.

