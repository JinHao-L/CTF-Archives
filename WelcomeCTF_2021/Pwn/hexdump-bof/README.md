# hexdump-bof [465 pts]

**Category:** Pwn

**Solves:** 15

## Description
>I wrote an hexdump converter service with my friend. He said that it looked very vulnerable, and volunteered to fix it. Im not quite sure he did ..
> 
> Connect via `nc challs1.nusgreyhats.org 5002`
> 
> P.S. If you are new to pwn, checkout the hints"

**Hint**
* Try to make the program crash! Use gdb or other debuggers to see why it crashed
* If jumping to `win` doesnt work, its due to [this, extra reading!](https://stackoverflow.com/questions/54393105/libcs-system-when-the-stack-pointer-is-not-16-padded-causes-segmentation-faul) Try jumping to `win+5` instead :)

## Solution
*TODO*
### Flag

