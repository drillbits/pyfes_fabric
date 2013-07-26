# coding: utf-8
from fabric.api import roles, sudo, task
from fabric.contrib.files import append

import cuisine


@task
@roles("ap")
def setup_client():
    """MySQL Client をインストールして設定したのち起動する。
    """
    install_client()


@task
@roles("ap")
def install_client():
    cuisine.package_ensure_apt("mysql-client")


@task
@roles("db")
def setup_server():
    """MySQL Server をインストールして設定したのち起動する。
    """
    install_client()
    install_server()

    configure_server()

    restart()


@task
@roles("db")
def install_server():
    cuisine.package_ensure_apt("mysql-server")


@task
@roles("db")
def configure_server():
    append(
        filename="/etc/mysql/my.cnf",
        text="""
[client]
default-character-set = utf8
[mysqld]
character-set-server = utf8
skip-character-set-client-handshake
[mysql]
default-character-set = utf8
""",
        use_sudo=True,
    )


@task
@roles("db")
def start():
    sudo("start mysql")


@task
@roles("db")
def stop():
    sudo("stop mysql")


@task
@roles("db")
def restart():
    stop()
    start()
