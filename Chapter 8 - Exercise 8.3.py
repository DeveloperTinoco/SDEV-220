

# Creates the function that will check the password
def checkpassword(password):

    # Counters that will track digits and characters in password that is entered
    digits = 0
    characters = 0

    # Loops through the entered password and counts the amount of digits and overall characters that were used
    for i in password:
        if i.isalpha():
            characters += 1
        elif i.isdigit():
            digits += 1
            characters += 1
        else:
            print("Password may only contain letters and digits!")
            return

    # Checks to see if the requirements for the password were met
    if characters >= 9:
        if digits >= 3:
            print("Password meets the requirements and is valid!")
        else:
            print("Password does not meet the digit requirements and is not valid!")

    else:
        print("Password does not meet the character requirements and is not valid!")


# Creates a variable that asks the user to enter a desired password and passes it to the checkpassword() function
Password = str(input("Enter a password: "))
checkpassword(Password)
