import json
import requests
from modules.qqsign import sign


def signRequest(data):
    data = json.dumps(data)
    s = sign(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
    }
    return requests.post('https://u.y.qq.com/cgi-bin/musics.fcg?format=json&sign=' + s, data=data, headers=headers)
