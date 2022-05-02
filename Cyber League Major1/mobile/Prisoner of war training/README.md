# Prisoner of war training [283 pts]

**Category:** mobile
**Solves:** 14

## Description
>As a soldier from the Motherland, being captured only makes you a laughing stock. This will train you to capture enemies, and guide you on how your hostages should be treated according to the law of the Motherland. All enemies are equipped with a bodycam APK. You will learn to decompile and locate sensitive information. "I spy with my little eye".\r\n\r\nAuthor: Wang Qing

**Hint**
* -

## Solution
### Part 1: Exploration
Running the apk with an emulator gives a simple app that produces a fake flag when u press the button: `CYBERLEAGUE{HAHAH_I_Got_You}`

Lets use `jadx` to decompile apk and read the source code. After reading the code, we realise that there are 5 inputs that are used to form the flag (using some "uncessarily complicated" encryption method)

Let's backtrace to find where the string are declared. We find that the Strings are defined in `R.String`, but these are not strings but rather integers. These integers seems to be addresses.

Furthermore, there are some suspicious strings that are not used anywhere (eg. `decrypt_me`, `app_name`, `gajjae` and `majayo`).

By looking further we find that the actual value of these strings are located in `res/values/strings`

### Part 2: Exploit
Let's create a Java file and use the exact same code used in the source code. We organize the strings and identify them based on their content type. (ie. `gajjae` and `majayo` are possible ciphertext and can replace `ani`)

``` js
ani -> CYBERLEAGUE{HAHAH_I_Got_You} // definitely fake
gajjae -> CYBERLEAGUE{BTS_FAKE_LOVE} // prob fake
majayo -> CYBERLEAGUE{PLs_Protect_Urselves_UAT_Pass} // flag
```

### Flag
`CYBERLEAGUE{PLs_Protect_Urselves_UAT_Pass}`
