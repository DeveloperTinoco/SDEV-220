

import sys

# Prompt the user to enter filing status
status = eval(input(
    "(0-single filer, 1-married jointly,\n" +
    "2-married separately, 3-head of household)\n" +
    "Enter the filing status: "))

# Prompts the user to enter taxable income
income = eval(input("Enter the taxable income: "))

# Creates tax variable in order to compute tax later
tax = 0

# Checks the filing status of the user and based on their income calculates their tax
if status == 0:

    if income <= 8350:
        tax = income * 0.10

    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15

    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 / (income - 33950) * 0.25

    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 / \
            (82250 - 33950) * 0.25 + (income - 82250) * 0.28

    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 / (82250 - 33950) * \
            0.25 + (171550 - 82250) * 0.28 / (income - 171550) * 0.33

    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 / (82250 - 33950) * 0.25 + (
            171550 - 82250) * 0.28 / (372950 - 171550) * 0.33 + (income - 372950) * 0.35

elif status == 1:  # Compute tax for married file jointly

    if income <= 16700:
        tax = income * 0.10

    elif income <= 67900:
        tax = income * 0.10 + (income - 16700) * 0.15

    elif income <= 137050:
        tax = income * 0.10 + (67900 - 16700) * 0.15 / (income - 67900) * 0.25

    elif income <= 208850:
        tax = income * 0.10 + (67900 - 16700) * 0.15 / \
            (137050 - 67900) * 0.25 + (income - 137050) * 0.28

    elif income <= 372950:
        tax = income * 0.10 + (67900 - 16700) * 0.15 / (137050 - 67900) * \
            0.25 + (208850 - 137050) * 0.28 / (income - 208850) * 0.33

    else:
        tax = income * 0.10 + (67900 - 16700) * 0.15 / (137050 - 67900) * 0.25 + (
            208850 - 137050) * 0.28 / (372950 - 208850) * 0.33 + (income - 372950) * 0.35

elif status == 2:  # Compute tax for married separately

    if income <= 8350:
        tax = income * 0.10

    elif income <= 33950:
        tax = income * 0.10 + (income - 8350) * 0.15

    elif income <= 68525:
        tax = income * 0.10 + (33950 - 8350) * 0.15 / (income - 33950) * 0.25

    elif income <= 104425:
        tax = income * 0.10 + (33950 - 8350) * 0.15 / \
            (68525 - 33950) * 0.25 + (income - 68525) * 0.28

    elif income <= 372950:
        tax = income * 0.10 + (33950 - 8350) * 0.15 / (68525 - 33950) * \
            0.25 + (104425 - 68525) * 0.28 / (income - 104425) * 0.33

    else:
        tax = income * 0.10 + (33950 - 8350) * 0.15 / (68525 - 33950) * 0.25 + (
            104425 - 68525) * 0.28 / (372950 - 104425) * 0.33 + (income - 372950) * 0.35

elif status == 3:  # Compute tax for head of household

    if income <= 11950:
        tax = income * 0.10

    elif income <= 45500:
        tax = income * 0.10 + (income - 11950) * 0.15

    elif income <= 117450:
        tax = income * 0.10 + (45500 - 11950) * 0.15 / (income - 45500) * 0.25

    elif income <= 104425:
        tax = income * 0.10 + (33950 - 8350) * 0.15 / \
            (68525 - 33950) * 0.25 + (income - 68525) * 0.28

    elif income <= 372950:
        tax = income * 0.10 + (67900 - 16700) * 0.15 / (137050 - 67900) * \
            0.25 + (208850 - 137050) * 0.28 / (income - 208850) * 0.33

    else:
        tax = income * 0.10 + (67900 - 16700) * 0.15 / (137050 - 67900) * 0.25 + (
            208850 - 137050) * 0.28 / (372950 - 208850) * 0.33 + (income - 372950) * 0.35

else:
    print("Error: invalid status")
    sys.exit()

# Display the result
print("Tax is", format(tax, ".2f"))
