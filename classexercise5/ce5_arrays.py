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


Pseudo code or flowchart:
    Please see flowchart.

'''

exercises = list()
assignments = list()
tests = list()
x = False
y = True
z = True

print("This program will ask you for your marks as percentages for every assessment you have had so far in this class.\n"
      "There are three categories of assessment: Class Exercises, Assignments, and Tests.\n")


print("Please input your marks for all of your class exercises. Input x to finish adding.")

while x == False:
    try:
        mark = str(input())
        if mark.isnumeric:
            exercises.append(mark)
        elif mark == "x":
            x = True
            # break
    except ValueError:
        print("gfdbdf")

print("done")

'''
print("Please input your marks for all of your assignments. Input x to finish adding.")

while input != "x":


print("Please input your marks for all of your tests. Input x to finish adding.")

while input != "x":
'''