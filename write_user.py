import json
import os
from utils.util import ae

key = os.environ['key']
iv = os.environ['iv']

uin = input('请输入uin:')
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

enc_uin = ae(uin, key, iv)

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
