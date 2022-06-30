# Django学習メモ

## Django を使ったプロジェクトの作成

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
  サーバーが起動したら、ウェブブラウザで <http://127.0.0.1:8000/> にアクセスしてみてください。おめでとうございます！」というページが表示され、ロケットが飛び立つのが見えると思います。成功です!

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

#### ※付記『データベースの作成について』

  Djangoはモデル（データベース設計と入出力のモデル）からのマイグレーションによってSQL文による操作を必要とせずに、データベースを構成します。

- SQLite データベースを使う場合
  Djangoは特別な設定不要でプロジェクトルートに db.sqlite3 という単一ファイルで扱えるSQLiteデータベースを作成します。

- 他のデータベースを使う場合は、使用するSQLデータベースに対し "CREATE DATABASE データベース名;" でデータベースを作成する。
- mysite/settings.py の DATABESES を設定する。
- 'default' 項目内の以下のキーをデータベースの接続設定に合うよう変更する。
- ENGINE --  
  'django.db.backends.sqlite3'、  
  'django.db.backends.postgresql'、  
  'django.db.backends.mysql'  
  または 'django.db.backends.oracle' のいずれかにします。  
  その他の[バックエンド](https://docs.djangoproject.com/ja/4.0/ref/databases/#third-party-notes)も利用可能。  
- NAME --  
  SQLite を使っていない場合、ここで USER や PASSWORD そして HOST などを設定して、mysite/settings.py のデータベースユーザに「データベース作成」の権限があることを確認します。  
  これで settings.py に権限を与えることで、Djangoのモデルからデータベースを自動作成、 Admin サイトのGUIからデータベースを管理、変更することができます。  

  ※詳細については [DATABASES](https://docs.djangoproject.com/ja/4.0/ref/settings/#std-setting-DATABASES) のリファレンスドキュメントを参照してください。

## アプリケーションの新規作成の手順

### Django プロジェクトを作成する

  コマンド、 ```django-admin startproject [Djangoルートディレクトリ名]``` を実行すると、カレントディレクトリに [Djangoルートディレクトリ名] がディレクトリとして作成され、 Django を構成するプロジェクトファイルが作成される。この構成ファイルの一群がDjangoの本体となる。  
  作成されたルートディレクトリに入り、 ```python manage.py [コマンド名]``` によって Django のコマンドは実行する。

### Django アプリケーションを作成する

  ルートディレクトリに入り、 ```py manage.py startapp [アプリケーション名]``` を実行することで、ルートディレクトリ配下にアプリケーションディレクトリが作成される。  

  ※アプリケーション（モジュール）は Pythonパス 上のどこにでも置くことができます。チュートリアルでは、プロジェクトのサブモジュールではなく、それ自身のトップレベルモジュールとしてインポートできるように、プロジェクトの manage.py ファイルと同じディレクトリにモジュールディレクトリを作成します。

### views.py, models.py, urls.py などの構成ファイルに変更を加える

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
    - 第一引数（必須） route ：第二引数の views.py を探す起点となるのはディレクトリ。上記は '' なのでドメイン直下 (<http://hogehoge.fuga/>) のルートパスを指定したことになる。
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

#### ※要約した説明

- models.py に変更を加える。
- views.py に表示したいHTMLのモデル呼び出しを設定する。  
  ※1. 基本的に view とは javascript jQuery Python などのコードと変数を含むHTMLであり、最終的にレダリングされHTML出力されるドキュメントの見た目の設定である。  
  ※2. 以下は views.py BootstrapのCMSテンプレートを使う場合の一例：
  - 呼び出すデータベースを settings.py に設定する。
  - テンプレートディレクトリを作って、テンプレートの .html を書く。
    ~~Bootstrap の CMS テンプレートを使うこともできる。（できるの？ ここ間違ってない？）  
      （※ CMS とは ContentsManagementSystem の略称。WEBサイトやコンテンツを構築・管理・更新できるシステムのこと）~~
- views.py の各ビューのクラス、関数を urls.py にインデックスする。

#### ※！更に要約した説明！

  **■ （たぶん） Django フレームワークを動かすと settings.py がはじめに読み込まれるので、そこにリストされている様々なフレームワークの対象ファイルを作ったり書き換えたりして、任意のウェブサイトやウェブアプリケーションを作れということらしい。**


## Model, View, Template の設定のしかた

### モデル（models.py）を変更する

- 基本的な手順  

  1. models.py の変更を行う。
  2. モデル変更のマイグレーションを作成するために ```python manage.py makemigrations``` を実行する。
  3. データベースにこれらの変更をてきようするため ```python manage.py migrate``` を実行する。  

  　マイグレーションはとても強力なツールであり、プロジェクトの発展に合わせて、モデルを変更し続けていくことができます。データベースやテーブルを削除して作り直す必要はありません - マイグレーションは、データを失うことなしにデータベースをライブでアップグレードするよう特化しています。これらについてはチュートリアルの後の部分でもっと深くカバーしますが、今は、モデルの変更を実施するための、上記3ステップガイドを覚えておいてください。  
  マイグレーションの作成と適用のコマンドが分割されている理由は、マイグレーションをバージョン管理システムにコミットし、アプリとともに配布するためです。これによって、あなたの開発が容易になるだけでなく、他の開発者や本番環境にとって使いやすいものになります。

### ビュー（views.py）を変更する

- views.py に HttpResponse を返す関数を書く

  - 例）

  ~~~python
  def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
  ~~~

  呼び出す関数を定義（例では datail ）して、 request 以外の引数がある場合には、それも定義（例では question_id ）する。
  この関数は必ず return HttpResponse() で終わる必要があり、HttpResponse() の引数には、出力する内容（例では "You're looking at question %s." ）を書く。（続きの % 以降は引数を $s に渡す書き方。Python3以降では非推奨らしいので、 format メソッドとかの 別の書き方をすべき）

  ~~~python
  def detail(request, question_id):
    return HttpResponse("You're looking at question {question_id}")
  ~~~

- views.py に書いた HttpResponse 関数を、 HTTPリクエストに従い出力できるよう urls.py に反映させる。
  
  例）

  ~~~python
  from django.urls import path

  from . import views

  urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
  ]
  ~~~

  　誰かがWebサイトの 「/polls/34/」 をリクエストすると、 Django は ROOT_URLCONF に指定されている Python モジュール mysite.urls をロードします。そのモジュール内の urlpatterns という変数を探し、順番にパターンを検査していきます。 polls/ にマッチした箇所を見つけた後、一致した文字列 ("polls/") を取り除き、残りの文字列である "34/" を次の処理のために 『polls.urls』 の URLconf に渡します。これは '<int：question_id>/' に一致し、結果として下記のように detail() が呼び出されます。

  ~~~python
  detail(request=<HttpRequest object>, question_id=34)
  ~~~

### views.py から分離されたページのデザインを templates 内の index.html に書く
  
  1. Django が検索、ロードするテンプレートのHTMLファイルを作る。  
    - 仮にアプリケーションのディレクトリ名が ```Djangoルートディレクトリ~/polls/``` である場合は、その```polls/```ディレクトリ内に下記の通り ```polls/templates/polls/``` のディレクトリを作成し、そこに ```polls/templates/polls/index.html``` はじめとするテンプレートHTMLファイルを作成していく。  
  2. あ
  3. S

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
