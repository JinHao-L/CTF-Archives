# Gates [50 pts]

**Category:** Reverse Engineering

**Solves:** 98

## Description
>Use the correct keys to enter the cool castle I copied from codepen.
> 
> http://challs1.nusgreyhats.org:5300/ 
> 
> (The flag consists of only ASCII characters)

## Solution

A typical web-based reverse engineering challenge. 
To view the `js` file, go to Inspector view (Dev tools), go to Sources tab and look for gate.js

This challenge features four gates that have to be cleared with 4 different keys.

Gates script for Gate4:

```py
import string
chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

rs = [2, 3, 4, 5]
target = [201, 129, 214, 102]
for i in range(4):
    r = rs[i]

    for c in chars:
        if ((((ord(c) << r) & 0xff) | (ord(c) >> (8 - r))) == target[i]): 
            print(c)
```


### Flag

