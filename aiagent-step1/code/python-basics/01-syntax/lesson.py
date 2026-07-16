"""
Day 1: Python 语法对比（Python vs Java）

学习目标：理解 Python 和 Java 的语法差异
"""

# ================================
# 1. 变量和类型
# ================================

# Java 写法：
# String name = "张三";
# int age = 25;
# double price = 99.9;
# boolean isActive = true;

# Python 写法：
name = "张三"      # 自动推断为 str
age = 25          # 自动推断为 int
price = 99.9      # 自动推断为 float
is_active = True  # 布尔值（注意大写）

print(f"姓名: {name}, 年龄: {age}, 价格: {price}, 激活: {is_active}")


# ================================
# 2. 数据结构
# ================================

# Java List -> Python list
# List<String> list = new ArrayList<>();
# list.add("A");
# list.add("B");

# Python list
my_list = ["A", "B", "C"]
print(f"列表: {my_list}")
print(f"第一个元素: {my_list[0]}")
print(f"切片: {my_list[0:2]}")  # Java 没有切片

# Java Map -> Python dict
# Map<String, Integer> map = new HashMap<>();
# map.put("age", 25);

# Python dict
my_dict = {"name": "张三", "age": 25}
print(f"字典: {my_dict}")
print(f"姓名: {my_dict['name']}")

# Python tuple（不可变列表）
my_tuple = ("A", "B", "C")
print(f"元组: {my_tuple}")

# Python set（无序不重复集合）
my_set = {1, 2, 3, 3, 3}
print(f"集合（自动去重）: {my_set}")


# ================================
# 3. 函数定义
# ================================

# Java 写法：
# public static int add(int a, int b) {
#     return a + b;
# }

# Python 写法：
def add(a, b):
    """加法函数"""
    return a + b

result = add(3, 5)
print(f"函数调用: 3 + 5 = {result}")


# 带类型注解的函数（推荐）
def add_with_type(a: int, b: int) -> int:
    """带类型注解的加法函数"""
    return a + b


# 默认参数（Java 不支持）
def greet(name: str = "世界") -> str:
    """带默认参数的函数"""
    return f"你好, {name}!"

print(greet())        # 使用默认值
print(greet("张三"))  # 传入参数


# 可变参数（Java 用 ...）
def sum_all(*args) -> int:
    """可变参数"""
    total = 0
    for num in args:
        total += num
    return total

print(f"可变参数求和: {sum_all(1, 2, 3, 4, 5)}")


# 关键字参数（Java 不支持）
def create_user(**kwargs) -> dict:
    """关键字参数"""
    return kwargs

user = create_user(name="张三", age=25, city="北京")
print(f"关键字参数: {user}")


# ================================
# 4. 条件判断
# ================================

# Java 写法：
# if (age >= 18) {
#     System.out.println("成年人");
# } else {
#     System.out.println("未成年人");
# }

# Python 写法：
age = 20

if age >= 18:
    print("成年人")
else:
    print("未成年人")

# elif（Java 用 else if）
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")


# ================================
# 5. 循环
# ================================

# Java for 循环：
# for (int i = 0; i < 5; i++) {
#     System.out.println(i);
# }

# Python for 循环：
for i in range(5):
    print(f"循环 {i}")


# 遍历列表（Java 增强for）
# for (String item : list) {
#     System.out.println(item);
# }

fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"水果: {fruit}")


# 同时获取索引和值（Java 需要用索引）
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")


# ================================
# 6. 类定义
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
# }

# Python 写法：
class Person:
    """人员类"""

    def __init__(self, name: str, age: int):
        """构造函数"""
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """字符串表示（类似 Java toString）"""
        return f"Person(name={self.name}, age={self.age})"

    def introduce(self) -> str:
        """自我介绍"""
        return f"我是 {self.name}，今年 {self.age} 岁"


# 创建对象
person = Person("张三", 25)
print(person)
print(person.introduce())


# 继承
class Student(Person):
    """学生类（继承 Person）"""

    def __init__(self, name: str, age: int, grade: str):
        """构造函数"""
        super().__init__(name, age)  # 调用父类构造函数
        self.grade = grade

    def introduce(self) -> str:
        """重写父类方法"""
        return f"我是 {self.name}，今年 {self.age} 岁，{self.grade} 年级"


student = Student("李四", 18, "大一")
print(student.introduce())


# ================================
# 7. 异常处理
# ================================

# Java 写法：
# try {
#     int result = 10 / 0;
# } catch (ArithmeticException e) {
#     System.out.println("除零错误");
# } finally {
#     System.out.println("清理资源");
# }

# Python 写法：
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"捕获异常: {e}")
finally:
    print("清理资源")


# ================================
# 8. 文件操作
# ================================

# Java 写法：
# try (BufferedReader br = new BufferedReader(new FileReader("test.txt"))) {
#     String line;
#     while ((line = br.readLine()) != null) {
#         System.out.println(line);
#     }
# } catch (IOException e) {
#     e.printStackTrace();
# }

# Python 写法（with 语句自动管理资源）：
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    sample_file = Path(temp_dir) / "test.txt"
    sample_file.write_text("Python 文件操作示例", encoding="utf-8")
    with sample_file.open("r", encoding="utf-8") as f:
        content = f.read()
        print(content)


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)

# 练习 1：创建一个列表，包含 5 个数字，计算平均值
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"练习 1 - 平均值: {average}")


# 练习 2：创建一个字典，存储学生信息（姓名、年龄、成绩）
student_info = {
    "name": "王五",
    "age": 20,
    "score": 88
}
print(f"练习 2 - 学生信息: {student_info}")


# 练习 3：编写一个函数，判断数字是否为偶数
def is_even(num: int) -> bool:
    """判断是否为偶数"""
    return num % 2 == 0

print(f"练习 3 - 10 是偶数吗？{is_even(10)}")


# 练习 4：使用 for 循环打印 1-10 的平方
print("练习 4 - 1-10 的平方:")
for i in range(1, 11):
    print(f"  {i}² = {i**2}")


# 练习 5：创建一个类 Rectangle，计算面积和周长
class Rectangle:
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
print(f"练习 5 - 矩形面积: {rect.area()}, 周长: {rect.perimeter()}")

print("\n✅ Day 1 学习完成！")
print("要点总结：")
print("1. Python 是动态类型，变量无需声明类型")
print("2. Python 用缩进代替大括号，无分号")
print("3. Python 函数用 def 定义，支持默认参数和可变参数")
print("4. Python 类用 __init__ 构造函数，无 this")
print("5. Python 用 with 语句管理资源，自动清理")
