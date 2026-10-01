'''
Should we expect a user to provide appropriate input?
    We shouldn't expect users to provide appropriate input if they're not instructed how to do so.

How can we help a user provide appropriate input?
    We can help a user to provide appropriate input by giving them instructions. Utilizing things like formatted strings asking for the
    exact type of input we are looking for, like an integer.

Is “appropriate” user input the same as “correct” user input?
    I don't believe that appropriate is the same as correct. An appropriate input would be something like inputting an integer when the program
    prompts for it. A correct input would be a valid input within the defined ranges that are set up in the program.

1. Clearly define the result (OUTPUT)
    Validate the following user information:
        Student name
        Student ID
        Exercise mark
        Attendance mode
    After validating the information to be in correct formatting, inform the user and terminate.

2. Determine what data is needed, and how to get it (INPUT)
    Student name: No trailing and leading spaces. Not all spaces or blank
    Student ID: 9 digits. Retain all zeros by converting to text after validating.
    Class mark: Whole number from 0-100 inclusive.
    Mode of attendance: Choose from "Online", "In person", or "Hybrid"

3. List the steps needed in between (PROCESS)
    Name: Input string for first name, input string for last name. Verify only alphabet characters with no spaces. Combine first and last names with
        a space in between.

    ID: Input integer for student number. Verify exactly 9 characters. Convert integer to text to preserve zeros.

    Mark: Input integer for class mark. Verify between 0-100.

    Mode: Set library for "Online, In person, Hybrid, online, in person, hybrid". Input string for mode. Match input against library.


# 4. Write your PLAN as pseudo-code and/or a flowchart

# 5. Test your plan for logical errors (DESK-CHECK)

'''

print("Welcome to the student information verifier! I will ask you for some information and inform you if you input it correctly.")

#Handle first and last name input with validation.
first_name = str(input("Please input your first name: "))
if first_name.isalpha():
    print("Thank you.")
else:
    print("The information you have entered was incorrectly formatted. Please do not enter anything other than alphabetic characters. Goodbye.")
    
last_name = str(input("Please input your last name: "))
if last_name.isalpha():
    print("Thank you.")
else:
    print("The information you have entered was incorrectly formatted. Please do not enter anything other than alphabetic characters. Goodbye.")

full_name = str(f"{first_name} {last_name}")

#Handle student ID input with validation.
student_id = int(input("Please input your 9 digit student ID: "))
if student_id.is_integer() == False:
    print("The information you have entered was incorrectly formatted. Please only enter a number in this field. Goodbye.")

student_id_count = (len(str(student_id)))
if student_id_count != 9:
    print("The information you have entered was incorrectly formatted. Please only enter a 9 digit number. Goodbye.")
else:
    print("Thank you.")

#Handle exercise mark input with validation.
exercise_mark = int(input("Please input your exercise mark: "))
if exercise_mark >= 0 and exercise_mark <= 100:
    print("Thank you.")
else:
    print("The information you have entered was incorrectly formatted. Please only enter a number from 0-100. Goodbye.")

attendance_mode = str(input("Please input your attendance mode from the following options: Online, In person, Hybrid: "))

list1 = ["Online", "online", "In-person", "In person", "in person", "in-person", "Hybrid", "hybrid"]

if attendance_mode not in list1:
    print("The information you have entered was incorrectly formatted. Please only enter an option from those provided. Goodbye.")
else:
    print("Thank you.")

#Tell user that all of the information was correct and terminate.
print(f"You have entered the information:{full_name}, {student_id}, {exercise_mark}, {attendance_mode}, and all of the information was correct! Great work my child.")