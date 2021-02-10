# Automation with Python

## PR for this file: 

This is Lab 19 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 10 February 2021
____________________

### Challenge
Given a document `potential-contacts`, find and collect all email addresses and phone numbers.

_________

### Features and Implementation Details

1. Phone numbers may be in various formats.
(xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.

    - phone numbers with missing area code should presume 206

    - phone numbers should be stored in xxx-yyy-zzzz format

2. Once emails and phone numbers are found they should be stored in two separate documents.

3. The information should be sorted in ascending order.

4. Duplicate entries are not allowed.
__________

## Approach

Approach is using regex to find relevant data and a read/write approach similar to [CF 401 Madlib Lab](https://github.com/kimmyd70/madlib-cli)

_____________
## Required User Acceptance Testing

1. The `phone_numbers.txt` and `emails.txt` files will be verified by an automated system. So make sure to match the naming/formatting requirements exactly.

phone_numbers.txt

123-456-7890
206-678-9012
234-567-8901

emails.txt

ana@foo.bar
bill_x@foo.bar
chris.schmidt@bar.baz
_________________

