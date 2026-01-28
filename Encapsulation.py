class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

ac = BankAccount(1000)
print(ac.get_balance())   # 1000
print(ac.__balance)     # ❌ Error
