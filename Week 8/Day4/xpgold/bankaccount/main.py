class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.authenticated = False
        self.balance = 0

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True

    def deposit(self, amount):
        if self.authenticated:
            if amount > 0:
                self.balance += amount
            else:
                raise Exception("Invalid deposit amount. Amount must be positive.")
        else:
            raise Exception("Authentication required to perform this action.")

    def withdraw(self, amount):
        if self.authenticated:
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                else:
                    raise Exception("Insufficient balance.")
            else:
                raise Exception("Invalid withdrawal amount. Amount must be positive.")
        else:
            raise Exception("Authentication required to perform this action.")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.authenticated:
            if amount > 0:
                if self.balance - amount >= self.minimum_balance:
                    self.balance -= amount
                else:
                    raise Exception("Withdrawal not allowed. Minimum balance requirement not met.")
            else:
                raise Exception("Invalid withdrawal amount. Amount must be positive.")
        else:
            raise Exception("Authentication required to perform this action.")


class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list) or not all(isinstance(account, (BankAccount, MinimumBalanceAccount)) for account in account_list):
            raise Exception("Invalid account list. Must be a list of BankAccount or MinimumBalanceAccount instances.")
        self.account_list = account_list
        if try_limit <= 0:
            raise Exception("Invalid try limit. Must be a positive number.")
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("===== Main Menu =====")
            print("1. Log in")
            print("2. Exit")
            choice = input("Enter your choice (1-2): ")
            if choice == "1":
                self.log_in()
            elif choice == "2":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def log_in(self):
        while self.current_tries < self.try_limit:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            for account in self.account_list:
                account.authenticate(username, password)
                if account.authenticated:
                    self.show_account_menu(account)
                    return
            self.current_tries += 1
            print("Incorrect username or password. Please try again.")
        print("Maximum login tries reached. Shutting down...")

    def show_account_menu(self, account):
        while True:
            print("===== Account Menu =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                try:
                    account.deposit(amount)
                    print("Deposit successful.")
                except Exception as e:
                    print(f"Error: {str(e)}")
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                try:
                    account.withdraw(amount)
                    print("Withdrawal successful.")
                except Exception as e:
                    print(f"Error: {str(e)}")
            elif choice == "3":
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage:
account1 = BankAccount("user1", "pass1")
account2 = MinimumBalanceAccount("user2", "pass2", minimum_balance=1000)
account3 = BankAccount("user3", "pass3")

atm = ATM([account1, account2, account3], try_limit=3)
