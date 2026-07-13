"""
Day 3: 面向对象编程（Python 风格）

学习目标：掌握 Python 的面向对象编程特性
"""

# ================================
# 1. 类定义基础
# ================================

# Java 写法：
# public class Person {
#     private String name;
#     private int age;
#
#     public Person(String name, int age) {
#         this.name = name;
#         this.age = age;
#     }
#
#     public String getName() {
#         return name;
#     }
#
#     public void setName(String name) {
#         this.name = name;
#     }
#
#     @Override
#     public String toString() {
#         return "Person{name='" + name + "', age=" + age + "}";
#     }
# }

# Python 写法：
class Person:
    """人员类"""

    def __init__(self, name: str, age: int):
        """构造函数"""
        self.name = name  # 公有属性
        self._age = age   # 私有属性约定（单下划线）

    def __str__(self) -> str:
        """字符串表示（类似 Java toString）"""
        return f"Person(name={self.name}, age={self._age})"

    def introduce(self) -> str:
        """自我介绍"""
        return f"我是 {self.name}，今年 {self._age} 岁"


# 创建对象
person = Person("张三", 25)
print(person)
print(person.introduce())


# ================================
# 2. 属性装饰器
# ================================

class Student:
    """学生类（使用属性装饰器）"""

    def __init__(self, name: str, score: float):
        self.name = name
        self._score = score

    @property
    def score(self) -> float:
        """获取成绩"""
        return self._score

    @score.setter
    def score(self, value: float):
        """设置成绩（带验证）"""
        if value < 0 or value > 100:
            raise ValueError("成绩必须在 0-100 之间")
        self._score = value

    @score.deleter
    def score(self):
        """删除成绩"""
        del self._score


student = Student("李四", 85)
print(f"学生姓名: {student.name}")
print(f"学生成绩: {student.score}")

# 修改成绩（自动验证）
student.score = 90
print(f"修改后成绩: {student.score}")

# 尝试设置无效成绩（会抛出异常）
try:
    student.score = 150
except ValueError as e:
    print(f"错误: {e}")


# ================================
# 3. 继承
# ================================

# Java 写法：
# public class GraduateStudent extends Person {
#     private String thesis;
#
#     public GraduateStudent(String name, int age, String thesis) {
#         super(name, age);
#         this.thesis = thesis;
#     }
# }

# Python 写法：
class GraduateStudent(Person):
    """研究生类（继承 Person）"""

    def __init__(self, name: str, age: int, thesis: str):
        """构造函数"""
        super().__init__(name, age)  # 调用父类构造函数
        self.thesis = thesis

    def __str__(self) -> str:
        """重写字符串表示"""
        return f"GraduateStudent(name={self.name}, age={self._age}, thesis={self.thesis})"

    def defend(self) -> str:
        """答辩方法"""
        return f"{self.name} 正在答辩论文：{self.thesis}"


grad = GraduateStudent("王五", 28, "深度学习在NLP中的应用")
print(grad)
print(grad.defend())


# ================================
# 4. 多态和方法重写
# ================================

class Animal:
    """动物基类"""

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        """发声方法（抽象方法）"""
        raise NotImplementedError("子类必须实现此方法")


class Dog(Animal):
    """狗类"""

    def speak(self) -> str:
        """重写发声方法"""
        return f"{self.name}: 汪汪汪！"


class Cat(Animal):
    """猫类"""

    def speak(self) -> str:
        """重写发声方法"""
        return f"{self.name}: 喵喵喵！"


# 多态
animals = [Dog("小黑"), Cat("小白")]
for animal in animals:
    print(animal.speak())


# ================================
# 5. 类方法和静态方法
# ================================

class MathUtils:
    """数学工具类"""

    version = "1.0"  # 类属性

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def get_version(cls) -> str:
        """类方法（类似 Java static）"""
        return f"MathUtils 版本: {cls.version}"

    @staticmethod
    def add(a: int, b: int) -> int:
        """静态方法（类似 Java static）"""
        return a + b


print(MathUtils.get_version())
print(f"静态方法: {MathUtils.add(3, 5)}")


# ================================
# 6. 魔法方法
# ================================

class Vector:
    """向量类（演示魔法方法）"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """字符串表示"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        """调试表示"""
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other: 'Vector') -> 'Vector':
        """重载 + 运算符"""
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        """重载 == 运算符"""
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        """重载 len()"""
        return 2


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f"向量加法: {v1 + v2}")
print(f"向量比较: {v1 == v2}")
print(f"向量长度: {len(v1)}")


# ================================
# 7. 抽象类
# ================================

from abc import ABC, abstractmethod

# Java 写法：
# public abstract class Shape {
#     public abstract double area();
# }

# Python 写法：
class Shape(ABC):
    """形状抽象类"""

    @abstractmethod
    def area(self) -> float:
        """计算面积（抽象方法）"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """计算周长（抽象方法）"""
        pass


class Rectangle(Shape):
    """矩形类"""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """计算面积"""
        return self.width * self.height

    def perimeter(self) -> float:
        """计算周长"""
        return 2 * (self.width + self.height)


rect = Rectangle(5, 3)
print(f"矩形面积: {rect.area()}")
print(f"矩形周长: {rect.perimeter()}")


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)

# 练习 1：创建 Book 类
class Book:
    """图书类"""

    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self._price = price

    @property
    def price(self) -> float:
        """获取价格"""
        return self._price

    @price.setter
    def price(self, value: float):
        """设置价格（验证）"""
        if value < 0:
            raise ValueError("价格不能为负数")
        self._price = value

    def __str__(self) -> str:
        return f"《{self.title}》- {self.author} (${self.price})"


book = Book("Python编程", "Eric Matthes", 59.9)
print(f"练习 1 - 图书: {book}")


# 练习 2：创建继承类
class EBook(Book):
    """电子书类（继承 Book）"""

    def __init__(self, title: str, author: str, price: float, format: str):
        super().__init__(title, author, price)
        self.format = format

    def __str__(self) -> str:
        return f"《{self.title}》- {self.author} (${self.price}) [{self.format}]"


ebook = EBook("流畅的Python", "Luciano Ramalho", 99.9, "PDF")
print(f"练习 2 - 电子书: {ebook}")


# 练习 3：创建抽象类
class Employee(ABC):
    """员工抽象类"""

    def __init__(self, name: str, base_salary: float):
        self.name = name
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self) -> float:
        """计算工资"""
        pass


class Manager(Employee):
    """经理类"""

    def __init__(self, name: str, base_salary: float, bonus: float):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.base_salary + self.bonus


manager = Manager("张经理", 10000, 5000)
print(f"练习 3 - 经理工资: {manager.calculate_salary()}")


print("\n✅ Day 3 学习完成！")
print("要点总结：")
print("1. Python 用 __init__ 构造函数，无 this")
print("2. Python 用 @property 装饰器实现 getter/setter")
print("3. Python 用 super().__init__() 调用父类构造函数")
print("4. Python 用 ABC 和 @abstractmethod 定义抽象类")
print("5. Python 用 __add__、__eq__ 等魔法方法重载运算符")