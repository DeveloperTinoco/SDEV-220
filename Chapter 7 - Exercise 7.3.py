

class Account():

    # Creates and sets the initial values for each variable
    def __init__(self, ID=1122, balance=100, annualInterestRate=4.5):
        self.__ID = ID
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    # Returns the ID value to show to the user
    def get_ID(self):
        return self.__ID

    # Returns the balance value to show to the user
    def get_balance(self):
        return self.__balance

    # Returns the annual interest rate
    def get_annualInterestRate(self):
        return self.__annualInterestRate

    # Calculates and returns the monthly interest rate
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate) / 12

    # Calculates and returns the monthly interest in terms of dollar value
    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    # Calculates any withdrawals
    def withdraw(self, amount):
        self.__balance -= amount

    # Calculates any deposits
    def deposit(self, amount):
        self.__balance += amount


# Creates an instance of the account class with the given ID, balance and annual interest rate parameters
account = Account(3345, 35000, 4.5)

# Shows the user their current balance
print("Your total account balance is: " + str(account.get_balance()) + ".")

# Creates a variable with a withdrawal amount and then passes that variable to the withdraw() function
x = 2500
account.withdraw(x)

# Shows the user their balance after their withdrawal
print("After withdrawing " + str(x) +
      " your new account balance is: " + str(account.get_balance()) + ".")

# Creates a variable with a deposit amount and then passes that variable to the deposit() function
y = 3000
account.deposit(y)

# Shows the user their balance after their deposit
print("After depositing " + str(y) + ", your new account balance is: " +
      str(account.get_balance()) + ".")

# Shows the user their information regarding their entire account
print("Your account ID is: " + str(account.get_ID()) + ". "
      "Your total balance is: " + str(account.get_balance()) + ". "
      "Your monthly interest rate is: " +
      str(account.getMonthlyInterestRate()) + ". "
      "Your monthly interest is: " + str(account.getMonthlyInterest()) + ". ")
