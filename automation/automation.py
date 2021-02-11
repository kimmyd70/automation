import re

# phone = 'phone_numbers.txt'
# reference: https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
# find all formats: 
# match within long text: \(?\b([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})\b
# allow leading 1s: ^(?:\+?1[-.●]?)?\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$
# allow 7-digit numbers: ^(?:\(?([0-9]{3})\)?[-.●]?)?([0-9]{3})[-.●]?([0-9]{4})$
# replace with format: \1●\2-\3

# email = 'email.txt'
# reference: https://emailregex.com/
# find using: r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"




# find and output info

with open('potential-contacts.txt',r) as full_file:
    line = full_file.readlines()
    while not EOF
        if line contains (regex phone):
            formatted_number = correct format to xxx-xxx-xxxx with re.sub(\1●\2-\3)
            with open("phone_numbers.txt", 'a') as phone: 
                phone.write(formatted_number) 

        elif line contains (regex email):
            formatted_email = data found (no sub needed)
            with open("email.txt", 'a') as email: 
                email.write(formatted_email) 

        else
            next line
                
    # format output files (helper function that takes in a file path)
    while not EOF:
        read 'phone_numbers.txt' line
        sort by first char
        rewrite file in order
        
        read 'email.txt' line
        sort by first char
        rewrite file in order
