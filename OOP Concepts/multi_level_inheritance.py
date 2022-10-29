class Vehicle :
    def __init__(self,name,license,price):
        self.name = name
        self.license = license
        self.price = price
    def start(self):
        print(f'{self.name} started')
    
class Bus(Vehicle):
    def __init__(self,name,license,price,seat,ticketPrice):
        super().__init__(name,license,price)
        self.seat = seat
        self.availableSeat = seat
        self.ticketPrice = ticketPrice
    def sellTicket(self,customerName,quantity,amount):
        self.availableSeat  -= quantity
        remaining =amount- self.ticketPrice*quantity
        if amount >= remaining:
            return Ticket(customerName)
        return 'No ticket'

class ACBus(Bus):
    def __init__(self):
        print('ac bus created')
class MiniBus(Bus):
    def __init__(sefl):
        super().__init__('Mini Bus','CTG434',1200000,50,540)
        print('mini bus created')

class Ticket :
    def __init__(self,owner):
        self.owner = owner
    
mini = MiniBus()
print(mini.name)