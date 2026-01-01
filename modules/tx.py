from utils.Http import signRequest
from utils.util import push


def refresh(loginuin, qqmusic_key):
    if qqmusic_key.startswith('W_X'):
        options = {
            'method': 'POST',
            'body': {
                "comm": {
                    "fPersonality": "0",
                    "tmeLoginType": "1",
                    "tmeLoginMethod": "1",
                    "qq": "",
                    "authst": "",
                    "ct": "11",
                    "cv": "12080008",
                    "v": "12080008",
                    "tmeAppID": "qqmusic"
                },
                "req1": {
                    "module": "music.login.LoginServer",
                    "method": "Login",
                    "param": {
                        "code": "",
                        "openid": "",
                        "refresh_token": "",
                        "str_musicid": loginuin,
                        "musickey": qqmusic_key,
                        "unionid": "",
                        "refresh_key": "",
                        "loginMode": 2
                    }
                }
            }
        }
        req = signRequest(options["body"])
        # print(req.text)
        body = req.json()
        if body['req1']['code'] != 0:
            print('失败, code: ' +
                  str(body['req1']['code']) + f'\n响应体: {body}')
            push(loginuin, '企鹅刷新失败')
            return None
        else:
            print('成功')
            qqmusic_key = body['req1']['data']['musickey']
            return qqmusic_key
    elif qqmusic_key.startswith('Q_H_L'):
        options = {
            'method': 'POST',
            'body': {
                'req1': {
                    'module': 'QQConnectLogin.LoginServer',
                    'method': 'QQLogin',
                    'param': {
                        'expired_in': 7776000,
                        'musicid': int(loginuin),
                        'musickey': qqmusic_key
                    }
                }
            }
        }
        req = signRequest(options['body'])
        # print(req.text)
        body = req.json()
        if body['req1']['code'] != 0:
            print('失败, code: ' +
                  str(body['req1']['code']) + f'\n响应体: {body}')
            push(loginuin, '企鹅刷新失败')
            return None
        else:
            print('成功')
            qqmusic_key = body['req1']['data']['musickey']
            return qqmusic_key
    else:
        print('未知的key格式')
        return None
