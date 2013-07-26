# coding: utf-8
from fabric.api import env, task


@task
def localhost():
    env.hosts = ["localhost"]
    env.user = "pyfes"
    # env.key_filename = "id_rsa"
    env.roledefs = {
        "ap": ["localhost"],
        "db": ["localhost"],
    }


@task
def guest():
    env.hosts = ["10.0.0.2"]
    env.user = "pyfes"
    # env.key_filename = "id_rsa"
    env.roledefs = {
        "ap": ["10.0.0.2"],
        "db": ["10.0.0.2"],
    }


@task
def dev():
    env.hosts = [
        "10.0.0.11",
        "10.0.0.12",
        "10.0.0.21",
        "10.0.0.22",
        "10.0.0.23",
    ]
    env.user = "pyfes"
    # env.key_filename = "id_rsa"
    env.roledefs = {
        "ap": [
            "10.0.0.11",
            "10.0.0.21",
        ],
        "db": [
            "10.0.0.21",
            "10.0.0.22",
            "10.0.0.23",
        ],
    }
