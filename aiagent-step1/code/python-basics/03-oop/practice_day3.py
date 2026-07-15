"""
Day 3 练习：面向对象编程

说明：本文件只有练习题，没有答案。
      请参考 oop.py 查看示例和答案。
"""


# ================================
# 练习 1：创建简单的类
# ================================

# TODO: 创建 Book 类，包含：
# - 属性：title, author, price
# - 构造函数 __init__
# - 方法 __str__ 返回字符串表示
# - 方法 get_info() 返回详细信息
class Book:
    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price

    def __str__(self) -> str:
        return f'Book title={self.title}, author={self.author}, price={self.price}'
    
    def get_info(self) -> str:
        return f'Book title={self.title}, author={self.author}, price={self.price}'

# TODO: 创建 Book 对象，测试方法
book = Book('金瓶梅', '罗贯中', 99.99)
print(f'book={book}')

# ================================
# 练习 2：属性装饰器
# ================================

# TODO: 创建 Product 类，包含：
# - 属性：name, price
# - 使用 @property 和 @price.setter 验证价格不能为负数
# - 方法 __str__
class Product:
    
    def __init__(self, name, price: float=0.0) -> None:
        self.name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负")
        self._price = value

# TODO: 创建 Product 对象，测试 setter
product = Product('脑白金', 999.99)
print(f'price = {product.price}')
product.price = 129.99
print(f'price = {product.price}')

# ================================
# 练习 3：继承
# ================================

# TODO: 创建 Animal 基类，包含：
# - 属性：name
# - 方法 speak()（抽象方法）
class Animal():

    def __init__(self, name) -> None:
        self._name = name
    
    def speak(self):
        raise NotImplemented('方法未实现')

# TODO: 创建 Dog 和 Cat 类继承 Animal，实现 speak()
class Dog(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self):
        print(f'小狗{self._name}汪汪汪～')

class Cat(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self):
        print(f'小猫{self._name}喵喵喵～')

# TODO: 测试多态
a = Animal('野兽甲')
# a.speak()
a1 = Dog('丹尼')
a2 = Cat('凯蒂')
a1.speak()
a2.speak()

# ================================
# 练习 4：类方法和静态方法
# ================================

# TODO: 创建 Calculator 类，包含：
# - 类属性：version
# - 类方法：get_version()
# - 静态方法：add(a, b)
class Calculator:

    version = '1.0'

    @classmethod
    def get_version(cls):
        return Calculator.version
    
    @staticmethod
    def add(a, b) -> float:
        return a+b

# TODO: 测试类方法和静态方法
print(f'{Calculator.get_version()}')
print(f'result = {Calculator.add(1,2)}')

# ================================
# 练习 5：抽象类
# ================================

# TODO: 创建 Shape 抽象类，包含：
# - 抽象方法：area(), perimeter()
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# TODO: 创建 Circle 类继承 Shape，实现抽象方法
class Circle(Shape):

    def __init__(self, r) -> None:
        super().__init__()
        self._r = r

    def area(self):
        return 3.14 * self._r ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self._r

# TODO: 创建 Rectangle 类继承 Shape，实现抽象方法
class Rectangle(Shape):

    def __init__(self, chang, kuan) -> None:
        super().__init__()
        self._chang = chang
        self._kuan = kuan

    def area(self):
        return self._chang * self._kuan
    
    def perimeter(self):
        return (self._chang + self._kuan) * 2


# ================================
# 练习 6：魔法方法
# ================================

# TODO: 创建 Money 类，包含：
# - 属性：amount, currency
# - 方法 __add__：加法运算
# - 方法 __eq__：相等比较
# - 方法 __str__：字符串表示
class Money:

    def __init__(self, amount, currency) -> None:
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        new_amount = self.amount + other.amount
        return Money(new_amount, self.currency)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Money):
            return False
        return self.amount == value.amount and self.currency == value.currency
    
    def __str__(self) -> str:
        return f'Money: amount = {self.amount}, currency = {self.currency}'


# TODO: 测试魔法方法
money0 = Money(19999999.99, 'dollar')
money1 = Money(19999999.99, 'dollar')
money2 = Money(19999999.99, 'RMB')
new_money0 = money0 + money1
print(f'new_money0 == {new_money0}')
print(f'money0==money1 is {money0==money1}, money0==money2 is {money0==money2}')
print(f'money0 = {money0}')

# ================================
# 验证区域
# ================================

print("\n" + "="*60)
print("Day 3 练习验证")
print("="*60)

# 在这里添加验证代码

print("\n✅ 完成所有练习后，取消上面的注释并运行！")