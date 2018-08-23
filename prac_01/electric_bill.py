
print("Electric bill estimator")
price = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
bill = price / 100 * daily_use * billing_days
print("Estimated bill: ${:.2f}".format(bill))

# TARIFF_11 = 0.244618
# TARIFF_31 = 0.136928
#
# MENU = """A - TARIFF 11
#  B - TARIFF 31
#  Q - Quit"""
# print("Select which tariff ", "\n", MENU)
# choice = input(">>> ").upper()
#
# while choice != "Q":
#     if choice == "A":
#         bill = TARIFF_11 * daily_use * billing_days
#         print("Estimated bill: ${:.2f}".format(bill))
#     elif choice == "B":
#         bill = TARIFF_31 * daily_use * billing_days
#         print("Estimated bill: ${:.2f}".format(bill))
#     else:
#         print("Invalid option")
#     print("Electric bill estimator")
#     print("Select which tariff ", "\n", MENU)
#     price = float(input("Enter cents per kWh: "))
#     daily_use = float(input("Enter daily use in kWh: "))
#     billing_days = int(input("Enter number of billing days: "))
#
#     choice = input(">>> ").upper()
# print("Thank you.")
