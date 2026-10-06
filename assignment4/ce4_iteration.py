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



# Number of hot dogs sold
traditional_dog_sold = "0"
veggie_dog_sold = "0"
curry_dog_sold = "0"
total_dog_sold = traditional_dog_sold + veggie_dog_sold + curry_dog_sold


Input = (Number_of_Traditional_Dog_sold []) + (Number_of_Veggie_Dog_sold []) + (Number_of_Curry_Dog_sold[])

print("Welcome to the Mystical Dog Machine")

Choice = ""
while Choice != "0":
    print("Please select from the following options:\n0. Tally total\n1. Regular Hot Dog\n2. Veggie Hot Dog\n3. Curry Hot Dog")
    if Choice == "1":
        Number_of_Traditional_Dog_sold = int(input("Enter the number of Traditional Dogs sold: "))
        traditional_dog_sold += Number_of_Traditional_Dog_sold
        elif Choice == "2":
        Number_of_Veggie_Dog_sold = int(input("Enter the number of Veggie Dogs sold:")

       