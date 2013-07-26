===============================
Fabric ハンゾン @ pyfes 2013.07
===============================

Package
=======

1 ファイルに全タスク書くのはつらい、という話です。

-f オプションを省略すると fabfile.py を使うということを書きましたが、fabfile という名前で Python のパッケージを作っておいても OK です。

内容はこのディレクトリの fabfile 見て下さい。

__init__.py でその他のモジュールを import しておきます。そうすると fab モジュール名.タスク みたいな感じで実行できます。

::

   # fabfile/__init__.py
   from . import hosts
   from . import repository

   # fabfile/hosts.py
   from fabric.api import task

   @task
   def localhost():
       env.hosts = ["localhost"]
       env.user = "pyfes"

1 ファイルの場合と違って、タスクにしたい関数には task デコレーターを付ける必要があります。

::

   $ fab --list
   Available commands:

     hosts.localhost
     repository.update

実行方法は一緒です。

::

   $ fab hosts.localhost repository.update:default

タスクの後の :default はそのタスクの関数の引数です。複数ある場合は :spam,ham,egg のようになります。

::

   # fabfile/repository.py
   from fabric.api import task
   from fabric.context_managers import cd

   @task
   def update(branch="default"):
       with cd("/var/www/repo"):
           run("hg pull")
           run("hg update {branch}".format(branch=branch))

このタスクの場合はリポジトリを指定したブランチに切り替えています。

Role
====

env.hosts はリストなので、複数のホストを指定できます。

ただ、すべてのホストに同じことをさせたいとは限りません。

例えば、上のリポジトリの更新は DB サーバーには必要ありません。

そこでロールですよ。

::

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

5 つのホストを指定した上で、env.roledefs というものを定義しています。ここでは ap というロールに 10.0.0.11-12 が、db というロールに 10.0.0.21-23 が指定されています。

リポジトリの更新は ap ロールのホストにだけ適用したいので、以下のようにします。

::

   # fabfile/repository.py
   from fabric.api import roles, task
   from fabric.context_managers import cd

   @task
   @roles("ap")
   def update(branch="default"):
       with cd("/var/www/repo"):
           run("hg pull")
           run("hg update {branch}".format(branch=branch))

これで repository.update は 10.0.0.11-12 に対してのみ実行されるようになります。便利。

その他便利機能
==============

スライド（ https://speakerdeck.com/drillbits/fabric-python-developers-festa-2013-dot-03-number-pyfes ）の 122 ページ以降とこのディレクトリの fabfile を見て感じ取って下さい。

とりあえず cuisine とか fabtools とかを pip install しておくといいかも。

あと @shiumachi 先生が午後のプレゼンで色々話してくれます。
