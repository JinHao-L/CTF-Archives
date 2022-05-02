import hashlib
from itertools import combinations

txs = [
    # put the attack transactions your found here
    '0x11f99f2239476ec65208bac539161c1f4d1176dfce613e2707aecdca8b722114',
    '0xa856ccf5933272778b795fa276ea44f262a4ae283f925331ab2e3eb2803dd43b',
    '0x99a5722bb73a73c6b47967f9b457e888d6503b0f9e1bf23fbf36de56ebad1522',
    '0xe42797c03261a22e6eadef6f0b33c11c46469a2fa6e4010a445f9fb721db2d3c',
    '0x2cdeac1f50db9532b85af2526fa0285fba81177454509a682c53c3ba00a98513',
    '0x0000000000000000000000000000000000000000000000000000000000000002',
    '0x0000000000000000000000000000000000000000000000000000000000000000',
    '0x0000000000000000000000000000000000000000000000000000000000000001',
    '0x0000000000000000000000000000000000000000000000000000000000000002',
    '0x0000000000000000000000000000000000000000000000000000000000000000',
    '0x0000000000000000000000000000000000000000000000000000000000000001',
    '0x0000000000000000000000000000000000000000000000000000000000000002',
    '0x0000000000000000000000000000000000000000000000000000000000000000',
    '0x0000000000000000000000000000000000000000000000000000000000000001',
    '0x0000000000000000000000000000000000000000000000000000000000000002',
    '0x0000000000000000000000000000000000000000000000000000000000000000',
    '0x0000000000000000000000000000000000000000000000000000000000000001',
    '0x0000000000000000000000000000000000000000000000000000000000000002',
    '0x0000000000000000000000000000000000000000000000000000000000000001',
    '0x0000000000000000000000000000000000000000000000000000000000000002',
    '0x0000000000000000000000000000000000000000000000000000000000000001',
    '0x0000000000000000000000000000000000000000000000000000000000000002',
]

assert len(comb) == 22
salt = b'hint: find abnormal transactions'
m = hashlib.sha256()
for tx_hash in sorted(comb):
    assert len(tx_hash) != 66 or tx_hash[:2] != '0x'
    m.update(salt + tx_hash.encode() + m.digest())

assert m.hexdigest()[:16] == 'bf22a2d63563554c'
print('flag{' + m.hexdigest() + '}')
