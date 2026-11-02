'''
You have now progressed beyond the midpoint of this course and would like to 
write a program to calculate your midterm mark. The description on how your 
midterm mark was calculated is in the course outline. Please refer back to the 
course outline for details.
Your program must ask the user for their marks for each assessment, ordered by 
type. The assessments include the Pre-Class Activities, Class Exercises, the first 
Test. Once the user finishes their entry, calculate and display the user’s grade as 
a percentage and their percentage for each type of assessment.
Your user may not always enter the correct details when asked. Ensure your 
program can identify that and guide the user on entering valid data

Input:
    Get mark for each assessment in a list for each type.

Output:
    Display average for each assessment type and average for all assessment types combined.

Steps inbetween:
    Add all entries to each respective list together, then divide by number of entries in that list.
    Add all averaged list values together and average by number of lists.

Pseudo code or flowchart:
    Please see flowchart.

'''

exercises = list()
assignments = list()
tests = list()
x = False
y = False
z = False
exercises_average = 0
assignments_average = 0
tests_average = 0

print("This program will ask you for your marks as percentages for every assessment you have had so far in this class.\n"
      "There are three categories of assessment: Class Exercises, Assignments, and Tests.\n")


print("Please input your marks for all of your class exercises. Input x to finish adding.")

while x == False:
    try:
        mark = str(input())
        if mark.isnumeric() == True:
            if int(mark) <= 100:
                exercises.append(mark)
            elif int(mark) >=100:
                raise ValueError
        elif mark == "x":
            x = True
        elif mark != "x":
            raise ValueError
    except ValueError:
        print("Please input either a valid mark of 100 or less, or x to exit.")


print("Please input your marks for all of your assignments. Input x to finish adding.")

while y == False:
    try:
        mark = str(input())
        if mark.isnumeric() == True:
            if int(mark) <= 100:
                assignments.append(mark)
            elif int(mark) >=100:
                raise ValueError
        elif mark == "x":
            y = True
        elif mark != "x":
            raise ValueError
    except ValueError:
        print("Please input either a valid mark of 100 or less, or x to exit.")


print("Please input your marks for all of your tests. Input x to finish adding.")

while z == False:
    try:
        mark = str(input())
        if mark.isnumeric() == True:
            if int(mark) <= 100:
                tests.append(mark)
            elif int(mark) >=100:
                raise ValueError
        elif mark == "x":
            z = True
        elif mark != "x":
            raise ValueError
    except ValueError:
        print("Please input either a valid mark of 100 or less, or x to exit.")


for e_value in exercises:
    exercises_average += int(e_value)
exercises_average /= len(exercises)

print(f"Your mark average for your exercises is :{exercises_average:.2f}.")

for a_value in assignments:
    assignments_average += int(a_value)
assignments_average /= len(assignments)

print(f"Your mark average for your assignments is :{assignments_average:.2f}.")

for t_value in tests:
    tests_average += int(t_value)
tests_average /= len(tests)

print(f"Your mark average for your tests is :{tests_average:.2f}.")

total_average = exercises_average + assignments_average + tests_average
total_average /= 3

print(f"Your overall average for your class is :{total_average:.2f}.")

str(input("Press enter to exit program."))