# what-a-concept
> It must be Thursday. I could never get the hang of Thursdays.





Arthur Dent (Hitch Hiker's Guide to The Galaxy)

![thrusday-concept-nadia-russian-doll](https://github.com/user-attachments/assets/6d314ca4-a137-49d3-a7c3-38861f6da8d0) ![friday-eve](https://github.com/user-attachments/assets/6722ff87-e23d-44cb-b132-6c18913114d9)

# usage
Here are some example usages to find out when BSM is. IKYK
```bash
$bash whenisbsm.sh september
"Datetime: Thursday, September 18, 2025 6:30Pm Location: TBD"
$
$bash whenisbsm.sh 08
DEBUG stupid user is using a number instead of string
INFO must convert stupidity
"Datetime: Thursday, August 21 , 2025 6:30Pm. Location: Partners Health, 399 Revolution Dr, Somerville, MA 02145"
$bash whenisbsm.sh 08 2025
DEBUG stupid user is using a number instead of string
INFO must convert stupidity
"Datetime: Thursday, August 21 , 2025 6:30Pm. Location: Partners Health, 399 Revolution Dr, Somerville, MA 02145"
$bash whenisbsm.sh 00007 2025
DEBUG stupid user is using a number instead of string
INFO must convert stupidity
"Datetime: Thursday, July 17, 2025 6:30Pm. Location: Wellington, 280 Congress St, Boston"
```

# TODO
- rust support
- ~pythonic support~
- ruby support
- c++ support
- bash script needs more robust year discovery format
- error reporting if someone is too dumb to specify a date that a record exists for BSM or other meetup
- NPM support
- interactive shell support with ncurses navigating interface.
- libFuse support to support navigating dates
- integrated support with meetup.com for registering
