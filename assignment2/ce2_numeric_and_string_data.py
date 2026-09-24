'''
Durham College likes to promote its applied research 
centres, with promotional items such as AI Hub-branded 
rubber ducks. As somewhat of a publicity stunt, someone 
has floated the idea of completely covering one of the two 
reservoirs at Durham College’s Oshawa Campus with these 
ducks.
Can you estimate the size of these reservoirs, and then use 
a program to determine how many rubber ducks would be 
required to cover it almost completely?
'''


# 1. Clearly define the result (OUTPUT)
#   How many rubber ducks are required to cover the reservoir.
# 2. Determine what data is needed, and how to get it (INPUT)
#    Ask user forReservoir size in square meters or length and width in meters, and rubber duck size in centimeters.
# 3. List the steps needed in between (PROCESS)
#   A. Ask the user for the size of the reservoir in square meters or length and width in meters.
#   B. Ask the user for the size of a rubber duck in centimeters.
# 4. Write your PLAN as pseudo-code and/or a flowchart
#   GET user choice for reservoir size input method
#   IF user chooses square meters
#       GET reservoir size in square meters
#   ELSE IF user chooses length and width in meters
#       GET reservoir length and width in meters
#   GET rubber duck length and width in centimeters
#   CONVERT reservoir size to square centimeters
#   CALCULATE number of rubber ducks required to cover the reservoir
# 5. Test your plan for logical errors (DESK-CHECK)

# 1 OUTPUT: The number of rubber ducks required to cover the reservoir.

# 2 INPUT: The dimensions of the reservoir (length and width) and the dimensions of a rubber duck (length and width).
class NegativeValueError(Exception):
    pass
x = True
y = True
z = True

# This states what the program does and what the user needs to input.
print("This is a program to calculate how many rubber ducks you need to cover a reservoir of a given size." \
    "The reservoir size can be given in either square meters or in legth and width in meters. The rubber duck size" \
    " will be given in centimeters.")
print("Please choose one of the following options:")
print("1. Enter the length and width of the reservoir in meters.")
print("2. Enter the size of the reservoir in square meters.")

# This is where the user chooses how they want to input the reservoir size, and then inputs the dimensions of the reservoir and rubber duck.

while x:
    try:
        get = input("Enter your choice (1 or 2): ")
        if get == "1":
            reservoir_length = float(input("Enter the length of the reservoir in meters: "))
            reservoir_width = float(input("Enter the width of the reservoir in meters: "))
            if reservoir_length <= 0 or reservoir_width <= 0:
                raise NegativeValueError
        elif get == "2":                  
            reservoir_size = float(input("Enter the size of the reservoir in square meters: "))
            if reservoir_size <= 0:
                raise NegativeValueError
        x = False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except NegativeValueError:
        print("Invalid input. Please enter a positive number.")
    

# This is where the user inputs the size of the rubber duck.

while y:
    try:
        rubber_duck_size_length = float(input("Enter the length of a rubber duck in centimeters: "))
        rubber_duck_size_width = float(input("Enter the width of a rubber duck in centimeters: "))
        if rubber_duck_size_length <= 0 or rubber_duck_size_width <= 0:
            raise NegativeValueError
        y = False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except NegativeValueError:
        print("Invalid input. Please enter a positive number.")

# This calculates the number of rubber ducks required to cover the reservoir.
reservoir_size_cm2 = reservoir_size * 10000  # Convert square meters to square centimeters
rubber_duck_size_cm2 = rubber_duck_size_length * rubber_duck_size_width
number_of_ducks = reservoir_size_cm2 / rubber_duck_size_cm2

# This is where we tell the user how many rubber ducks they would need to fill the reservoir.
print(f"You would need approximately {number_of_ducks:.0f} rubber ducks to cover the reservoir.")

while z:
    print("Press enter to exit.")
    input()
    z = False

