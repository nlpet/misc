import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

word = 'doge'
key_len = 32
doge = """

                  ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀

"""

def pad_key(key):
    diff = key_len - len(key)
    key = word * (diff // len(word)) + key
    return key.zfill(key_len).encode('utf-')

def encrypt(msg, key):
    key = pad_key(key)
    iv = os.urandom(16)
    msg = msg.encode('utf-8')

    cipher = Cipher(algorithms.AES(key), modes.OFB(iv))
    encryptor = cipher.encryptor()
    ct = iv + encryptor.update(msg) + encryptor.finalize()
    return base64.b64encode(ct).decode('utf-8')


def decrypt(ct, key):
    key = pad_key(key)
    ct = base64.b64decode(ct.encode('utf-8'))

    iv = ct[:16]
    cipher = Cipher(algorithms.AES(key), modes.OFB(iv))

    decryptor = cipher.decryptor()
    msg = decryptor.update(ct[16:]) + decryptor.finalize()

    try:
        return msg.decode('utf-8')
    except:
        return msg
