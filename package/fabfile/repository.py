# coding: utf-8
from fabric.api import env, run, task, roles
from fabric.context_managers import cd
from fabric.contrib.files import exists

import cuisine


@task
@roles("ap")
def clone():
    """リポジトリをクローンする。
    """
    with cuisine.mode_sudo():
        cuisine.dir_ensure(
            location="/var/www",
            recursive=True,
            mode="755",
            owner=env.user,
            group=env.user,
        )

    if exists("/var/www/repo"):
        return

    with cd("/var/www"):
        run("hg clone https://bitbucket.org/aodag/addressbook")


@task
@roles("ap")
def update(branch="default"):
    """リポジトリを指定されたブランチで update する。
    """
    with cd("/var/www/repo"):
        run("hg pull")
        run("hg update {branch}".format(branch=branch))
