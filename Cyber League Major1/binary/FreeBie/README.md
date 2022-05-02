# FreeBie [77 pts]

**Category:** binary
**Solves:** 27

## Description
>During your training, you found a fellow spaceman-in-training. Hiding in a dark corner, he seem to be alive yet aloof. Hugging his knee close to the chest with his head tuck down, he mumbled "find the password... find the pass.. find th pass.. fithpass.."\r\n\r\nAuthor: Bing Zhong

**Hint**
* -

## Solution

### Part 1: Exploration
We are given with a single binary file `FreeAirpodGen_test` which asks for a password.
My first thought is to decompile the binary using IDA. However, I ended up with alot of gibberish code with various python modules import. Appparently this is compiled using python, so we have to use a python decompiler

### Part 2: Decompilation
After various googling, I find that I can decompile the code using python using 7z or `pyi-archive_viewer` to get the pyc files.

I obtained the `FreeAirpodGen_test.pyc` file and tried decompiling it using `uncompyle6`. However, apparently the magic byte is wrong. Using a random library pyc file in the archive (`warnings.pyc`), I compared the magic bytes and use it to fix the target file.

After fixing, we can decompile the file to get the source code. We then get a sha256 string that contains the flag. Using dcodr, I managed to decrypt the hash and get the flag.

### Flag
CYBERLEAGUE{WHAT_d03s_tequiero_meeeN}
