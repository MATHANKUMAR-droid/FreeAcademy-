
# MULTI-FUNCTION CALCULATOR
# Algebra with Python Project

import math
from fractions import Fraction
from sympy import symbols, Eq, solve, sympify, sqrt, simplify

x = symbols('x')


# 1. SOLVE PROPORTIONS
def solve_proportion():
    print("\n--- SOLVE PROPORTIONS ---")
    print("Enter three known values. Leave the unknown value blank.")

    a = input("First numerator (a): ")
    b = input("First denominator (b): ")
    c = input("Second numerator (c): ")
    d = input("Second denominator (d): ")

    values = [a, b, c, d]

    if values.count('') != 1:
        print("Please leave exactly one value blank.")
        return

    try:
        a, b, c, d = [
            float(v) if v else None for v in values
        ]

        if (b == 0 or d == 0) and d is not None and b is not None:
            print("Denominators cannot be zero.")
            return

        if a is None:
            if c == 0:
                print("Cannot determine a unique value.")
                return
            answer = b * c / d

        elif b is None:
            if d == 0:
                print("Cannot determine a unique value.")
                return
            answer = a * d / c

        elif c is None:
            if a == 0:
                print("Cannot determine a unique value.")
                return
            answer = a * d / b

        else:
            if a == 0:
                print("Cannot determine a unique value.")
                return
            answer = b * c / a

        print("Missing value =", answer)

    except (ValueError, TypeError, ZeroDivisionError):
        print("Invalid input.")


# 2. SOLVE EQUATIONS FOR X
def solve_for_x():
    print("\n--- SOLVE FOR X ---")
    print("Example: 2*x + 5 = 15")

    try:
        equation = input("Enter equation: ")
        left, right = equation.split('=')

        expression = Eq(sympify(left), sympify(right))
        result = solve(expression, x)

        if result:
            print("Solution:", result)
        else:
            print("No solution found.")

    except Exception as error:
        print("Invalid equation:", error)


# 3. FACTOR SQUARE ROOTS
def factor_square_root():
    print("\n--- FACTOR SQUARE ROOTS ---")

    try:
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("Please enter a non-negative integer.")
            return

        result = simplify(sqrt(number))
        print(f"Square root of {number} = {result}")

    except ValueError:
        print("Please enter a valid integer.")


# 4. DECIMAL TO FRACTION AND PERCENT
def decimal_conversion():
    print("\n--- DECIMAL CONVERSION ---")

    try:
        decimal = float(input("Enter decimal: "))

        fraction = Fraction(str(decimal))
        percent = decimal * 100

        print("Decimal:", decimal)
        print("Fraction:", fraction)
        print("Percentage:", percent, "%")

    except ValueError:
        print("Invalid decimal.")


# 5. FRACTION TO DECIMAL AND PERCENT
def fraction_conversion():
    print("\n--- FRACTION CONVERSION ---")

    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))

        if denominator == 0:
            print("Denominator cannot be zero.")
            return

        fraction = Fraction(numerator, denominator)
        decimal = float(fraction)
        percent = decimal * 100

        print("Simplified fraction:", fraction)
        print("Decimal:", decimal)
        print("Percentage:", percent, "%")

    except ValueError:
        print("Invalid input.")


# 6. PERCENT TO DECIMAL AND FRACTION
def percentage_conversion():
    print("\n--- PERCENTAGE CONVERSION ---")

    try:
        percentage = float(input("Enter percentage: "))

        decimal = percentage / 100
        fraction = Fraction(str(percentage)) / 100

        print("Percentage:", percentage, "%")
        print("Decimal:", decimal)
        print("Fraction:", fraction)

    except ValueError:
        print("Invalid percentage.")


# MAIN CALCULATOR MENU
def calculator():

    while True:

        print("\n================================")
        print("      MULTI-FUNCTION CALCULATOR")
        print("================================")

        print("1. Solve Proportions")
        print("2. Solve Equations for X")
        print("3. Factor Square Roots")
        print("4. Decimal to Fraction and Percent")
        print("5. Fraction to Decimal and Percent")
        print("6. Percent to Decimal and Fraction")
        print("7. Exit")

        choice = input("\nSelect an option (1-7): ")

        if choice == '1':
            solve_proportion()

        elif choice == '2':
            solve_for_x()

        elif choice == '3':
            factor_square_root()

        elif choice == '4':
            decimal_conversion()

        elif choice == '5':
            fraction_conversion()

        elif choice == '6':
            percentage_conversion()

        elif choice == '7':
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


# RUN THE CALCULATOR
calculator()
