# 閉講情報 NITIC

このプロジェクトは茨城高専のウェブサイトから休講情報を取得し、出力します。

htmlから要素を抽出しているだけなので、使えなくなる可能性があります。

~~APIがほしい~~

## 特徴

- 休講情報を含むサイトのURLを抽出します。
- 抽出したURLから特定のパターンを含む行を抽出します。
- 抽出した行の特定の文字を置換して情報をフォーマットします。
- 最新の情報をファイルに保存し、更新をチェックします。

## 必要条件

- Python 3.x
- `requests`
- `python-dotenv`

## インストール

1. リポジトリをクローンします:

    ```sh
    git clone https://github.com/yourusername/Closed-Lecture-NITIC.git
    cd Closed-Lecture-NITIC
    ```

2. 必要なライブラリをインストールします:

    ```sh
    pip install -r requirements.txt
    ```

## 使用方法

スクリプトを実行します:

```sh
python3 ClosedLecture.py
```

## 関数

- `extract_urls_from_site(url, pattern)`: 指定された正規表現パターンを使用してサイトからURLを抽出します。
- `extract_lines_with_pattern_from_url(url, pattern)`: 指定されたパターンを含む行をURLから抽出します。
- `replace_chars_in_lines(lines, old_chars, new_chars)`: 提供された古い文字と新しい文字に基づいて行の文字を置換します。
- `get_last_info()`: `last_info.txt` から最後に保存された情報を取得します。
- `save_last_info(info)`: 提供された情報を `last_info.txt` に保存します。
- `fetch_class_info()`: ウェブサイトから閉講情報を取得し処理します。
- `main()`: スクリプトを実行するメイン関数。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。
