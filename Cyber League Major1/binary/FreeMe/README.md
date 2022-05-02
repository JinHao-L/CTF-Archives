# FreeMe [183 pts]

**Category:** binary
**Solves:** 16

## Description
>Hoping to get a clearer look on his face, you approach the man and tap his shoulder. He shot up and burst into screams! "FILTHY PASSON!, DONT YOU TOUCH ME!!!" He shove you back to the ground and slowly sat down with his legs to his chest. As he slowly tuck his head, he mumbered "find the password.."\r\n\r\nAuthor: Ng Bing Zhong

**Hint**
* -

## Solution

### Part 1: Exploration
We are given with a single binary file `FreeAirpodGen` which asks for a password.Similar to FreeBie, this binary is compiled using python, so we have to use a python decompiler

### Part 2: Decompilation
Using 7z or `pyi-archive_viewer`, we can get the pyc files for the binary.

Here, I obtained the `FreeAirpodGen.pyc` file and `FreeAirpod.cpython-36m-x86_64-linux-gnu.so` shared object file. The magic bytes is broken here so I fixed it using a similar method to using `warnings.pyc`.

After fixing the pyc file, we can decompile the file to get the following source code:
``` py
import FreeAirpod
FreeAirpod.main()
```

### Part 3: Finding the flag
This means that we have to look for the `FreeAirpod` library. Luckily we already have the `FreeAirpod.cpython-36m-x86_64-linux-gnu.so` file. Decompiling it with IDA gave alot of gibberish which is difficult to reverse engineer.

Using `strings` and `grep`, I found that there is the `CYBERLEAGUE{` string in the so library.

![screenshot](./Screenshot%20from%202022-05-02%2020-10-28.png)

Decoding the `406972503064355f6675725f413131` using CyberChef gives `@irP0d5_fur_A11` which gives the flag.

### Flag
`CYBERLEAGUE{@irP0d5_fur_A11}`
