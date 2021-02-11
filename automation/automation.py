import re

# phone = 'phone_numbers.txt'
# reference: https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
# find all formats: 
# match within long text: \(?\b([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})\b
# allow leading 1s: ^(?:\+?1[-.●]?)?\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$
# allow 7-digit numbers: ^(?:\(?([0-9]{3})\)?[-.●]?)?([0-9]{3})[-.●]?([0-9]{4})$
# replace with format: \1●\2-\3

# email = 'email.txt'
# reference: https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-
# find top-level domains: .com, .net, .org, .gov
# reference: https://emailregex.com/
# find using solid inclusive (nothing 100%): r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# Notes from discussion with Aaron I:
# split this into def find and def write
# fn to determine line data: return phone or email or none as string and put into array; iterate until number
# fn to format the specific data
# fn to write into the correct output file
# consider 28 without pulling all lines in at once; consider iterating each word/char (slice)

def find(in_filepath, regex):
    """ find info 
    function that takes in an input file path and a regex as strings"""
    
    with open(in_filepath,'r') as input_file:
        for line in input_file.readlines():
            data = re.findall(regex, line)
            print(*data, sep = "\n")

# def write():
            # with open(out_filepath, 'w+') as output_file:
            #     for item in data:
            #         output_file.write(item)
            #         output_file.write('\n')

# def format_output_file(filepath):
#     """ format output files (helper function that takes in a file path)
#         use for 'phone_numbers.txt' and 'email.txt' for this lab"""
    
#     with open(file,r) as output_file:
#         for line in output_file.readlines()
#             read first char
#             sort by first char
#             rewrite file in order
        
#         # return formatted file    
#         return output_file
        
# # call formatting function
# # put business logic into main
# format_output_file(input_file)

if __name__ == "__main__":
    in_file = "../input/potential_contacts.txt"
    
    # see comments at top of doc    
    email_regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    output_file = "../output/emails.txt"
    # simple find digits regex
    test_regex = '\d+'
    find(in_file, test_regex)
        # call format output document function
        
    # # see comments at top of doc    
    # phone_regex1 = "\(?\b([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})\b"
    # phone_regex2 = "^(?:\+?1[-.●]?)?\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$"
    # phone_regex3 = "^(?:\(?([0-9]{3})\)?[-.●]?)?([0-9]{3})[-.●]?([0-9]{4})$"
    
    # with open("../output/phone_numbers.txt", 'w+') as out_file_phone:
    #     find_and_write(in_file, phone_regex1, out_file_phone)
    #     find_and_write(in_file, phone_regex2, out_file_phone)
    #     find_and_write(in_file, phone_regex3, out_file_phone)
    #     # call format output document function

 
