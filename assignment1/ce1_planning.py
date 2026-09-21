"""CE-1 Planning Assignment"""
"""
# COSC 1100 
# Kevin Tzambazis
# This is a program that calculates the total amount of ice cream sold in mL for one week based on the number of cones sold for each size.
"""


# 1.	Clearly define the result (OUTPUT)
# Identify amount of ice cream cones sold in one week and display total in mL
print("This program will calculate the total amount of ice cream sold in mL for one week.")
print("The sizes are: kid, small, medium, and large.")
print("Please enter the number of cones sold for each size.")

# 2.	Determine what data is needed, and how to get it (INPUT) 
kid_cones = 60
small_cones = 120
medium_cones = 240
large_cones = 360

class NegativeNumberError(Exception):
    pass

# Ask for number of kid, small, medium, and large cones to multiply with respective amounts
x = True
while x:
    try:
        get_kid_cones = int(input("Kid cones: "))
        get_small_cones = int(input("Small cones: "))
        get_medium_cones = int(input("Medium cones: "))
        get_large_cones = int(input("Large cones: "))
        if get_kid_cones < 0 or get_small_cones < 0 or get_medium_cones < 0 or get_large_cones < 0:
            raise NegativeNumberError
        x = False
    except ValueError:
        print("Please enter a valid integer.")
    except NegativeNumberError:
        print("Please enter a whole number greater than or equal to 0.")

# Multiply number of cones by each respective mL amount
kid_total = get_kid_cones * kid_cones
small_total = get_small_cones * small_cones
medium_total = get_medium_cones * medium_cones
large_total = get_large_cones * large_cones

# Add all mL amounts together
total_mL = kid_total + small_total + medium_total + large_total

# Print the mL total to the user
print(f"The total amount of ice cream sold in one week is {total_mL} mL.")

y = True
while y:
    print("Press Enter to exit the program.")
    input()
    y = False

# 4.	Write your PLAN as pseudo-code and/or a flowchart
# 5.	Test your plan for logical errors (DESK-CHECK) 
# 6.	Get your development environment ready (SET UP) 
# 7.	Translate your plan into code (CODE) 
# 8.	Attempt to run your program; find and fix syntax errors (DEBUG) 
# 9.	Run your program using test data (TEST) 
# 10.	Distribute