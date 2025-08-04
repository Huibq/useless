import re as _re
from hashlib import md5, sha1
import base64
from Crypto.Cipher import AES

zzc_headMap = [23, 14, 6, 36, 16, 7, 19]
zzc_middleMap = [89,  39, 179, 150, 218,  82, 58, 252, 177,  52, 186, 123, 120,  64, 242, 133, 143, 161, 121, 179]
zzc_tailMap = [16,  1, 32, 12, 19, 27,  8,  5]


def createMD5(s: str):
    return md5(s.encode("utf-8")).hexdigest()


def v(b):
    res = []
    p = [21, 4, 9, 26, 16, 20, 27, 30]
    for x in p:
        res.append(b[x])
    return ''.join(res)


def c(b):
    res = []
    p = [18, 11, 3, 2, 1, 7, 6, 25]
    for x in p:
        res.append(b[x])
    return ''.join(res)


def y(a, b, c):
    e = []
    r25 = a >> 2
    if b is not None and c is not None:
        r26 = a & 3
        r26_2 = r26 << 4
        r26_3 = b >> 4
        r26_4 = r26_2 | r26_3
        r27 = b & 15
        r27_2 = r27 << 2
        r27_3 = r27_2 | (c >> 6)
        r28 = c & 63
        e.append(r25)
        e.append(r26_4)
        e.append(r27_3)
        e.append(r28)
    else:
        r10 = a >> 2
        r11 = a & 3
        r11_2 = r11 << 4
        e.append(r10)
        e.append(r11_2)
    return e


def n(ls):
    e = []
    for i in range(0, len(ls), 3):
        if i < len(ls) - 2:
            e += y(ls[i], ls[i + 1], ls[i + 2])
        else:
            e += y(ls[i], None, None)
    res = []
    b64all = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    for i in e:
        res.append(b64all[i])
    return ''.join(res)


def t(b):
    zd = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    ol = [212, 45, 80, 68, 195, 163, 163, 203, 157, 220, 254, 91, 204, 79, 104, 6]
    res = []
    j = 0
    for i in range(0, len(b), 2):
        one = zd[b[i]]
        two = zd[b[i + 1]]
        r = one * 16 ^ two
        res.append(r ^ ol[j])
        j += 1
    return res


def sign(params):
    md5Str = createMD5(params).upper()
    h = v(md5Str)
    e = c(md5Str)
    ls = t(md5Str)
    m = n(ls)
    res = 'zzb' + h + m + e
    res = res.lower()
    r = _re.compile(r'[\\/+]')
    res = _re.sub(r, '', res)
    return res


def sign_zzc(data):
    hexsha1 = sha1(data.encode()).hexdigest()
    middle = []
    for i in range(0, 20):
        middle.append(int(hexsha1[2 * i] + hexsha1[2 * i + 1], 16))
    middle = list(map(lambda x, y: x ^ y, middle, zzc_middleMap))
    _sign = base64.b64encode(bytearray(middle))
    _sign = _re.sub(r'[+/=]', '', _sign.decode())
    _sign = 'zzc' + ''.join(hexsha1[x] for x in zzc_headMap) + _sign + ''.join(hexsha1[x] for x in zzc_tailMap)
    return _sign.lower()


def aes_decrypt(base64_text, key, iv):
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    decrypted_text = aes.decrypt(base64.b64decode(base64_text))
    padding_length = decrypted_text[-1]
    decrypted_text = decrypted_text[:-padding_length]
    return decrypted_text.decode('utf-8')
