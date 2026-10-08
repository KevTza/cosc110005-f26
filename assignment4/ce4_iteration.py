'''Kevin Tzambazis and Casey Mandl-Gibson'''

'''John is the owner of a hotdog stand. He sells three (3) types of hot dogs, 
Traditional, Veggie Dog, and Curry Hot Dog. He would like a simple console 
based system to assist him in tallying and determining which type of hot dog is 
more popular. 
As he intends to enter the data as the orders come in, he would like the system 
to present the options of the hot dogs in a repeated loop, with an extra option 
to tally and exit the system. This will be done with menu options like: 1, 2, 3, 4.
When an option is selected, the user is presented with a chance to enter a 
whole number, indicating the number sold. 
The tally option (4) would display the number sold for each type of hot dog with 
a percentage of the total number of hot dogs sold before exiting.
Remember, John may not always hit the proper keys!'''

'''1. Clearly define the result (OUTPUT)

Total number of dogs sold with percentage breakdown for each, after exit condition is met.

2. Determine what data is needed, and how to get it (INPUT)

Number of Traditional Dog sold,
Number of Veggie Dog sold,
Number of Curry Dog sold,
Menu choices

3. List the steps needed in between (PROCESS)

Present selection menu for dog types
After selection ask for number of type
Add number given to running total for that type
Present selection menu again
After Tally option is picked add all running totals together
Print final total and exit

4. Write your PLAN as pseudo-code and/or a flowchart

5. Test your plan for logical errors (DESK-CHECK)'''



# Hot dog variables
traditional_sold = "0"
veggie_sold = "0"
curry_sold = "0"
total_sold = "0"

# Intro
print("Welcome to the Mystical Dog Machine")

# Menu loop start
choice = ""
class WrongChoice(Exception):
    pass
list1 = ["0", "1", "2", "3"]

while choice != 0:
    try:
        choice = (input("Please select from the following options  :\n0. Tally total\n1. Regular Hot Dog\n2. Veggie Hot Dog\n3. Curry Hot Dog\n"))
        if choice not in list1:
            raise WrongChoice
    except WrongChoice:
        print("Sorry. Please input a number provided.")

    # Traditional choice
    try:
        if choice == "1":
            new_traditional_sold = int(input("Enter the number of Traditional hot dogs sold: "))
            traditional_sold = int(traditional_sold) + int(new_traditional_sold)

    # Veggie choice
        elif choice == "2":
            new_veggie_sold = int(input("Enter the number of Veggie hot dogs sold: "))
            veggie_sold = int(veggie_sold) + int(new_veggie_sold)

    # Curry choice
        elif choice == "3":
            new_curry_sold = int(input("Enter the number of Curry hot dogs sold: "))
            curry_sold = int(curry_sold) + int(new_curry_sold)

    
    # Tally choice
        elif choice == "0":
            total_sold = int(traditional_sold) + int(veggie_sold) + int(curry_sold)
            traditional_percent = int(traditional_sold) / int(total_sold) * 100
            veggie_percent = int(veggie_sold) / int(total_sold) * 100
            curry_percent = int(curry_sold) / int(total_sold) * 100
            print(f"Thanks for using the Mystical Dog Machine. Your totals are:\nTraditional hot dogs: {traditional_sold}\nVeggie hot dogs: {veggie_sold}\nCurry hot dogs: {curry_sold}")
            print(f"Your dog breakdown is:\nTraditional hot dogs: {traditional_percent:.0f}%\nVeggie hot dogs: {veggie_percent:.0f}%\nCurry hot dogs: {curry_percent:.0f}%")

    except ValueError:
        print("Sorry. Please input a whole number.")
            