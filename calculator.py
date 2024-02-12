print("Simple Python Calculator")
# Allows user to select between Addition, Subtraction, Multiplication, and Division
mode = int(input("Insert Mode: (1) = Addition, (2) = Subtraction (3) = Multiplication, (4) = Division: " ))
# Error Message for modes 5+
if mode >= 5:
    print("Sorry, that mode is not available. Please try again")
# If statements to make stuff work and Answer Functions to make stuff look nice
if mode == 1:
    first = float(input("  " ))
    sumsecond = float(input("+ " ))
    sumanswer = first + sumsecond
    print("=",sumanswer)
if mode == 2:
    first = float(input("  " ))
    difsecond = float(input("- " ))
    difanswer = first - difsecond
    print("=",difanswer)
if mode == 3:
    first = float(input("  " ))
    mulsecond = float(input("x " ))
    mulanswer = first * mulsecond
    print("=",mulanswer)
if mode == 4:
    first = float(input("  " ))
    divsecond = float(input("/ " ))
    divanswer = first / divsecond
    print("=",divanswer)
