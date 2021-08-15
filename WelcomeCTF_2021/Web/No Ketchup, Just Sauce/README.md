# No Ketchup, Just Sauce [120 pts]

**Category:** Web

**Solves:** 47

## Description
> Building my ketchup startup at http://challs1.nusgreyhats.org:5208/

**Hint**
* What did the developer leave behind in the source code? Could it be something that you can access?

## Solution
Category: Web exploration

The first step is to explore the webpage. So one of my friend found that the robots.txt file is available at http://challs1.nusgreyhats.org:5208/robots.txt

The `robots.txt` hinted at the existence of the `reborn.php` file

Followed this lead, we visited http://challs1.nusgreyhats.org:5208/reborn.php, which shows a single input form, labeled What is your favourite ketchup?

Using the inspector, We found a comment left by the challenge creator:

> \<!-- Version 2.2.3. Backup file contains version 2.2.2. -->

This hints at the possibility of a backup file?

We then tried multiple possible routes based on the idea of web file backup and found http://challs1.nusgreyhats.org:5208/reborn.php.bak. 
This downloaded the version 2.2.3 backup file: `reborn.php.bak`.

Found the secret code: `no ketchup, raw sauce -- too many calories, not good` and submit to obtain flag

### Flag
`greyhats{n0_k3tchup_r4w_s4uc3_892e89h89e}`