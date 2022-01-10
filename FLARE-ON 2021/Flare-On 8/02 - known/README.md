# 02 - known [1 pts]

**Category:** Flare-On 8
**Solves:** None

## Description
>We need your help with a ransomware infection that tied up some of our critical files. Good luck.\r\n\r\n7-zip password: flare

**Hint**
* -

## Solution

Using IDA to decompile the .exe file and following the input variable, we find the suspicious function that handles the logic of the decryption software.

The decryption logic of the decryption program is as follow:
``` python
for i in range(0, 8):
    result[i] = rotl(input[i] ^ cipher[i], i) - i;
```
* `result` here is your decrypted output and lets assume that it is our desired plaintext
* `rotl` here is binary rotate left
* `cipher` here is your encrypted data
* `input` here is our input and lets assume that it is the secret decryption key
* Another thing we can learn is that the key is of length 8

By analysing the names of the encrypted file, we can determine/guess a few things:
* `.gif`, `.png`, `.jpg` files start with some magic numbers
* `latin_alphabet.txt.encrypted` correspond to encrypted alphabets in alphabetical order

We can now craft our exploit by reversing the decryption. The high level idea is to add, rotate right then xor:
``` python
# Key idea of decryption reversal:
for i in range(0, 8):
    key[i] = rotr(plain[i] + i, i) ^ cipher[i]
```

Exploit script in (./crack.py)[./crack.py]

### Flag
> You_Have_Awakened_Me_Too_Soon_EXE@flare-on.com
