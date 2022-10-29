#inheritance 
#base class will have only the common attributes and method
class Device:
    def __init__(self,brand,price,color) :
        self.brand = brand
        self.price = price
        self.color = color
    def re_sale(self):
        print('Ready to sell')

class Laptop(Device) :
    def __init__(self,brand,price,color,disc):
        super().__init__(brand,price,color)
        self.disc = disc
    
    def run(self):
        print('running the laptop')
    def __repr__(self) -> str:
        return f'laptop {self.brand} : {self.price} : {self.color}'
    def purchase(self,money):
        if money<self.price :
            return 'No Laptop  for you'
        else :
            print('This device is for you')
            return [self,money-self.price]
    

class Phone :
    def __init__(self,brand,price,color,camera,sim_num):
        self.brand= brand
        self.price=price
        self.color=color
        self.camera = camera
        self.sim_num=sim_num
    def __repr__(self) -> str:
        return f'laptop {self.brand} : {self.price} : {self.color}'
    def purchase(self,money):
        if money<self.price :
            return 'No Laptop  for you'
        else :
            print('This device is for you')
            return [self,money-self.price]
    def is_dual_sim(self):
        return self.sim_num
    
class Watch:
    def __init__(self,brand,price,color,watch_type):
        self.brand= brand
        self.price=price
        self.color=color
        self.watch_type = watch_type
    def purchase(self,money):
        if money<self.price :
            return 'No Laptop  for you'
        else :
            print('This device is for you')
            return [self,money-self.price]
    def isAnalog(self):
        return self.watch_type
    
class Manager :
    def __init__(self,name,salary,experience,designation):
        pass
    def day_total_sales(self):
        pass
    def handle_customer_complain(self):
        pass
class SalesPerson:
    def __init__(self,name,salary,experience,designation,commission):
        pass
    def handle_customer(self):
        pass

lenovo = Laptop('Lenovo',42000,'black','500gb')
hp = Laptop('hp',50000,'white','3204gb')
oppo = Phone('Oppo',15000,'black','15mp',2)
samsung = Phone('samsung',32000,'silver','48mp',1)
print(lenovo)
print(hp)
print(oppo)
print(samsung)
lenovo.re_sale()
print(hp.brand)