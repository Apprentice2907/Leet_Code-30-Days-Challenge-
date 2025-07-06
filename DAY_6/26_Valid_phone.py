'''
Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890
'''




# Python solution to validate phone numbers in a text file

def is_valid_phone_number(line):
    if len(line) == 12 and line[3] == '-' and line[7] == '-':
        return line.replace('-', '').isdigit()
    elif len(line) == 14 and line[0] == '(' and line[4] == ')' and line[5] == ' ' and line[9] == '-':
        srt = line[1:4]
        mid = line[6:9]
        end = line[10:]
        return srt.isdigit() and mid.isdigit() and end.isdigit()
    return False

with open('file.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if is_valid_phone_number(line):
            print(line)




# grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt
