from dunder_methods import Product

class Drink(Product):
    def __init__(self, name, price, number):
        super().__init__(name, price) # super().__init__: 執行父母的__init__
        self.number = number

d = Drink('蘋果起司蛋糕', 120, 4)

Food = type('Food', (Product,), {})

# class Food(Product):
#     pass

f = Food('芒果布丁', 60)

if __name__ == '__main__':
    # print(d.number)
    # print(type(Drink))
    # print(type(Product))
    # print(type(d))
    # print(isinstance(type, object))
    # print(isinstance(type, type))
    # print(isinstance(d, Drink)) # d是不是Drink的實例
    # print(isinstance(d, Product)) 
    print(f)