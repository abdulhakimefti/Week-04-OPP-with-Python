# public 
# protected
#private 

class Account:
    pass

class StudentAccount(Account):
    def __init__(self,holder,balance,school):
        self.__balance= balance
    def withdraw(self,amount):
        if amount> self.__balance:
            return 'No money'
        self.__balance-=amount
    def deposit(self,amount):
        if amount < 0 :
            return 'Negative amount'
        self.__balance+=amount
    def getBalance(self):
        return self.__balance

nas  = StudentAccount('nas daily',12000,'Nas Academy')
print(nas.getBalance())
nas._StudentAccount__balance=204999
print(nas.getBalance())
# print(dir(nas))