"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {months}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(income):
    """This will print the report based on the incomes"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(income,1):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()