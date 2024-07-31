import json
import os
from utils.util import ae, ad, push
from modules import tx
from modules import kg

key = os.environ['key']
iv = os.environ['iv']

with open("./utils/secret.json", "r", encoding='utf-8') as f:
    txt = json.load(f)


def doJob(user):
    if txt[user]['tab'] == 'qq':
        try:
            txt[user]['qqmusic_key'] = ae(tx.refresh(str(ad(txt[user]['loginuin'], key, iv)), ad(txt[user]['qqmusic_key'], key, iv)), key, iv)
        except Exception as e:
            print('出错！！')
    else:
        try:
            txt[user]['qqmusic_key'] = ae(kg.refresh_token(str(ad(txt[user]['loginuin'], key, iv)), ad(txt[user]['qqmusic_key'], key, iv)), key, iv)
        except Exception as e:
            print('出错！！')


for u in txt:
    doJob(u)

with open("./utils/secret.json", "w", encoding='utf-8') as f:
    json.dump(txt, f)

# print(ad(txt['User_4']['loginuin'], key, iv))
# print(ad(txt['User_4']['qqmusic_key'], key, iv))
# print(ae('', key, iv))
# print(ae('', key, iv))
# print(tx.refresh('', ''))
