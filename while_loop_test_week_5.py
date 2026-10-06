choice = ""
while choice != "0":
    print("\n1. Simple addition\n2. Practice code\n0. Exit")
    choice = input("Choice: ").strip()
    if choice == "1":
        num_1 = int(input("\nPlease enter your first number: "))
        num_2 = int(input("\nPlease enter your second number: "))
        print(str(f"\nThe result is {num_1 + num_2}"))
    elif choice == "2":
        print("Something Else")
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Choose 1, 2 or 0.")
