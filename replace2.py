import json
import os

key = os.environ['key']
iv = os.environ['iv']

while True:
    User = input('请输入需要替换掉User:')
    if User == 'exit':
        break
    secrte_path = './utils/secret.json'
    date = None
    with open(secrte_path, "r", encoding='utf-8') as f:
        txt = json.load(f)
        txt[User] = txt[f"User_{len(txt)}"]
        txt.pop(f"User_{len(txt)}")
        with open(secrte_path, "w", encoding='utf-8') as F:
            json.dump(txt, F)
        print('替换完成！')
