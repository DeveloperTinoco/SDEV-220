

# Creates Account class


class Account:

    # Initializes the variables
    def __init__(self, id, balance):
        self.__id = id
        self.__balance = balance

    # Returns the balance of the user
    def getBalance(self):
        return format(self.__balance, ".2f")

    # Returns the id of the user
    def getID(self):
        return self.__id

    # Sets the id for the user
    def setID(self):
        self.__id = id

    # Deposits money into the user's account
    def deposit(self, depositedMoney):
        self.__balance += depositedMoney

    # Withdraws money from the user's account
    def withdraw(self, withdrawalMoney):

        # Makes sure that the user can not withdraw more money than they have in their balance
        if withdrawalMoney < self.__balance:
            self.__balance -= withdrawalMoney
        else:
            print("\n You are trying to withdraw more than what is available in your account. Please check your balance first before attempting to withdraw again. \n")

# Creates main function


def main():

    # Creates accounts list that will act as an instance per each user for 10 users that have a starting balance of 500
    accounts = []
    for i in range(10):
        accounts.append(Account(i, 500))

    # Enters the "menu" and doesn't quit until you manually exit
    while True:

        # Asks for id from user
        id = eval(input("\n\n Enter an account ID: "))

        # Checks the id that the user entered to make sure it is valid
        if id >= 0 and id <= 9:

            # Creates the menu for the user to interact with
            print(
                "\n Main Menu \n 1: Check Balance \n 2: Withdraw \n 3: Deposit \n 4: Exit \n")
            mainMenuChoice = eval(input(" Enter a choice: "))

            # While the user's choice is not the "Exit" option, the menu will continue to reset after every interaction
            while mainMenuChoice != 4:

                # Choice to view balance
                if mainMenuChoice == 1:
                    balance = accounts[id].getBalance()
                    print("\n Your balance is $" + str(balance) + ".")
                    print(
                        "\n Main Menu \n 1: Check Balance \n 2: Withdraw \n 3: Deposit \n 4: Exit \n")
                    mainMenuChoice = eval(input("Enter a choice: "))

                # Choice to withdraw money
                elif mainMenuChoice == 2:
                    withdrawalMoney = eval(
                        input("\n Enter how much money you would like to withdraw: "))
                    accounts[id].withdraw(withdrawalMoney)
                    print(
                        "\n Main Menu \n 1: Check Balance \n 2: Withdraw \n 3: Deposit \n 4: Exit \n")
                    mainMenuChoice = eval(input("Enter a choice: "))

                # Choice to deposit money
                elif mainMenuChoice == 3:
                    depositedMoney = eval(
                        input("\n Enter how much money you would like to deposit: "))
                    accounts[id].deposit(depositedMoney)
                    print(
                        "\n Main Menu \n 1: Check Balance \n 2: Withdraw \n 3: Deposit \n 4: Exit \n")
                    mainMenuChoice = eval(input("Enter a choice: "))

                # Does not allow the user to enter an invalid option
                else:
                    mainMenuChoice = eval(
                        input("\n You must enter a valid option (1-4): "))

        # Makes sure the user enters a valid id number
        else:
            print(" Invalid account ID, please try again.")


# Runs the program
if __name__ == "__main__":
    main()
