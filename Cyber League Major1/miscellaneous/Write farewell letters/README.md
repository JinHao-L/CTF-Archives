# Write farewell letters [25 pts]

**Category:** miscellaneous
**Solves:** 51

## Description
>Say goodbye (or good riddance) to everyone you know and love. \r\n\r\nNote: Compatible with all galaxy devices.\r\n\r\nAuthor: Hakkasuru

**Hint**
* -

## Solution
Run the program and find the location of the yoda picture.

We find that it is located in a `tmp` folder inside a `app.asar` file. This `asar` file seems to be a archive file for electron apps.

With some googling we can extract the asar file and find the flag in the `index.js` file

```
npx asar extract app.asar destfolder 
```


### Flag
`CYBERLEAGUE{7h3_cu73n355_15_5720n9_w17h_7h15_0n3}`
