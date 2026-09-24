class Account:
    """Base class for a bank account."""

    def __init__(self, name, number):
        self.name = name
        self.number = str(number)
        self.__balance = 0.0

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += float(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def __str__(self):
        return f"{self.name} [{self.number}] P {self.__balance:g}" if self.__balance == int(self.__balance) else f"{self.name} [{self.number}] P {self.__balance}"

    def __del__(self):
        # A destructor may be called during interpreter shutdown, so avoid
        # assuming that every attribute is still available.
        number = getattr(self, "number", "")
        if number:
            print(f"Account {number} closed")


class SavingsAccount(Account):
    """An account that earns the configured interest rate."""

    def __init__(self, name, number):
        super().__init__(name, number)
        self.__interest = 0.05

    def addInterest(self):
        self.deposit(self.getBalance() * self.__interest)


class Bank:
    """A bank that manages checking and savings accounts."""

    def __init__(self, name):
        self.name = name
        self.__accounts = []
        print(f"Welcome to {self.name}")

    def showAccounts(self):
        print("Showing accounts")
        for account in self.__accounts:
            print(account)

    def openAccount(self):
        print("Ready to open an account")
        name = input("Account name: ")
        number = input("Account number: ")
        account_type = input("Account type (savings or checking): ").strip().lower()

        if account_type == "savings":
            account = SavingsAccount(name, number)
        else:
            account = Account(name, number)

        self.__accounts.append(account)
        print("Account created")
        print(account)

    def closeAccount(self):
        print("Ready to close an account")
        number = input("Enter account number: ").strip()
        for index, account in enumerate(self.__accounts):
            if account.number == number:
                del self.__accounts[index]
                print("Account closed")
                return
        print("Account not found")

    def deposit(self):
        print("Ready to deposit an amount")
        amount = float(input("Enter amount to deposit: "))
        print(f"You are about to deposit an amount of P {amount}")
        number = input("Enter account number: ").strip()

        for account in self.__accounts:
            if account.number == number:
                account.deposit(amount)
                print("Deposit successful")
                print(account)
                return
        print("Account not found")

    def addInterest(self):
        print("Adding interest to all savings accounts")
        for account in self.__accounts:
            if isinstance(account, SavingsAccount):
                account.addInterest()
                print(f"Interest added to account {account.number}")
                print(account)

    def __del__(self):
        name = getattr(self, "name", "")
        accounts = getattr(self, "_Bank__accounts", [])
        if name:
            print(f"Thank you for banking with {name}")
        # Clear the collection so each account's destructor is invoked while
        # the bank is being destroyed.
        accounts.clear()


if __name__ == "__main__":
    mbtc = Bank("Metrobank")
    mbtc.openAccount()
    mbtc.openAccount()
    mbtc.showAccounts()
    mbtc.deposit()
    mbtc.deposit()
    mbtc.addInterest()
    mbtc.closeAccount()
