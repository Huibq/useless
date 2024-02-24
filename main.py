import json
import os
from utils.util import ae
from utils.util import ad
from modules import tx
from utils.util import CreateObject

key = os.environ['key']
iv = os.environ['iv']
createObject = CreateObject

with open("./utils/secret.json", "r", encoding='utf-8') as f:
    txt = json.load(f)

tools = createObject(txt)
try:
    tools.User_1.qqmusic_key = ae(tx.refresh(str(ad(tools.User_1.loginuin, key, iv)), ad(tools.User_1.qqmusic_key, key, iv)), key, iv)
except Exception as e:
    print(e)
try:
    tools.User_2.qqmusic_key = ae(tx.refresh(str(ad(tools.User_2.loginuin, key, iv)), ad(tools.User_2.qqmusic_key, key, iv)), key, iv)
except Exception as e:
    print(e)
try:
    tools.User_3.qqmusic_key = ae(tx.refresh(str(ad(tools.User_3.loginuin, key, iv)), ad(tools.User_3.qqmusic_key, key, iv)), key, iv)
except Exception as e:
    print(e)
try:
    tools.User_4.qqmusic_key = ae(tx.refresh(str(ad(tools.User_4.loginuin, key, iv)), ad(tools.User_4.qqmusic_key, key, iv)), key, iv)
except Exception as e:
    print(e)
with open("./utils/secret.json", "w", encoding='utf-8') as f:
    json.dump(tools, f)


# print(ad(tools.User_4.loginuin, key, iv))
