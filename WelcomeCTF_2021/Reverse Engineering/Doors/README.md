# Doors [50 pts]

**Category:** Reverse Engineering

**Solves:** 81

## Description
>Find the keys to unlock all doors. Python is easier to write but is it also easier to read?
> 
> `nc challs1.nusgreyhats.org 5301`

**Hint**
* \-

## Solution

For this challenge, there are 4 parts (doors) with each doors requiring a specific passcode. The file `doors.py` provides the source code for the 4 parts.

### Part 1
* The last 3 hex value of the key is `0x246` (from key mask 0xfff)
* The first 3 hex value of key is `0x942` (bitwise shift of key) 
* The hex 0x942246 => 9708102 (decimal)
* Part 1 passcode: **9708102**

### Part 2
* Math-based
* Last 3 digit: Cube root 78402752 = 428
* First 3 digit: 189 ^ 861 = 992
* Part 2 passcode: **992428**

### Part 3
* Reverse-engineer math operation
* Follow from 2478123 to key
* Part 3 passcode: **2187324**

### Part 4
* Passcode is of length 6
* Hash of each digit with specific string have to match `hhs`

Although MD5 is insecure, it is easier to bruteforce the solution since we know the passcode is a 6-value digits. 

So search space is 10^6 which is computationally possible

Brute force produces:
* Part 4 passcode: **612381**

### Flag
`greyhats{0p3n_th3m_w17h_c0d3}`
