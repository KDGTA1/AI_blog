# ブログアプリのセットアップ手順

このリポジトリをクローンして、友達と一緒に編集するための手順です。

## 1. リポジトリをクローンする

```bash
git clone https://github.com/KDGTA1/AI_blog.git
cd AI_blog
```

## 2. 仮想環境を作成して有効化する

```bash
# 仮想環境を作成
python3 -m venv .venv

# 仮想環境を有効化
# macOS/Linuxの場合:
source .venv/bin/activate
# Windowsの場合:
.venv\Scripts\activate
```

## 3. 必要なパッケージをインストールする

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. データベースをセットアップする

```bash
python manage.py migrate
```

## 5. 開発サーバーを起動する

```bash
python manage.py runserver
```

ブラウザで `http://127.0.0.1:8000/` を開くとブログアプリが表示されます。

## 6. 管理画面を使う場合（オプション）

```bash
python manage.py createsuperuser
```

その後、`http://127.0.0.1:8000/admin/` にアクセスしてログインできます。

---

## 友達と一緒に編集する方法

### 変更をプッシュする前に

1. **最新の変更を取得する**
   ```bash
   git pull origin main
   ```

2. **変更をコミットする**
   ```bash
   git add .
   git commit -m "変更内容の説明"
   ```

3. **変更をプッシュする**
   ```bash
   git push origin main
   ```

### 注意事項

- 複数人で同時に編集する場合は、**必ず `git pull` してから編集を始める**
- 同じファイルを編集すると競合（コンフリクト）が発生する可能性があります
- 競合が発生した場合は、GitHub上で解決するか、手動でマージする必要があります

---

## トラブルシューティング

### リポジトリにアクセスできない場合

1. **コラボレーターとして追加されているか確認**
   - リポジトリのオーナー（KDGTA1）に連絡して、コラボレーターとして追加してもらう
   - GitHubのリポジトリページ → Settings → Collaborators で追加

2. **GitHubアカウントでログインしているか確認**
   - ブラウザでGitHubにログインしているか確認

### クローンできない場合

- インターネット接続を確認
- GitHubのURLが正しいか確認: `https://github.com/KDGTA1/AI_blog.git`

### サーバーが起動しない場合

- 仮想環境が有効化されているか確認
- 必要なパッケージがインストールされているか確認: `pip install -r requirements.txt`
- ポート8000が既に使用されている場合は、別のポートを指定: `python manage.py runserver 8001`

