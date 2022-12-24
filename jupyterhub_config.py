# Configuration file for JupyterHub
import os

c = get_config()
#Используем Докер спавнер
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
#Подключаем готовый образ
c.DockerSpawner.image = os.environ["DOCKER_NOTEBOOK_IMAGE"]
#Используем эту команду
spawn_cmd = os.environ.get("DOCKER_SPAWN_CMD", "start-singleuser.sh")

c.DockerSpawner.cmd = spawn_cmd
#Задаем имя сети
network_name = os.environ["DOCKER_NETWORK_NAME"]

c.DockerSpawner.use_internal_ip = True

c.DockerSpawner.network_name = network_name

notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR") or "/home/jovyan/work"

c.DockerSpawner.notebook_dir = notebook_dir
#Маунтим даунные
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}

c.DockerSpawner.remove = True

c.DockerSpawner.debug = True
#Меняем
c.JupyterHub.hub_ip = "jupyterhub"
#Задаем порт
c.JupyterHub.hub_port = 8080
#Команда для кукисов
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
#Url
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"
#Аутенфикация пользователей
c.NativeAuthenticator.open_signup = True

admin = os.environ.get("JUPYTERHUB_ADMIN")

if admin:
    c.Authenticator.admin_users = [admin]
