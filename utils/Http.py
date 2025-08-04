import json
import requests
from modules.qqsign import sign_zzc

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}
session.headers.update(headers)


def signRequest(data):
    data = json.dumps(data)
    s = sign_zzc(data)
    return session.post('https://u6.y.qq.com/cgi-bin/musics.fcg?format=json&sign=' + s, data=data, headers=headers)
