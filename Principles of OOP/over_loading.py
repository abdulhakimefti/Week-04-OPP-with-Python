def add(num1,num2,num3,num4=0):
    return num1+num2+num3+num4

print(add(2,34,5))
print(add(4,4,2,2))

class Account:
    def __init__(self,holder,balance):
        self.holder = holder
        self.balance= balance
    def __add__(self,other):
        return self.balance+other.balance
my_account =  Account('sakib',50000)
her_account= Account('sishir',3290)

print(my_account+her_account)