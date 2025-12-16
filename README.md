## Django ブログアプリ

このディレクトリには、Django 製のシンプルなブログアプリ `myblog` が含まれています。

### セットアップ

```bash
cd /Users/ria7/Desktop/ブログ
python3 -m venv .venv
source .venv/bin/activate  # Windows の場合: .venv\Scripts\activate
pip install -r requirements.txt
```

### 開発サーバー起動

```bash
source .venv/bin/activate
python manage.py runserver
```

ブラウザで `http://127.0.0.1:8000/` を開くと、ブログの**記事一覧**が表示されます。

- `/` または `/blog/` : 記事一覧
- `/blog/post/new/` : 新規記事作成
- `/blog/post/<id>/` : 記事詳細

### 管理画面

管理画面に入るには、スーパーユーザーを作成します。

```bash
source .venv/bin/activate
python manage.py createsuperuser
```

その後、`http://127.0.0.1:8000/admin/` にアクセスしてログインしてください。


# AI_blog
