"""
Day 4: 装饰器和上下文管理器

学习目标：理解 Python 装饰器和上下文管理器
"""

# ================================
# 1. 装饰器基础
# ================================

# 装饰器本质：修改其他函数功能的函数

def my_decorator(func):
    """简单装饰器"""
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

# 使用装饰器
@my_decorator
def say_hello():
    print("你好！")

say_hello()


# ================================
# 2. 带参数的装饰器
# ================================

def my_decorator_with_args(func):
    """带参数的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper

@my_decorator_with_args
def add(a: int, b: int) -> int:
    """加法函数"""
    return a + b

result = add(3, 5)
print(f"结果: {result}\n")


# ================================
# 3. 实际应用：计时装饰器
# ================================

import time

def timer(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    """慢函数"""
    time.sleep(1)
    return "完成"

print(slow_function())


# ================================
# 4. 内置装饰器
# ================================

class MyClass:
    """演示内置装饰器"""

    class_var = "类属性"

    def __init__(self, value: int):
        self.instance_var = value

    @staticmethod
    def static_method():
        """静态方法（类似 Java static）"""
        print("静态方法")

    @classmethod
    def class_method(cls):
        """类方法（第一个参数是类本身）"""
        print(f"类方法: {cls.class_var}")

    @property
    def value(self) -> int:
        """属性 getter"""
        return self._value

    @value.setter
    def value(self, val: int):
        """属性 setter"""
        if val < 0:
            raise ValueError("值不能为负数")
        self._value = val


obj = MyClass(10)
MyClass.static_method()
MyClass.class_method()


# ================================
# 5. 上下文管理器（with 语句）
# ================================

# Java 写法：
# try (BufferedReader br = new BufferedReader(new FileReader("test.txt"))) {
#     String line = br.readLine();
# } catch (IOException e) {
#     e.printStackTrace();
# }

# Python 写法：
# with open("test.txt", "r") as f:
#     content = f.read()


# ================================
# 6. 自定义上下文管理器
# ================================

class Timer:
    """计时上下文管理器"""

    def __enter__(self):
        """进入上下文"""
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        self.end = time.time()
        print(f"执行时间: {self.end - self.start:.4f}秒")
        return False  # 不抑制异常

# 使用自定义上下文管理器
with Timer():
    time.sleep(1)
    print("执行中...")


# ================================
# 7. contextlib 模块
# ================================

from contextlib import contextmanager

@contextmanager
def timer_context():
    """使用装饰器创建上下文管理器"""
    start = time.time()
    yield  # 返回控制权
    end = time.time()
    print(f"执行时间: {end - start:.4f}秒")

with timer_context():
    time.sleep(1)
    print("执行中...")


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)

# 练习 1：创建日志装饰器
def logger(func):
    """日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] 返回值: {result}")
        return result
    return wrapper

@logger
def multiply(a: int, b: int) -> int:
    return a * b

print(f"练习 1 - 乘法: {multiply(4, 5)}\n")


# 练习 2：创建验证装饰器
def validate_positive(func):
    """验证参数为正数"""
    def wrapper(*args):
        for arg in args:
            if arg < 0:
                raise ValueError("参数必须为正数")
        return func(*args)
    return wrapper

@validate_positive
def calculate_area(width: float, height: float) -> float:
    return width * height

try:
    print(f"练习 2 - 面积: {calculate_area(5, 3)}")
    calculate_area(-1, 5)  # 会抛出异常
except ValueError as e:
    print(f"练习 2 - 错误: {e}\n")


# 练习 3：创建数据库连接上下文管理器
class DatabaseConnection:
    """模拟数据库连接"""

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        """连接数据库"""
        print(f"连接数据库: {self.db_name}")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """关闭连接"""
        print(f"关闭数据库连接: {self.db_name}")
        self.connected = False
        return False

    def query(self, sql: str):
        """执行查询"""
        if not self.connected:
            raise RuntimeError("数据库未连接")
        print(f"执行查询: {sql}")

with DatabaseConnection("mydb") as db:
    db.query("SELECT * FROM users")

print("\n✅ Day 4 学习完成！")
print("要点总结：")
print("1. 装饰器是修改其他函数功能的函数")
print("2. @staticmethod、@classmethod、@property 是常用内置装饰器")
print("3. 上下文管理器用 __enter__ 和 __exit__ 实现")
print("4. with 语句自动管理资源，无需手动关闭")
print("5. @contextmanager 装饰器可以简化上下文管理器创建")