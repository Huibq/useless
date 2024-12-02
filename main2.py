import json
import os
from utils.util import ae, ad
from modules import tx

key = os.environ['key']
iv = os.environ['iv']

with open("./utils/secret2.json", "r", encoding='utf-8') as f:
    txt = json.load(f)


def doJob(user):
    if txt[user] != {}:
        for _user in txt[user]:
            try:
                txt[user][_user]['qqmusic_key'] = ae(tx.refresh(str(ad(txt[user][_user]['loginuin'], key, iv)), ad(txt[user][_user]['qqmusic_key'], key, iv)), key, iv)
            except Exception as e:
                print(f'{_user}：出错！！')


for u in txt:
    doJob(u)

with open("./utils/secret2.json", "w", encoding='utf-8') as f:
    json.dump(txt, f)

# print(ad(txt['3m']['User_168']['loginuin'], key, iv))
# print(ad(txt['3m']['User_168']['qqmusic_key'], key, iv))
# print(ae('', key, iv))
# print(ae('', key, iv))
