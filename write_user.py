import json
import os
from utils.util import ae

key = os.environ['key']
iv = os.environ['iv']

uin = input('请输入uin:')

all_user = []
for i in range(3):
    Path = f'./utils/secret.json' if i == 0 else f'./utils/secret{i + 1}.json'
    with open(Path, "r", encoding='utf-8') as f:
        users = json.load(f)
        for user in users:
            all_user.append(users[user]['loginuin'])

enc_uin = ae(uin, key, iv)

if enc_uin in all_user:
    print(f"已存在：{enc_uin}")
else:
    qqmusickey = input('请输入qqmusickey:')
    secrte_type = input('请选择写入文档:')
    secrte_path = './utils/secret.json'
    date = None
    if secrte_type == '1':
        secrte_path = './utils/secret.json'
    elif secrte_type == '2':
        secrte_path = './utils/secret2.json'
        date = input('请输入日期:')
    elif secrte_type == '3':
        secrte_path = './utils/secret3.json'
        date = input('请输入日期:')
    else:
        secrte_path = './utils/secret.json'

    with open(secrte_path, "r", encoding='utf-8') as f:
        txt = json.load(f)

        enc_qqmusickey = ae(qqmusickey, key, iv)

        user_name = 'User_{}'.format(len(txt) + 1)

        print(user_name)

        txt[user_name] = {
                "qqmusic_key": enc_qqmusickey,
                "loginuin": enc_uin,
                "tab": "qq" if date is None else date
            }

        with open(secrte_path, "w", encoding='utf-8') as f:
            json.dump(txt, f)

        print('写入完成！')
