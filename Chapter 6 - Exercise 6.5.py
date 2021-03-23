

# Creates a function to display the numbers entered from lowest to highest
def displayIncreasingNumbers(numbers):
    increasing = sorted(numbers)
    print("The numbers in increasing order are: " + str(increasing) + ".")

# Creates a function to display the numbers entered from highest to lowest


def displayDecreasingNumbers(numbers):
    decreasing = sorted(numbers, reverse=True)
    print("The numbers in decreasing order are: " + str(decreasing) + ".")


# Asks the user to input 3 number values
number1 = int(input("Please enter your first number: "))
number2 = int(input("Please enter your second number: "))
number3 = int(input("Please enter your third number: "))

# Puts the entered numbers in a list
numbersList = [number1, number2, number3]

# Passes the list into both functions to display both orders back to the user
displayIncreasingNumbers(numbersList)
displayDecreasingNumbers(numbersList)
