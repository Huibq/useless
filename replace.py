import json
import os

key = os.environ['key']
iv = os.environ['iv']

User = input('请输入需要替换掉User:')
secrte_type = input('请选择写入文档:')
secrte_path = './utils/secret.json'
date = None
if secrte_type == '1':
    secrte_path = './utils/secret.json'
elif secrte_type == '2':
    secrte_path = './utils/secret2.json'
elif secrte_type == '3':
    secrte_path = './utils/secret3.json'
else:
    secrte_path = './utils/secret.json'

with open(secrte_path, "r", encoding='utf-8') as f:
    txt = json.load(f)
    txt[User] = txt[f"User_{len(txt)}"]
    txt.pop(f"User_{len(txt)}")
    with open(secrte_path, "w", encoding='utf-8') as F:
        json.dump(txt, F)
    print('替换完成！')
