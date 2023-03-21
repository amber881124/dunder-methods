class Product: # class名稱第一字要大寫
    # 初始化
    def __init__(self, name, price):
        self.name = name # property
        self.price = price # property

    # 怎麼print(預設.簡單版)
    def __str__(self):
        return f'{self.name} ${self.price}'

    # 怎麼print(詳細.debug用)
    def __repr__(self):
        return f'<Product({self.name}, {self.price})>'

    # 遇到 + 的反應    
    def __add__(self, other):
        if isinstance(other, Product):
            return [self, other]
        if isinstance(other, str):
            self.name += other

    # 遇到 * 的反應
    def __mul__(self, other):
        mul = []
        for _ in range(other):
            mul.append(self)
        return mul    


p1 = Product('巧克力冰淇淋麵包', 60)
p2 = Product('草莓大理石蛋糕', 75)
p1 + '魔法'
# print(p1) # 巧克力冰淇淋麵包魔法 $60
# print(repr(p1)) # <Product(巧克力冰淇淋麵包魔法, 60)>
# print(p1 + p2) # [<Product(巧克力冰淇淋麵包魔法, 60)>, <Product(草莓大理石蛋糕, 75)>]
# print(p2 * 3) # [<Product(草莓大理石蛋糕, 75)>, <Product(草莓大理石蛋糕, 75)>, <Product(草莓大理石蛋糕, 75)>]


class ShoppingCart:
    def __init__(self, product):
        self.product = product

    def __getitem__(self, key):
        return self.product[key]

s = ShoppingCart([p1, p2])
print(s[1]) # 草莓大理石蛋糕 $75
# 如果沒寫__getitem__會變: 'ShoppingCart' object is not subscriptable(可訂閱)