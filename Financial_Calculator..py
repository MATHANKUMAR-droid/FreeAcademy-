
!pip install numpy sympy pandas -q

import math
import numpy as np
import sympy as sp
import pandas as pd

print("Financial Calculator is ready!")

# ============================================================
# FINANCIAL CALCULATOR
# Python | NumPy | SymPy | Pandas
# ============================================================

import math
import numpy as np
import sympy as sp
import pandas as pd


# ============================================================
# 1. ANNUITY CALCULATOR
# Monthly or Continuous Growth
# ============================================================

def annuity_calculator():

    print("\n===== ANNUITY CALCULATOR =====")

    print("1. Monthly contributions with monthly compounding")
    print("2. Continuous contributions with continuous growth")

    choice = input("Choose an option (1 or 2): ")

    try:

        payment = float(input("Enter regular payment amount: "))
        annual_rate = float(input("Enter annual interest rate (%): "))
        years = float(input("Enter investment period (years): "))

        if payment < 0 or years < 0 or annual_rate <= -100:
            print("Invalid financial values.")
            return

        r = annual_rate / 100

        if choice == "1":

            months = int(round(years * 12))
            monthly_rate = r / 12

            if months == 0:
                future_value = 0

            elif monthly_rate == 0:
                future_value = payment * months

            else:
                future_value = (
                    payment *
                    (((1 + monthly_rate) ** months - 1)
                     / monthly_rate)
                )

            print("\nMonthly Annuity Result")
            print(f"Monthly payment: {payment:,.2f}")
            print(f"Number of payments: {months}")

        elif choice == "2":

            if r == 0:
                future_value = payment * years

            else:
                future_value = (
                    payment * (math.exp(r * years) - 1) / r
                )

            print("\nContinuous Annuity Result")
            print(f"Annual contribution rate: {payment:,.2f}")

        else:
            print("Invalid option.")
            return

        print(f"Future Value: {future_value:,.2f}")

    except (ValueError, OverflowError):
        print("Please enter valid numerical values.")


# ============================================================
# 2. MONTHLY MORTGAGE PAYMENT CALCULATOR
# ============================================================

def mortgage_calculator():

    print("\n===== MORTGAGE CALCULATOR =====")

    try:

        principal = float(input("Enter loan amount: "))
        annual_rate = float(input("Enter annual interest rate (%): "))
        years = float(input("Enter loan duration (years): "))

        if principal <= 0 or years <= 0 or annual_rate < 0:
            print("Enter a positive loan amount and duration.")
            return

        monthly_rate = annual_rate / 100 / 12
        total_months = int(round(years * 12))

        if monthly_rate == 0:

            monthly_payment = principal / total_months

        else:

            monthly_payment = (
                principal *
                monthly_rate *
                (1 + monthly_rate) ** total_months
                /
                ((1 + monthly_rate) ** total_months - 1)
            )

        total_payment = monthly_payment * total_months
        total_interest = total_payment - principal

        print("\nMORTGAGE RESULTS")
        print(f"Loan amount: {principal:,.2f}")
        print(f"Monthly payment: {monthly_payment:,.2f}")
        print(f"Total payment: {total_payment:,.2f}")
        print(f"Total interest: {total_interest:,.2f}")

    except (ValueError, OverflowError, ZeroDivisionError):
        print("Invalid input.")


# ============================================================
# 3. RETIREMENT INVESTMENT BALANCE
# ============================================================

def retirement_calculator():

    print("\n===== RETIREMENT INVESTMENT CALCULATOR =====")

    try:

        initial_investment = float(
            input("Enter initial investment amount: ")
        )

        monthly_contribution = float(
            input("Enter monthly contribution: ")
        )

        annual_rate = float(
            input("Enter expected annual return (%): ")
        )

        years = float(
            input("Enter number of investment years: ")
        )

        if (
            initial_investment < 0
            or monthly_contribution < 0
            or annual_rate <= -100
            or years < 0
        ):
            print("Invalid investment values.")
            return

        months = int(round(years * 12))
        monthly_rate = annual_rate / 100 / 12

        if months == 0:

            balance = initial_investment

        elif monthly_rate == 0:

            balance = (
                initial_investment +
                monthly_contribution * months
            )

        else:

            initial_future_value = (
                initial_investment *
                (1 + monthly_rate) ** months
            )

            contributions_future_value = (
                monthly_contribution *
                (((1 + monthly_rate) ** months - 1)
                 / monthly_rate)
            )

            balance = (
                initial_future_value +
                contributions_future_value
            )

        invested_amount = (
            initial_investment +
            monthly_contribution * months
        )

        earnings = balance - invested_amount

        print("\nRETIREMENT PROJECTION")
        print(f"Final investment balance: {balance:,.2f}")
        print(f"Total money invested: {invested_amount:,.2f}")
        print(f"Estimated investment earnings: {earnings:,.2f}")

    except (ValueError, OverflowError):
        print("Invalid input.")


# ============================================================
# 4. TIME REQUIRED TO DOUBLE AN INVESTMENT
# ============================================================

def doubling_calculator():

    print("\n===== INVESTMENT DOUBLING CALCULATOR =====")

    try:

        principal = float(input("Enter initial investment: "))

        annual_rate = float(
            input("Enter annual interest rate (%): ")
        )

        if principal <= 0 or annual_rate <= 0:
            print("Investment and interest rate must be positive.")
            return

        rate = annual_rate / 100

        # Annual compounding
        years = math.log(2) / math.log(1 + rate)

        # Rule of 72 approximation
        rule_72 = 72 / annual_rate

        final_amount = principal * 2

        print("\nDOUBLING RESULTS")
        print(f"Initial investment: {principal:,.2f}")
        print(f"Target investment: {final_amount:,.2f}")
        print(f"Exact doubling time: {years:.2f} years")
        print(f"Rule of 72 estimate: {rule_72:.2f} years")

    except (ValueError, OverflowError, ZeroDivisionError):
        print("Invalid input.")


# ============================================================
# 5. LOGARITHMIC EQUATION SOLVER
# ============================================================

def logarithmic_solver():

    print("\n===== LOGARITHMIC EQUATION SOLVER =====")

    print("Supported example:")
    print("log(x, 2) = 3")
    print("log(x) = 2")
    print("log(x, 10) = 2")

    try:

        equation = input("\nEnter logarithmic equation: ")

        if "=" not in equation:
            print("Please enter an equation containing '='.")
            return

        left, right = equation.split("=", 1)

        x = sp.symbols("x", real=True)

        lhs = sp.sympify(left)
        rhs = sp.sympify(right)

        result = sp.solve(
            sp.Eq(lhs, rhs),
            x
        )

        valid_results = []

        for solution in result:

            if solution.is_real is False:
                continue

            # Check the original equation numerically
            try:
                value = float(solution)

                if not math.isfinite(value):
                    continue

                if value <= 0:
                    # Logarithms require positive arguments
                    continue

                valid_results.append(solution)

            except (ValueError, TypeError, OverflowError):
                continue

        if valid_results:

            print("\nSOLUTIONS")

            for solution in valid_results:
                print(f"x = {solution}")

        else:

            print("No valid real solution found.")

    except Exception as error:

        print("Unable to solve equation:", error)


# ============================================================
# 6. SCIENTIFIC NOTATION CONVERTER
# ============================================================

def scientific_notation_converter():

    print("\n===== SCIENTIFIC NOTATION CONVERTER =====")

    print("1. Decimal to scientific notation")
    print("2. Scientific notation to decimal")

    choice = input("Choose conversion (1 or 2): ")

    try:

        if choice == "1":

            number = float(input("Enter decimal number: "))

            if not math.isfinite(number):
                print("Enter a finite number.")
                return

            print("\nSCIENTIFIC NOTATION")
            print(f"{number:.6e}")

        elif choice == "2":

            coefficient = float(
                input("Enter coefficient: ")
            )

            exponent = int(
                input("Enter exponent: ")
            )

            number = coefficient * (10 ** exponent)

            print("\nDECIMAL VALUE")
            print(f"{number:.10g}")

        else:

            print("Invalid option.")

    except (ValueError, OverflowError):
        print("Invalid scientific notation input.")


# ============================================================
# MAIN FINANCIAL CALCULATOR MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 48)
        print("           FINANCIAL CALCULATOR")
        print("=" * 48)

        print("1. Annuity Calculator")
        print("2. Monthly Mortgage Calculator")
        print("3. Retirement Investment Calculator")
        print("4. Investment Doubling Calculator")
        print("5. Logarithmic Equation Solver")
        print("6. Scientific Notation Converter")
        print("7. Exit")

        print("=" * 48)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            annuity_calculator()

        elif choice == "2":
            mortgage_calculator()

        elif choice == "3":
            retirement_calculator()

        elif choice == "4":
            doubling_calculator()

        elif choice == "5":
            logarithmic_solver()

        elif choice == "6":
            scientific_notation_converter()

        elif choice == "7":

            print("\nThank you for using Financial Calculator!")
            break

        else:

            print("\nInvalid choice. Please select 1-7.")


# RUN APPLICATION

if __name__ == "__main__":
    main()
