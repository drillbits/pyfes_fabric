===============================
Fabric ハンゾン @ pyfes 2013.07
===============================

はい https://github.com/pyspa/pyfes/blob/develop/201307.rst#fabric

Fabric is 何
============

読みましょう https://speakerdeck.com/drillbits/fabric-python-developers-festa-2013-dot-03-number-pyfes

いるもの
========

Python 2.7
----------

Py3 は Fabric 未対応です http://python3wos.appspot.com/

easy_install, pip, virtualenv
-----------------------------

まあ virtualenv なくてもいいけど

C コンパイラ
------------

pycrypto が C 使ってるんで gcc とか cygwin とか MinGW とか入れておいて下さい。

http://okuhiiro.daiwa-hotcom.com/wordpress/?p=657
Windows の場合はこんな感じでできないこともないみたいですが、正直検証とかしてないんで Mac か Linux がいいです。

ていうか Windows から Fabric 叩いたことないんで Mac か Linux がいいです。

Fab る対象の環境
----------------

ローカルに ssh で繋げる VM があれば最高です。スナップショット取っておきましょう。

外部のやつ（EC2 とか）でもいいですけど、オラコー社提供のインターネットは 22 番ポーツ使えないので各自 wimax とかでアレしてください。

まったくない人は色々と配布します。

色々と足りない人
================

何もかもがない、もしくは Windows なのでだるそうな人
---------------------------------------------------

VirtualBox のインストーラーと Ubuntu Desktop のイメージ配布するのでそれ使って下さい。

Ubuntu Desktop には Python が動く環境が入っています。

こいつを使う場合は自分自身をゲストとして Fabric を実行します。

Python + Fabric は動くけど VM がない
------------------------------------

VirtualBox のインストーラーと Ubuntu Server のイメージ配布するのでそれ使って下さい。

あなたのローカルをホスト、Ubuntu Server をゲストとして Fabric を使っていきます。

インストールとか
================

VirtualBox
----------

配布した VirtualBox-4.2.16-86992-OSX.dmg or VirtualBox-4.2.16-86992-Win.exe を使ってインストールしてください。

終わったら Oracle_VM_VirtualBox_Extension_Pack-4.2.16-86992.vbox-extpack もインストールしておいてください。

ダブルクリックすると VirtualBox が起動してそのまま道なりにインストールできます。

VM のインポート
---------------

VirtualBox を立ち上げて ファイル -> 仮想アプライアンスのインポート -> アプライアンスを開く から配布した ova ファイルをインポートします。

ホスト & ゲストが欲しい場合は pyfes_fabric_host.ova で Ubuntu Desktop を、ゲストだけでいい場合は pyfes_fabric_guest.ova で Ubuntu Server を入れて下さい。

ID とパスワードは共に pyfes です。

ローカルからゲストにつなぐ設定
------------------------------

VM を起動していない状態で VirtualBox の 環境設定 -> ネットワーク でホストオンリーネットワークを追加します。設定は以下のとおり。

:IPv4 アドレス: 10.0.0.1
:IPv4 ネットマスク: 255.255.255.0

上記以外はデフォルトで OK です。次は VM を右クリックして 設定 -> ネットワーク -> アダプター 2 でネットワークアダプターを有効化して

:割り当て: ホストオンリーアダプター
:名前: 上記で設定したやつ（たぶん vboxnet0）

pyfes_fabric_guest.ova には予め 10.0.0.2 が設定されているので、これで ssh pyfes@10.0.0.2 などで接続できるようになります。

変更したい場合は以下のようにしてください。

::

   $ sudo vim /etc/network/interfaces
   auto eth1
   iface eth1 inet static
       network 10.0.0.1
       netmask 255.255.255.0
       address 10.0.0.2  # <- ここを変更
   $ sudo /etc/init.d/networking restart

Fabric のインストール
=====================

ホスト（あなたのローカル環境 or Ubuntu Desktop）にインストールします。

::

   $ mkdir ~/.virtualenv
   $ virtualenv ~/.virtualenv/pyfes
   $ . ~/.virtualenv/pyfes/bin/activate
   (pyfes)$ pip install fabric

1 ファイルだけでやるやつ
========================

fabfile.py だけでやるやつ。

single ディレクトリの README.rst 読んで下さい。

複数ファイルでパッケージにするやつ
==================================

実際は 1 ファイルに全部書くとか無理ゲーなので複数ファイルにわけます。

package ディレクトリの README.rst 読んで下さい。
