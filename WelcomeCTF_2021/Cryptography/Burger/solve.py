from pwn import *
import hashlib
from string import printable

SERVER = "challs1.nusgreyhats.org"
PORT = 5210

FLAG = b'0'*56

block = 16

def getOutput():
    p.recvuntil(b' :\n')
    target = p.recvuntil(b'\n')
    target = target.lstrip().rstrip()
    p.recvuntil(b' :')
    return target

def toChunks(hashes):
    chunks = [hashes[i:i+(block * 2)].decode("utf-8") for i in range(0, len(hashes), (block * 2))]
    print('\n'.join(chunks))
    return chunks

def solve(targetHash, knownPrefix):
    text = knownPrefix
    # padding
    text += b'\0' * (block - ((len(text) + 1) % block))
    for x in range(256):
        guess = bytes(chr(x), 'utf-8') + text
        guessHash = ''

        for i in range(0, len(guess), block):
            sha512 = hashlib.sha512()
            sha512.update(guess[i:i + block])
            guessHash += sha512.hexdigest()[:block * 2]

        # print(guess[0:block], guess[block:])
        if guessHash == targetHash:
            print("\nFound:",guess)
            return bytes(chr(x), 'utf-8')
    return None

binary = None
p = process(binary) if binary else remote(SERVER, PORT)

p.recvuntil(b' :')
p.sendline(b'')

flagHash = getOutput()
print(f'Hashed Flag :')
flagChunks = toChunks(flagHash)

known = b''
for i in range(18, 130, 2):
    p.sendline(b'0'*i)
    hashes = getOutput()
    print(f'Part{i} :')
    chunks = toChunks(hashes)

    offset = -1 - ((len(known) + 1) // block)

    lastByte = solve(''.join(chunks[offset:]), known)
    print(lastByte)
    known = lastByte + known

p.interactive()
