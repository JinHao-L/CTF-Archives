import hashlib

def decryptFlag(msg, shared_secret):
    sha512 = hashlib.sha512()
    sha512.update(str(shared_secret).encode('ascii'))
    key = sha512.digest()[:len(msg)]
    return bytes([i[0] ^ i[1] for i in zip(key, msg)])

words = ['stethy', 'cherubimical', 'nontarnishing', 'achoke', 'bechirp']

key = " ".join(words)

cipher = open('encrypted_flag', 'rb').read()
print(key)
flag = decryptFlag(cipher, key)
print(flag)
# open('flag.txt', 'wb').write(flag)
