# Django学習メモ

## Django のコマンド

### startproject
```django-admin startproject mysite```

  プロジェクトを作成する。  
  初めて Django を使うのなら、最初のセットアップを行う必要があります。通常は、 Django のプロジェクト (project) を構成するコードを自動生成します。プロジェクトとは、データベースの設定や Django 固有のオプション、アプリケーション固有の設定などといった、個々の Django インスタンスの設定を集めたものです。  
  コマンドラインから、コードを置きたい場所に cd して、上記のコマンドを 実行してください。これを実行すると、現在のディレクトリに mysite ディレクトリが作成されます。動作しなければ django-admin 実行時の問題 を参照してください。  

### startapp
```py manage.py startapp [プロジェクト名]```

  このコマンドは [プロジェクト名] のディレクトリと基本的な Django プロジェクトに必要な View Model などのファイルを作成します。  

### runserver
```py manage.py runserver```

  Python で書かれた軽量の Web サーバである Django 開発サーバを起動しました。私たちはこれを Django と共に提供し、本番用のサーバ (Apache のような) の設定に煩わされることなく、本番の準備が整うまで迅速に開発を行えるようにしました。  
  今、注意すべきことは、このサーバを本番環境に近いところで使わないでください。このサーバーは、あくまでも開発用です。(私たちはウェブフレームワークを作る仕事をしているのであって、ウェブサーバーを作っているのではありません)。  
  サーバーが起動したら、ウェブブラウザで http://127.0.0.1:8000/ にアクセスしてみてください。おめでとうございます！」というページが表示され、ロケットが飛び立つのが見えると思います。成功です!

### makemigrations
```django-admin makemigrations [app_label [app_label ...]]```

  モデルに基づいて新しいマイグレーションを作成する。  
  マイグレーションは Django がモデル (そしてデータベーススキーマでもあります) の変更を保存する方法です。  
  マイグレーションは、ディスク上のただのファイルです。望むならば、新しいモデルのためのマイグレーションをファイル polls/migrations/0001_initial.py から読むこともできます。  
  安心してください、Django がマイグレーションのファイルを作成するたびにそれを毎回読む必要はありません。しかし、Django が行う変更を手動で微調整したいというときのために、マイグレーションは人間可読なファイルとして設計されています。  
  Djangoにモデルに変更があったこと(この場合、新しいものを作成しました)を伝え、そして変更を マイグレーション の形で保存することができました。

### migrate  
```python -m manage.py migrate```

  Django には、マイグレーションをあなたの代わりに実行し、自動でデータベーススキーマを管理するためのコマンドがあります。これは migrate と呼ばれるコマンドで、この後すぐに見ていきます。  
  モデルとは、データに関する唯一かつ決定的な情報源です。モデルには、保存しているデータの必須フィールドと動作が含まれています。Django は DRY 原則に従います。目標は、データモデルを一箇所で定義し、そこから自動的に物事を派生させることです。

## アプリケーションの作り方

### Django プロジェクトを作成する

  コマンド、 ```django-admin startproject [ルートディレクトリ名]``` を実行すると、カレントディレクトリに [ルートディレクトリ名] がディレクトリとして作成され、 Django を構成するプロジェクトファイルが作成される。  
  作成されたルートディレクトリに入り、 ```python manage.py [コマンド名]``` によって Django のコマンドは実行する。

### Django アプリケーションを作成する

  ルートディレクトリに入り、 ```py manage.py startapp [アプリケーション名]``` を実行することで、ルートディレクトリ配下にアプリケーションディレクトリが作成される。  

  ※アプリケーション（モジュール）は Pythonパス 上のどこにでも置くことができます。チュートリアルでは、プロジェクトのサブモジュールではなく、それ自身のトップレベルモジュールとしてインポートできるように、プロジェクトの manage.py ファイルと同じディレクトリにモジュールディレクトリを作成します。

### views.py, models.py, urls.py などの構成ファイルに変更を加える

- views.py に表示したいHTMLのモデル呼び出しを設定する。  
  ※1. 基本的に view とは javascript jQuery Python などのコードと変数を含むHTMLであり、最終的にレダリングされHTML出力されるドキュメントの見た目の設定である。  
  ※2. 以下は views.py BootstrapのCMSテンプレートを使う場合の一例：
  - 呼び出すデータベース
  - 使用するBootstrapのCMSテンプレート  
    （※ CMS とは ContentsManagementSystem の略称。WEBサイトやコンテンツを構築・管理・更新できるシステムのこと）
  - テンプレートに渡すデータ
- テンプレートを
- models.py に変更を加える。（まだ学習不足）
- プロジェクトルートディレクトリにある settings.py を編集し、 INSTALLED_APPS 設定に ```[アプリケーション名].apps.[アプリケーション名（クラスなので頭文字大文字）]Config```
 の [アプリケーション名（クラスなので頭文字大文字）]Config クラスを 先述のとおりドットつなぎのパスで追加する。

  ~~~python
  mysite/settings.py
      INSTALLED_APPS = [  
        '[アプリケーション名].apps.[アプリケーション名（クラスなので頭文字大文字）]Config',
        # ...他、最初からあるコンフィグ後略
  ~~~

- views.py を呼ぶための URL を対応付けをする。
  - **アプリケーションディレクトリ**に urls.py を新規作成して、 urlpatterns を設定する。

    ~~~python
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ~~~

  - ※上記、 path() の説明
    - 第一引数（必須） route ：第二引数の views.py を探す起点となるのはディレクトリ。上記は '' なのでドメイン直下 (http://hogehoge.fuga/) のルートパスを指定したことになる。
    - 第二引数（必須） view ：views.py の 関数 index
    - 第三引数（任意） kwargs ：キーと対になって対応する辞書変数を指定できる。（※まだ使ったことがないのでわからない）
    - 第四引数（任意） name ：人間にとってわかりやすい名前（エイリアス）をつけることができる。
  - アプリケーションディレクトリに新規作成した [アプリケーション名/urls.py] を、**プロジェクトルートディレクトリにある** urls.py に django.urls.include の import を追加して、 urlpatterns のリストに include() を挿入する。

    ~~~python
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
        # ...他、最初からあるコンフィグ後略
    ]
    ~~~

  - ※上記の説明
    - include() 関数は他の URLconf を参照することができる。 Django が include() に遭遇すると、そのポイントまでに一致した URL の部分を切り落とし、次の処理のために残りの文字列をインクルードされた URLconf へ渡す。  
    - include() の背景にある考えは、 URL を簡単にプラグ & プレイ可能にすること。 polls は独自の URLconf (polls/urls.py) を持っているので、 "/polls/" 、 "/fun_polls/" や、 "/content/polls/" といった、どんなパスルート下にも置けて、どこに置いてもきちんと動作する。  
    - URLパターンをインクルードするときはいつでも include() を使うべき。  
    - 唯一の例外は admin.site.urls はこれについての。
    - （※正直もうひとつ理解しきれていない。次も参照： [他の URLconfs をインクルードする](https://docs.djangoproject.com/ja/4.0/topics/http/urls/#including-other-urlconfs) ）

## Model, View, Template の設定のしかた

### モデル（models.py）を変更する

- 基本的な手順  

  1. models.py の変更を行う。
  2. モデル変更のマイグレーションを作成するために ```python manage.py makemigrations``` を実行する。
  3. データベースにこれらの変更をてきようするため ```python manage.py migrate``` を実行する。  

  　マイグレーションはとても強力なツールであり、プロジェクトの発展に合わせて、モデルを変更し続けていくことができます。データベースやテーブルを削除して作り直す必要はありません - マイグレーションは、データを失うことなしにデータベースをライブでアップグレードするよう特化しています。これらについてはチュートリアルの後の部分でもっと深くカバーしますが、今は、モデルの変更を実施するための、上記3ステップガイドを覚えておいてください。  
  マイグレーションの作成と適用のコマンドが分割されている理由は、マイグレーションをバージョン管理システムにコミットし、アプリとともに配布するためです。これによって、あなたの開発が容易になるだけでなく、他の開発者や本番環境にとって使いやすいものになります。

（※一時的メモ・次にやること、 https://docs.djangoproject.com/ja/4.0/intro/tutorial02/ の真ん中あたりのシェル実行をやってみる。 __str__ メソッドの追加までやった）





## manage.py のコマンド一覧

~~~powershell

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
~~~
