

# Creates a function that takes one argument
def countUppercase(inputString):

    # If there is no string entered by the user, then the 0 value is returned since no letters are present
    if not inputString:
        return 0

    # When a string is entered, this function recursively calls itself to see how many uppercase letters are present
    else:
        upper = countUppercase(inputString[1:])

        # Goes through the string and increments the counter if an uppercase letter is encountered
        if inputString[0].isupper():
            return upper + 1
        else:
            return upper


# Asks user for input
inputString = input(
    "Enter a string to see how many uppercase letters it contains: ")

# Passes the user's string input into the function
countUppercase(str(inputString))

# Shows the user how many uppercase letters are present in the string they entered
print("The amount of uppercase letters in the string that you entered is " +
      str(countUppercase(inputString)) + ".")
