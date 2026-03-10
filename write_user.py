import json
import os
from utils.util import ae

KEY = os.getenv("key")
IV = os.getenv("iv")
if not KEY or not IV:
    raise RuntimeError("缺少环境变量 key 或 iv")

FILES = {
    "1": "./utils/secret.json",
    "2": "./utils/secret2.json",
    "3": "./utils/secret3.json"
}


def load(path):
    if not os.path.exists(path):
        return {}
    try:
        return json.load(open(path, "r", encoding="utf-8"))
    except:
        return {}


def next_user(data):
    if not data:
        return "User_1"
    return f"User_{max(int(k.split('_')[1]) for k in data)+1}"


uin = input("请输入uin: ").strip()
enc_uin = ae(uin, KEY, IV)

all_uin = []
for p in FILES.values():
    all_uin += [v["loginuin"] for v in load(p).values()]

if enc_uin in all_uin:
    print(f"已存在：{enc_uin}")
    exit()

qqmusickey = input("请输入qqmusickey: ").strip()
t = input("请选择写入文档(1/2/3): ").strip()

path = FILES.get(t, FILES["1"])
date = input("请输入日期: ").strip() if t in ("2", "3") else None

data = load(path)
user = next_user(data)

data[user] = {
    "qqmusic_key": ae(qqmusickey, KEY, IV),
    "loginuin": enc_uin,
    "tab": date or "qq"
}

json.dump(data, open(path, "w", encoding="utf-8"))

print(user)
print("写入完成！")
