import base64
import hashlib
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES


def createMD5(s: str):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def ad(base64_text, key, iv):
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    decrypted_text = aes.decrypt(base64.b64decode(base64_text))
    padding_length = decrypted_text[-1]
    decrypted_text = decrypted_text[:-padding_length]
    return decrypted_text.decode('utf-8')


def ae(plain_text, key, iv):
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    pad_length = AES.block_size - (len(plain_text.encode('utf-8')) % AES.block_size)
    padded_text = plain_text.encode('utf-8') + bytes([pad_length]) * pad_length
    encrypted_text = aes.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode()


def aes_hex(plain_text):
    key = b'c24f74ca2820225badc01946dba4fdf7'
    iv = b'adc01946dba4fdf7'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    crypto = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return crypto.hex()


def sortDict(dictionary):
    sorted_items = sorted(dictionary.items())
    sorted_dict = {k: v for k, v in sorted_items}
    return sorted_dict


def mergeDict(dict1, dict2):
    merged_dict = dict2.copy()
    merged_dict.update(dict1)
    return merged_dict


class CreateObject(dict):
    def __init__(self, d):
        super().__init__(d)
        self._raw = d
        for key, value in d.items():
            if isinstance(value, dict):
                setattr(self, key, CreateObject(value))
            else:
                setattr(self, key, value)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key != "_raw":
            self._raw[key] = value

    def to_dict(self):
        result = {}
        for key, value in self.items():
            if isinstance(value, CreateObject):
                result[key] = value.to_dict()
            else:
                result[key] = value
        return result

    def __getattr__(self, UNUSED):
        return None


if __name__ == '__main__':
    pass
