# ここでget-source.pyでダウンロードしたテキストファイルを開く
# その中の会話のテキストだけを抽出する
# Unicodeエンコーディングされている文字をUTF-8に復元する
# 辞書に格納する
import re

f = open('log-799931.html', 'r')


def checkMatch(msg, pat):
    pattern = re.compile(pat)
    result = pattern.match(msg)
    if result:
        print(result.group(0))
    else:
        print('Don\'t matched')


for data in f:
    checkMatch(data, r'message')
