class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)
    def show_info(self):
        print(f'{self.name}, {self.price}')

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        self.price = self.price - discount

price1 = Product('Хлеб', 100)
price2 = Product('Молоко', 150)
price3 = Product('Колбаса', 200)

price1.apply_discount(10)
price3.apply_discount(20)
price1.show_info()
price2.show_info()
price3.show_info()