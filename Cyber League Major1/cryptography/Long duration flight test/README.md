# Long duration flight test [77 pts]

**Category:** cryptography
**Solves:** 27

## Description
>Your crew will be subjected to an endurance test to ensure you can survive the 1,400 light year trip via a 88-hour simulated flight. No one can intense such a long simulation without food and water. Yet, a SSH private key is given to you. If only you can decipher the message that is encrypted in DES and input the safe word. Pineapple juice? \xf0\x9f\x8d\x8d\r\n\r\nMessage:\r\n5ed0b9428aa782f5830fcbaf2731c7d95aeca05cd0ad789e282806d86d02c362abe4ed3d98b6ad39\r\n\r\nAuthor: Ng Bing Zhong

**Hint**
* -

## Solution
Use `John the Ripper` to decrypt the SSH key and use the password to decrypt the DES

### Flag
CYBERLEAGUE{y0u_4r3_my_BAbigiRL}
