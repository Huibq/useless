import json
import os
from utils.util import ae, ad

key = os.environ['key']
iv = os.environ['iv']
while True:
    User = input('请输入需要替换掉uin:')
    if User == 'exit':
        break
    en_User = ae(User, key, iv)

    secrte_data = ['./utils/secret.json', './utils/secret2.json', './utils/secret3.json']
    for secrte_path in secrte_data:
        with open(secrte_path, "r", encoding='utf-8') as f:
            txt = json.load(f)
            Type = False
            for i in txt:
                if txt[i]['loginuin'] == en_User:
                    Type = True
                    if secrte_path == './utils/secret2.json' or secrte_path == './utils/secret3':
                        Continue = input('是否继续替换，1是2否:')
                        if Continue == '2':
                            break
                    txt[i] = txt[f"User_{len(txt)}"]
                    txt.pop(f"User_{len(txt)}")
                    with open(secrte_path, "w", encoding='utf-8') as F:
                        json.dump(txt, F)
                    print('替换完成！')
                    print('替换路径：{}'.format(secrte_path))
                    break
            if Type:
                Type = False
                break

