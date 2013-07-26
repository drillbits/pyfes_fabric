===============================
Fabric ハンゾン @ pyfes 2013.07
===============================

1 ファイルだけでやるやつです。

-f オプションで指定もできますが、だるいので省略したい。省略すると fabfile.py を使います。

内容はこのディレクトリの fabfile.py 見て下さい。

::

   $ fab --list
   Available commands:

    guest
    hello
    local
    remote_uname
    uname

定義した関数がそのままタスクになります。

fabric.api から色んな便利関数が import できます。

:local: fab コマンド叩いた環境で引数に指定したコマンドを実行
:run: fab コマンドの -H オプションで指定した環境で同上

local コマンドを使っているタスクを実行すると以下のようになります。

::

   $ fab hello
   [localhost] local: echo hello
   hello

   Done.
   $ fab uname
   [localhost] local: uname
   Linux

   Done.

run コマンドを使っているタスクを実行する場合は -u でユーザーを、-H でホストを指定します。今回は SSH Key の設定をしていないので、パスワードの入力も必要になります。

ちなみに -H を指定しなかった場合は、コマンド実行後に入力を求められます。一方 -u を指定しなかった場合は現在実行しているユーザー名と同じものが用いられます。

::

   $ fab remote_uname -u pyfes -H 10.0.0.2
   [10.0.0.2] Executing task 'remote_uname'
   [10.0.0.2] run: uname
   [10.0.0.2] Passphrase for private key:
   [10.0.0.2] out: Linux
   [10.0.0.2] out:

   Done.
   Disconnecting from 10.0.0.2... done.

localhost を指定すれば localhost に対して実行もできます。guest を別途用意していない場合はこちらで。どちらにしろ ssh でつないでいます。

::

   $ fab remote_uname -u pyfes -H localhost
   [localhost] Executing task 'remote_uname'
   [localhost] run: uname
   [localhost] Passphrase for private key:
   [localhost] out: Linux
   [localhost] out:

   Done.
   Disconnecting from localhost... done.

タスクはつなげて実行できます。

::

   $ fab hello uname
   [localhost] local: echo hello
   hello
   [localhost] local: uname
   Linux

   Done.

-H オプションをいちいちつけるのはだるいので、fabfile 内に定義もできます。

::

   # coding: utf-8
   from fabric.api import env, local, run

   env.hosts = ["10.0.0.2"]
   env.user = "pyfes"

   def remote_uname():
       run("uname")

ホストの指定自体をタスクにすることもできます。最初にホスト指定のタスクを実行した後、任意のタスクをつなげて実行します。実際は大抵この方法で実行対象を指定します。

::

   $ fab guest remote_uname
   [10.0.0.2] Executing task 'remote_uname'
   [10.0.0.2] run: uname
   [10.0.0.2] Passphrase for private key:
   [10.0.0.2] out: Linux
   [10.0.0.2] out:

   Done.
   Disconnecting from 10.0.0.2... done.

最初に実行するタスクを変えるだけで色々な環境に対してタスクを実行できます。

::

   $ fab dev restart
   $ fab staging restart
   $ fab production restart
