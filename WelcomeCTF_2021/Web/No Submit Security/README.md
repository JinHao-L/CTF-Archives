# No Submit Security [50 pts]

**Category:** Web

**Solves:** 85

## Description
>I heard that my website is leaking some secret when a button is clicked, so I removed that button. I think it should be secure enough now.
> 
> http://challs1.nusgreyhats.org:5217/

## Solution
Category: Web, HTML

Inspecting the source code reveals a form with multiple hidden fields, these fields have seemingly random names and values.

Something seems missing? The submit button is not found in the form.

By manually adding the button into the form, we can submit the seemingly randoms input to index.php

``
<input type='submit' name='Submit'/>
``

### Flag

`greyhats{5U8m1551O5_15_FRoM_tH3_CL13Nt_51d3}`