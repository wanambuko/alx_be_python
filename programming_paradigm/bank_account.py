class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute
        self.__account_balance = initial_balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    # Display balance
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
