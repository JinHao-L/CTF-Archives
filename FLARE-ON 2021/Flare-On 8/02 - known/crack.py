#!/usr/bin/python3

def bytes_from_file(filename, chunksize=8):
    with open(filename, "rb") as f:
        chunk = f.read(chunksize)
        return chunk


def rotl(num, rotations, bits=8):
    for i in range(0, rotations):
        bit = num & (1 << (bits-1))
        num <<= 1
        if(bit):
            num |= 1
        num &= (2**bits-1)

    return num


def rotr(num, rotations, bits=8):
    for i in range(0, rotations):
        num &= (2**bits-1)
        bit = num & 1
        num >>= 1
        if(bit):
            num |= (1 << (bits-1))

    return num


def solve(filename, possiblePlain):
    print('Analyse', filename)
    for pt in possiblePlain:
        n = len(pt)
        key = [0] * n
        cipher = bytes_from_file("Files/" + filename, 8)
        for i in range(0, n):
            key[i] = rotr(pt[i] + i, i) ^ cipher[i]
            print("plain:", chr(rotl(key[i] ^ cipher[i], i) - i))

        print(key)
        try:
            keyStr = ''.join([chr(x) for x in key])
            print(keyStr)
        except Exception as e:
            # ignore
            print(e)
            continue


solve('latin_alphabet.txt.encrypted', [b'ABCDEFGH'])
solve('capa.png.encrypted',
      [b'\x89\x50\x4E\x47\x0d\x0a\x1a\x0a'])
solve('commandovm.gif.encrypted',
      [b'\x47\x49\x46\x38\x37\x61',
       b'\x47\x49\x46\x38\x39\x61'])
# solve('flarevm.jpg.encrypted',
#      [b'\xFF\xD8\xFF\xDB\xFF\xD8\xFF\xE0'])
