# KRANE [292 pts]

**Category:** Reverse Engineering
**Solves:** 35

## Description
> **Keep Reversing and Nobody Explodes**
> 
> Bomb defusing, but theres no manual...? Can you still do it?
> 
> [challs1.nusgreyhats.org:5302](http://challs1.nusgreyhats.org:5302)

**Hint**
* \-

## Solution
Topic: Web assembly (WASM) reverse engineering

For this challenge, you play the role of the bomb defusal guy and you have to defuse the bomb by cutting the wire, pressing a specific sequence of alphabets and pushing the red button at a specific time. There is a serial number at the side of the bomb which should probably hint at the defusing method. (Similar game to [Keep Talking and Nobody Explodes](https://keeptalkinggame.com/))

We managed to decompile the wasm file (see `main.dec`) and locate the functions that are responsible for the main game logic.
* `ca` function is called when the alphabets are pressed
* `cb` function is called when the red button is pushed
* `cc` function is called when any of the wires is cut
* Lastly, `check` function is called after any of the 3 operations and it checks if the bomb explodes. 

That's as far as I got and I did not manage to get any further info from the decompiled file (too many variables to follow)

However, I did manage to get the flag in another way: by trial and error

There are a few observations that are made:
1. Only one wire can be cut (always fail when a 2nd wire is cut)
2. Red button can be pushed anytime and most of the time it should pass (didnt figure out the logic behind it)
3. All 4 alphabets should be pressed in a specific order

With these observations, I began my spree of random spamming and managed to get my flag within the hour.

See [creator's writeup](https://github.com/NUSGreyhats/welcome-ctf-2021/blob/main/Challenges/Reverse/keep_reversing_and_nobody_explodes/challenge.md)

### Flag
`greyhats{Wh0_n33D5_a_p4rTnER}`
