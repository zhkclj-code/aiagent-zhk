"""
Day 1 练习：Python 语法对比（Python vs Java）

说明：本文件只有练习题，没有答案。
      请参考 python_vs_java.py 查看示例和答案。

练习方法：
1. 阅读 python_vs_java.py 理解语法
2. 在本文件中编写代码完成练习
3. 运行本文件验证结果
"""

# ================================
# 练习 1：变量和类型
# ================================

# TODO: 创建三个变量，分别存储：
# - 你的姓名（字符串）
# - 你的年龄（整数）
# - 你的 Python 学习天数（整数，比如 0）
name = "阿朱"
age = 18
python = 1


# TODO: 使用 print() 和 f-string 打印这些变量
print(f"my name is {name}, age is {age}, python study days is {python}")


# ================================
# 练习 2：数据结构
# ================================

# TODO: 创建一个列表，包含 5 个你喜欢的水果名称
friuts = ["apple", "banana", "orange", "grape", "watermelon"]

# TODO: 创建一个字典，存储你的个人信息（姓名、年龄、城市）
personal_info = {"age": 18, "name": "阿朱", "city": "北京"}


# TODO: 创建一个元组，包含三个数字（1, 2, 3）
numbers = (1, 2, 3)

# TODO: 创建一个集合，包含 1, 2, 3, 3, 3，观察去重效果
set_example = {1, 2, 3, 3, 3}
print(f"集合（自动去重）: {set_example}")

# ================================
# 练习 3：函数定义
# ================================


# TODO: 定义一个函数 calculate_average，接收两个参数 a 和 b，返回平均值
def calculate_average(a, b):
    return (a + b) / 2


# TODO: 定义一个函数 greet，接收一个参数 name（默认值为"朋友"），返回问候语
def greet(name: str = "朋友"):
    return f"你好 {name}"


# TODO: 定义一个函数 sum_all，使用可变参数 *args，返回所有参数的和
def sum_all(*args):
    result = 0
    for num in args:
        result += num

    return result


# ================================
# 练习 4：条件判断
# ================================


# TODO: 编写代码，判断年龄是否成年（>=18）
def is_adult(age):
    if age < 18:
        print("未成年")
    else:
        print("已成年")


# TODO: 编写代码，根据成绩判断等级：
# - >= 90: 优秀
# - >= 80: 良好
# - >= 60: 及格
# - < 60: 不及格
def get_level(score):
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")


# ================================
# 练习 5：循环
# ================================

# TODO: 使用 for 循环打印 1-10
for item in range(1, 11):
    print(item)

# TODO: 使用 for 循环遍历水果列表，打印每个水果
for fruit in friuts:
    print(fruit)

# TODO: 使用 enumerate 同时打印索引和水果名称
for index, fruit in enumerate(friuts):
    print(f"{index}号水果：{fruit}")

# ================================
# 练习 6：类定义
# ================================


# TODO: 定义一个类 Student，包含：
# - 属性：name, age, grade
# - 构造函数 __init__
# - 方法 introduce() 返回自我介绍
class Student:

    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"my name is {self.name}, 今年{self.age}岁，上{self.grade}年级")


# TODO: 创建一个 Student 对象，调用 introduce() 方法
student = Student("小猪猪", 13, 9)
methed = student.introduce
print(f"methed = {methed}")
student.introduce()

# ================================
# 练习 7：异常处理
# ================================

# TODO: 编写代码，尝试计算 10 / 0，捕获 ZeroDivisionError 异常
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"捕获异常{e}")
finally:
    print("资源回收")

# ================================
# 综合练习
# ================================


# TODO: 定义一个类 Calculator，包含：
# - 方法 add(a, b)：加法
# - 方法 subtract(a, b)：减法
# - 方法 multiply(a, b)：乘法
# - 方法 divide(a, b)：除法（处理除零异常）
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            print(f"除数不能为0，{e}")


# TODO: 创建 Calculator 对象，测试所有方法
cal = Calculator()
rst_add = cal.add(1, 2)
rst_sub = cal.subtract(1, 2)
rst_mul = cal.multiply(1, 2)
rst_dev = cal.divide(1, 2)
print(f"add={rst_add}, sub= {rst_sub}, mul= {rst_mul}, dev= {rst_dev}")


# ================================
# 验证区域
# ================================

print("\n" + "=" * 60)
print("Day 1 练习验证")
print("=" * 60)

# 在这里添加验证代码
# 例如：
# print(f"练习 1: 姓名={name}, 年龄={age}")
# print(f"练习 3: 平均值={calculate_average(10, 20)}")
# print(f"练习 6: {student.introduce()}")

print("\n✅ 完成所有练习后，取消上面的注释并运行！")
