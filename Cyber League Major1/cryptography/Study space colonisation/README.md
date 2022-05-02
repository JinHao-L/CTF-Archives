# Study space colonisation [40 pts]

**Category:** cryptography
**Solves:** 39

## Description
>b"Apart from reaching the planet, populating the planet under our Motherlands flag is equally important. Your crew must lead 100 colonists to establish your states foothold before all others. Coordinates are given to you locked by an SSH key. Hmm.. what to do? whaaat toooo doooooo :)\r\n\r\nAuthor: Ng Bing Zhong\r\n\r\nAlternate Host: keeper@52.221.216.127:5002"

**Hint**
* -

## Solution
Using John the Ripper to crack the ssh private key, we can get the password `jessica`. Using it we can ssh into the server and get the flag

### Flag

