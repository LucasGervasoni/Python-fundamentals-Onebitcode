class Product:
    def __init__(self, name, price):
        self.price = price
        self.name = name
    
    def __str__(self):
        return f'Produto: {self.name} \nPreço: {self.price}'
    
    def Discount(self, perc_discount):
        valueDiscount = (self.price/100) * perc_discount
        finalPrice = self.price - valueDiscount
        return int(finalPrice)
    
mac = Product('Mac', 8300)
print(mac)
print(mac.Discount(15))
