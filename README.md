# kuso-agent
相談をするとクソなアドバイスをしてくれるクソエージェント

## setup
1. `.env` を作成 `cp .env.example .env`
1. `.env` に API key など必要な値を設定

### Docker Compose での実行

1. `docker compose up -d`

`.env` はコンテナに自動で渡されます (ポートは固定で 8000 を使用)。ソースは `./kuso-agent` -> `/app/kuso-agent` にマウントされるため、ホストでの編集が即コンテナに反映されます。

### ローカルセットアップ (uv)

1. `uv sync`
1. `uv run adk web`

### 動作確認
1. ブラウザで `http://localhost:8000`
