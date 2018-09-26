"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    no_months = int(input("How many months? "))

    for month in range(1, no_months + 1):
        monthly_income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(monthly_income)
    (income_report(incomes, no_months))


def income_report(incomes, no_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, no_months + 1):
        monthly_income = incomes[month - 1]
        total += monthly_income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, monthly_income, total))


main()
