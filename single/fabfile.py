# coding: utf-8
from fabric.api import env, local, run

# env.hosts = ["localhost"]
# env.hosts = ["10.0.0.2"]
# env.user = "pyfes"
# env.key_filename = "id_rsa"


# task
def hello():
    local("echo hello")  # shell command


def uname():
    local("uname")


def remote_uname():
    run("uname")


# hosts
def localhost():
    env.hosts = ["localhost"]
    env.user = "pyfes"
    # env.key_filename = "id_rsa"


def guest():
    env.hosts = ["10.0.0.2"]
    env.user = "pyfes"
    # env.key_filename = "id_rsa"
