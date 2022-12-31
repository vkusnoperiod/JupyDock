# JupyDock

A reference deployment of JupyterHub, a multi-user Jupyter Notebook environment, using Docker is provided by JupyDock.

## Features

- Creating a quick-to-launch JupyterHub demo environment.
- Providing small groups, teams, or departments with a multi-user Jupyter Notebook environment.

## Copy

- Clone repository below:
`git clone https://github.com/vkusnoperiod/JupyDock.git`

## Running 

Following steps to start JupyDock:
 - Download all required things (written in requirements.txt)
 - Create a Docker-Compose by witing this command in shell `docker-compose build`
 - Start a container using command `docker-compose up` You can also write -d `docker-compose up -d` for running in detached mode or other optional things that are provided by docker environment.
 - Once you have done the following steps, open any browser and go to this page: `localhost:80`


## Development

- DockerSpawner is used to provide each user with ditstinguished container on the same host.
- You can easily use JupyDock with custom directories, ports and other.
- Im using JupyterHub Native Authenticator to authenticate users.

## Edit

- In build script you can change image name or add any needed flags.
- To edit JupyterHub port, replace `80` with any other port number you need in docker-compose.yml file.

