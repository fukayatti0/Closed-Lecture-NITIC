# Pythonの公式イメージを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 依存関係ファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションを実行
CMD ["python", "ClosedLecture.py"]