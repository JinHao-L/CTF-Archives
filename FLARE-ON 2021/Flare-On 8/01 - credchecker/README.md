# 01 - credchecker [1 pts]

**Category:** Flare-On 8
**Solves:** None

## Description
>Welcome to Flare-On 8! This challenge surves as your tutorial mission for the epic quest you are about to emark upon. Reverse engineer the Javascript code to determine the correct username and password the web page is looking for and it will show you the flag. Enter that flag here to advance to the next stage. All flags will be in the format of valid email addresses and all end with "@flare-on.com".\r\n\r\n7-zip password: flare

**Hint**
* -

## Solution

This is a simple reversing challenge. By inspecting the html file, we find that there is a script file that handles the login credential checking. 

A simple reversing reveals the username and password: (you can use the inbuilt browser console)
```js
const username = 'Admin',
const password = btoa('goldenticket')
```

### Flag
> enter_the_funhouse@flare-on.com
