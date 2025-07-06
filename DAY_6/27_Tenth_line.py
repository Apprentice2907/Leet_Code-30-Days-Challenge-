'''
Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:

Line 10
Note:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.'''



with open('file.txt') as f:
    for i, line in enumerate(f, start=1):
        if i == 10:
            print(line.strip())
            break


# with open('file.txt') as f:
#     lines = f.readlines()
#     if len(lines) >= 10:
#         print(lines[9].strip())



# from itertools import islice

# with open('file.txt') as f:
#     tenth_line = next(islice(f, 9, 10), None)
#     if tenth_line:
#         print(tenth_line.strip())



#  What if the file has less than 10 lines?
# with open('file.txt') as f:
#     lines = f.readlines()
#     if len(lines) >= 10:
#         print(lines[9].strip())
#     else:
#         print("File has less than 10 lines.")





# sed -n '10p' file.txt