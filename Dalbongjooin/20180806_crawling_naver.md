import random
import re
from urllib.parse import quote

import requests

def search_naver(keyword):
    encoded_keyword = quote(keyword.encode('utf-8'))
    url = "https://openapi.naver.com/v1/search/local?query=%s" % encoded_keyword
    headers = {
        "X-Naver-Client-Id": "X9PSJVC7d6g9sqvZt41U",
        "X-Naver-Client-Secret": "zdDBiDYZFn"
    }
    res = requests.request("GET", url, headers=headers).json()['items']
    return res

result = search_naver('올리브영')
