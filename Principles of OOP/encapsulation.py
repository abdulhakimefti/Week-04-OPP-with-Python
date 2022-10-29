class Account:
    def __init__(self, accountHolder, initialBalance):
        self.accountHolder = accountHolder
        self.__balance = initialBalance
        self._account_number=13214

    def deposit(self, amount):
        print(f'adding {amount}')
        self.__balance += amount

    def withdraw(self, amount):
        print(f'withdraw {amount}')
        self.__balance -= amount


class StudentAccount(Account):
    def __init__(self, holder, initialBalance, school):
        self.school = school
        super().__init__(holder, initialBalance)
    def getBalance(self):
        return self.__balance
    def getAccNum(self):
        return self._account_number

rafsan = StudentAccount('rafsan', 50000, 'IUB')
# print(rafsan.__balance)
rafsan.deposit(20000)
rafsan.deposit(32342)
# rafsan.__balance = 0
# print(rafsan.__balance)
print(rafsan.getAccNum())
print(rafsan.getBalance())
print(rafsan._account_number)