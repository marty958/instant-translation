# coding: utf-8
import sys
import requests
import pyperclip

url = "https://translate.google.com/translate_a/single"

while(1):
    mode = input('Select Mode: ej(English -> Japanese), je(Japanese -> English), or quit\n> ')
    # print(mode)
    if mode == "quit":
        sys.exit(0)
    elif mode == "ej" or mode == "je":
        if mode == "ej":
            source_lang     = "en"
            translate_lang  = "ja"
            source          = input('Pass the sentence to translate.\n> ')
        elif mode == "je":
            source_lang     = "ja"
            translate_lang  = "en"
            source          = input("翻訳する文を入力してください.\n> ")
        headers = {
            "Host": "translate.google.com",
            "Accept": "*/*",
            "Cookie": "",
            "User-Agent": "GoogleTranslate/5.9.59004 (iPhone; iOS 10.2; ja; iPhone9,1)",
            "Accept-Language": "ja-jp",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }
        params = {
            "client": "it",
            "dt": ["t", "rmt", "bd", "rms", "qca", "ss", "md", "ld", "ex"],
            "otf": "2",
            "dj": "1",
            "q": source,
            "hl": "ja",
            "ie": "UTF-8",
            "oe": "UTF-8",
            "sl": source_lang,
            "tl": translate_lang,
        }
        res = requests.get(url=url,
                           headers=headers,
                           params=params,)
        res = res.json()
        dest = res["sentences"][0]["trans"]
        print(dest)
        pyperclip.copy(dest)
    else:
        print("Retry")
