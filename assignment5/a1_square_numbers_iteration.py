'''
For this lab you will create a simple console application using Python that will graphically display all the square 
numbers within a range provided by the user. For our purposes, a square number is any number that can be 
computed by multiplying a whole number by itself. The first several square numbers are 1 (1 squared), 4 (2 
squared), 9 (3 squared) and 16 (4 squared). This assignment will provide you with the opportunity to design 
program logic with both individual and nested loops. It should also reinforce the time-saving value of planning 
before you code. 

Getting User Input: 
In the input phase of the program, display a banner-like header and then prompt the user for the bottom limit 
and the top limit to the numbers they want to investigate. The lower limit must be a whole number between the 
range of 1 and 10000 inclusive, and the upper limit must be between the lower limit and 10000 inclusive. Should 
the user enter something other than a valid, in-range number, then display an appropriate message that 
describes the problem and give the user the opportunity to input the limit again. 

Final Output:  
Once you have valid input, you will produce a list of all square numbers between the user’s entered lower bound 
and upper bound. Start by displaying “Square numbers between”, including the boundaries entered. In addition 
to displaying the square number, you will also display the square root of the number that it is the square of. 

1. Clearly define the result (OUTPUT)
    Display all numbers that have a square root between a given range set by the user.

2. Determine what data is needed, and how to get it (INPUT)
    An upper and lower bound, both within 1-10,000 - Ask the user for that input

3. List the steps needed in between (PROCESS)


4. Write your PLAN as pseudo-code and/or a flowchart


5. Test your plan for logical errors (DESK-CHECK)

'''

import math
x = True
y = True
lower_bound = 0
upper_bound = 0

class BadInput(Exception):
    pass
class SmallNum(Exception):
    pass

print("######################################################\n"
      "                SQUARE NUMBER FINDER                  \n"
      "######################################################\n\n")
print("This program will find all square numbers between a lower and upper bound set by the user between 1 and 10,000.")

while x:
    try:
        lower_bound = int(input("Please enter the lower bound: "))
        if lower_bound <= 0:
            raise BadInput
        elif lower_bound >= 10000:
            raise BadInput
        x = False
    except ValueError:
        print("Please enter a whole number between 1 and 10,000.")
    except BadInput:
        print("Please enter a whole number between 1 and 10,000.")

while y:
    try:
        upper_bound = int(input("Please enter the upper bound: "))
        if upper_bound <= 0:
            raise BadInput
        elif upper_bound >= 10000:
            raise BadInput
        elif upper_bound <= lower_bound:
            raise SmallNum
        y = False
    except ValueError:
        print("Please enter a whole number between 1 and 10,000.")
    except BadInput:
        print("Please enter a whole number between 1 and 10,000.")
    except SmallNum:
        print("Please enter a number larger than the lower bound.")

for count in range(lower_bound, upper_bound):
    root = math.sqrt(count)
    if root % 1 == 0:
        print(f"{count}({int(root)} squared)")

str(input("Press enter to exit program."))