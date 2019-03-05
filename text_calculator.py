####################################################
# A simple text calculator program written in
# python that reads user input from the command
# line and prints the output. Can handle addition,
# subtraction, multiplication, and division.
# Reads in an unlimited number of input
#
# By Doug Purcell
# website: http://www.purcellconsult.com
#
#
#####################################################

i = 0
nums, calc, count = [], [], 0
instructions = """
How to use program:
1\n+\n3\n=\n4.0
Can use: +, -, /, or * operators 
Enter your input below:
"""
print(instructions)
""" program only reads input on a new
line so not very user friendly.
Will create updated version of calculator
so it can read in input horizontally """
while True:
    compute = input()
    nums.append(compute)
    if compute == '=':
        break
for x in nums:
    if x.isnumeric():
        x = float(x)
        calc.append(x)
    else:
        calc.append(x)
while count < len(calc):
    if count == 1 and calc[count] == '+':
        i += calc[count - 1] + calc[count + 1]
        count += 1
    if count == 1 and calc[count] == '-':
        i += calc[count - 1] - calc[count + 1]
        count += 1
    if count == 1 and calc[count] == '*':
        i += calc[count - 1] * calc[count + 1]
        count += 1
    if count == 1 and calc[count] == '/':
        i += calc[count - 1] / calc[count + 1]
        count += 1
    elif calc[count] == '+':
        i += calc[count + 1]
        count += 1
    elif calc[count] == '-':
        i -= calc[count + 1]
        count += 1
    elif calc[count] == '*':
        i *= calc[count + 1]
        count += 1
    elif calc[count] == '/':
        i /= calc[count + 1]
        count += 1
    else:
        count += 1
        continue
    if count == '=':
        break
print(i)
