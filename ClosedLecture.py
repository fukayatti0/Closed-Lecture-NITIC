import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()


def extract_urls_from_site(url, pattern):
    response = requests.get(url)
    response.raise_for_status()
    urls = re.findall(pattern, response.text)
    return urls


def extract_lines_with_pattern_from_url(url, pattern):
    response = requests.get(url)
    response.raise_for_status()
    lines = response.text.splitlines()
    pattern_compiled = re.compile(pattern)
    lines_with_pattern = [
        line for line in lines if pattern_compiled.search(line)]
    return lines_with_pattern


def replace_chars_in_lines(lines, old_chars, new_chars):
    if len(old_chars) != len(new_chars):
        raise ValueError("old_charsと新_charsの長さが一致しません。")
    for old_char, new_char in zip(old_chars, new_chars):
        lines = [line.replace(old_char, new_char) for line in lines]
    return lines


def get_last_info():
    if os.path.exists('last_info.txt'):
        with open('last_info.txt', 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    return []


def save_last_info(info):
    with open('last_info.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(info))


def fetch_class_info():
    site_url = 'https://www.ibaraki-ct.ac.jp/info/archives/category/cancellation'
    url_pattern = r'<a href="https://www.ibaraki-ct.ac.jp/info/archives/(\d+)">休講情報'
    extracted_patterns = extract_urls_from_site(site_url, url_pattern)
    extracted_urls = [
        "https://www.ibaraki-ct.ac.jp/info/archives/" + url for url in extracted_patterns]

    if extracted_urls:
        target_url = extracted_urls[0]
        pattern = r'<p><mark style="background-color:#ccffcc" class="has-inline-color">.*?</mark><br>'
        result = extract_lines_with_pattern_from_url(target_url, pattern)

        old_chars = ['<p><mark style="background-color:#ccffcc" class="has-inline-color">', '<span style="text-decoration: underline;">',
                     '</mark>', '<br>', '</p>', '</span>', '<a href="', '">', '【特別研修日時間割】', '</a>', '☆', '◇', '◎', '◉']
        new_chars = ['\n', '\n', '', '\n', '\n', '\n', '',
                     '', '', '', '授業・教室変更：', '遠隔授業：', '補講：', '休講：']
        replaced_result = replace_chars_in_lines(result, old_chars, new_chars)

        return replaced_result
    else:
        return None


def main():
    info = fetch_class_info()
    if info:
        last_info = get_last_info()
        if info != last_info:
            print("最新の授業情報:\n" + "\n".join(info))
            print("\n" + "="*40 + "\n")
            save_last_info(info)
        else:
            print("新しい授業情報はありません。")
    else:
        print("授業情報を取得できませんでした。")


if __name__ == '__main__':
    main()
