import json
import os
from utils.util import ae, ad
from modules import tx

key = os.environ['key']
iv = os.environ['iv']

with open("./utils/secret2.json", "r", encoding='utf-8') as f:
    txt = json.load(f)


def doJob(user):
    try:
        txt[user]['qqmusic_key'] = ae(tx.refresh(str(ad(txt[user]['loginuin'], key, iv)), ad(txt[user]['qqmusic_key'], key, iv)), key, iv)
    except Exception as e:
        print(f'{user}：出错！！')


for u in txt:
    doJob(u)

with open("./utils/secret2.json", "w", encoding='utf-8') as f:
    json.dump(txt, f)

# print(ad(txt['User_186']['loginuin'], key, iv))
# print(ad(txt['User_186']['qqmusic_key'], key, iv))
# print(ae('', key, iv))
# print(ae('', key, iv))
