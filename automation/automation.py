import re

# phone = 'phone_numbers.txt'
# reference: https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
# find all formats: 

# email = 'email.txt'
# reference: https://www.tutorialspoint.com/Extracting-email-addresses-using-regular-expressions-in-Python
# find top-level domains: .com, .net, .org, .gov

# Notes from discussion with Aaron I:
# split this into def find and def write
# fn to determine line data: return phone or email or none as string and put into array; iterate until number
# fn to format the specific data
# fn to write into the correct output file
# consider 28 without pulling all lines in at once; consider iterating each word/char (slice)

def find(in_filepath, regex, out_filepath):
    """ function takes in an input file path, regex, output path as strings;
        calls next function to write to the output file"""
    data_list = []
    with open(in_filepath,'r') as input_file:
        for line in input_file.readlines():
            data = re.findall(regex, line)
            data_list.append(data)
            # print(*data, sep = "\n")
            
        write(data_list, out_filepath)

def write(list, out_filepath):
    """ writes data found in find as single items on a line to 
        specified output file; prints length of data list to command line"""
        
    with open(out_filepath, 'w') as output_file:
        length = str(len(list))
        print(f'{out_filepath} is {length} records long \n')
        
        for item in list:
            for single in item:
                output_file.writelines(single)
                output_file.writelines('\n')
            

# def format_phone_nums(num):
#     num = re.sub(r'(?<!\S)(\d{3})-', r'(\1) ', num) 

# def format_output_file(filepath):
#     """ format output files (helper function that takes in a file path)
#         use for 'phone_numbers.txt' and 'email.txt' for this lab"""

    # parse out area codes starting with 0-1  

    # with open(file,r) as output_file:
    #     for line in output_file.readlines()
    #         first_char = line.slice(1)
#             sort by first char             
#             rewrite file in order
        
#         # return formatted file    
#         return output_file
        

if __name__ == "__main__":
    in_file = "../input/potential_contacts.txt"
    
    # see comments at top of doc for regex reference
    # email regex finds and writes to the output file!! Yippee!!   
    email_regex = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    output_file_email = "../output/emails.txt"
    find(in_file, email_regex, output_file_email)
    
    # phone regex finds and writes to the output file 
    
    # 7 digit numbers seem to be missing (??) and captures bad area codes
    phone_regex = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    
    output_file_phone = "../output/phone_numbers.txt"
    find(in_file, phone_regex, output_file_phone)
    
    
    # call format output document function

 
