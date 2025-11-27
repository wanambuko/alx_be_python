import sys
from bank_account import BankAccount

def main():
    # Example starting balance
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split command and parameters
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Deposit command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")

    # Withdraw command
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    # Display balance
    elif command == "display":
        account.display_balance()

    # Invalid command
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
