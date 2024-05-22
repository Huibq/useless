import hashlib
import json
import time
import requests
from utils.util import aes_hex, push


def refresh_token(user='', token=''):
    ts = int(time.time() * 1000)
    p3 = aes_hex(json.dumps({'clienttime': ts // 1000, 'token': token}, separators=(',', ':'), ensure_ascii=False))
    data = {
        'p3': p3,
        'clienttime_ms': ts,
        't1': 0,
        't2': 0,
        'userid': user
    }
    params = {
        'dfid': '10xlnS11DjP02FXlMh10uVwZ',
        'appid': 3116,
        'mid': 252913861237135247806451300444659133777,
        'clientver': 10643,
        'clienttime': ts // 1000
    }
    params['signature'] = sign(params, json.dumps(data))
    login_url = 'http://login.user.kugou.com/v4/login_by_token'
    headers = {
        'User-Agent': 'Android810-1070-10643-46-0-NetMusic-wifi',
        'KG-THash': '255d751',
        'KG-Rec': '1',
        'KG-RC': '1',
    }
    response = requests.post(login_url, params=params, json=data, headers=headers)
    if response.json()['error_code'] != 0:
        push(user, 'KG刷新失败')
        return None
    print('成功')
    return response.json()['data']['token']


def sign(params, data=None):
    signkey = 'LnT6xpN3khm36zse0QzvmgTZ3waWdRSA'
    params = ''.join(sorted(f'{k}={v}' for k, v in params.items()))
    params = f'{signkey}{params}{data}{signkey}'
    return hashlib.md5(params.encode()).hexdigest()
