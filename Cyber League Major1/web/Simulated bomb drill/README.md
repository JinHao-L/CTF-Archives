# Simulated bomb drill [82 pts]

**Category:** web
**Solves:** 24

## Description
>b"You know whats worse than a bomb? FAILURE TO CONTAIN ONE! Youre going to contain and eliminate any bomb, explosive or the tiniest spark in under a minute.\r\n\r\nAuthor: Hades95200"

**Hint**
* You need to defuse the bomb.\n\nCHECK OUT /defuse

## Solution
`/` -> gives u a `princesspeach` cookie that is a base64 encoded current UTC timestamp
`/decode` -> checks the cookie and displays an image

### Idea
Apparently u have to visit the decode page before ur cookie expires, this means that u have to visit `/decode` with the current timestamp (prob +- a few milliseconds leeway)

### Exploit
We shd build a script to send a GET request to `/decode` with the curr timestamp (see `exploit.py`)

### Flag
I forgot
