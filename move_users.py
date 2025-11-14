import json, os
from utils.util import ad

key = os.environ['key']
iv = os.environ['iv']

remain_users = []  # 保留的uin
remove_users = []
old_home_path = "./utils/secret3.json"
new_home_path = "./utils/secret.json"

with open(old_home_path, "r", encoding='utf-8') as f:
    txt = json.load(f)

cache_txt = txt.copy()  # 使用复制避免在循环时改变字典导致出错

for user in cache_txt:
    uin = int(ad(txt[user]['loginuin'], key, iv))
    if uin not in remain_users:
        remove_users.append(txt[user])  # 中转列表
        txt.pop(user)  # 移除不需要的

new_txt = {}  # 中转字典
for new_user in txt:
    user_name = 'User_{}'.format(len(new_txt) + 1)
    new_txt[user_name] = txt[new_user]  # 保留的

with open(old_home_path, "w", encoding='utf-8') as f:
    json.dump(new_txt, f)  # 保存

with open(new_home_path, "r", encoding='utf-8') as f:
    home = json.load(f)

for user in remove_users:
    user_name = 'User_{}'.format(len(home) + 1)
    home[user_name] = user  # 将移除的加入目的地

with open(new_home_path, "w", encoding='utf-8') as f:
    json.dump(home, f)
