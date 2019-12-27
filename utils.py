import binascii
from hashlib import pbkdf2_hmac, md5


def tampared(a,split):
    if len(a) > 2:
        print(a.split(split)[0], split, a.split(split))
        x = pbkdf2_hmac('sha256', str(a.split(split)[0]).encode(),
                        md5(str(a.split(split)[0]).encode()).hexdigest().encode(),
                        iterations=100000)
        print(binascii.hexlify(x).decode())
        return binascii.hexlify(x).decode() != a.split(split)[1]