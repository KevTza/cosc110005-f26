# The idea behind this is to make a program that counts to 100 and prints "Fizz" for multiples of 3,
# "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both 3 and 5.

x = 1
a, b, c = 0, 0, 0
d = True

while d:
    while x <= 100:
        if x % 3 == 0 and x % 5 == 0:
            print(f"{x}: FizzBuzz")
            c += 1
        elif x % 3 == 0:
            print(f"{x}: Fizz")
            a += 1
        elif x % 5 == 0:
            print(f"{x}: Buzz")
            b += 1
        
        else:
            print(f"{x}")
        x += 1

    print(f"Total Fizz: {a}")
    print(f"Total Buzz: {b}")
    print(f"Total FizzBuzz: {c}")

    print("Do you want to run the program again? (y/n)")
    response = input().lower()
    if response == "y":
        x = 1
        a, b, c = 0, 0, 0
    else:
        d = False