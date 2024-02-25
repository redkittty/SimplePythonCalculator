print("Simple Python Calculator")
# Allows user to select between Addition, Subtraction, Multiplication, and Division
mode = int(input("Insert Mode: (1) = Addition, (2) = Subtraction (3) = Multiplication, (4) = Division: " ))
# Error Message for non-existent modes
if mode >= 5:
    print("Sorry, that mode is not available. Please try again")
# If statements to make stuff work and Answer Functions to make stuff look nice
if mode <= 4:
    if mode <= 0:
        print("Sorry, that mode is not available. Please try again")
    if mode >= 1:
        first = float(input("  " ))
        if mode == 1:
            second = float(input("+ " ))
            print(first + second)
        if mode == 2:
            second = float(input("- " ))
            print(first - second)
        if mode == 3:
            second = float(input("x " ))
            print(first * second)
        if mode == 4:
            second = float(input("/ " ))
            print(first / second)
