"""
Day 4: 装饰器和上下文管理器

学习目标：理解 Python 装饰器和上下文管理器
"""

# ================================
# 0. 装饰器核心概念 - Java开发者必读
# ================================

"""
【什么是装饰器】
装饰器是一个函数，接收一个函数作为参数，返回一个新的函数。
本质是语法糖：@decorator 等价于 func = decorator(func)

【装饰器执行时机】
⚠️ 关键：装饰器在函数定义时立即执行，而非函数调用时！
这和Java注解有本质区别：
- Java注解：只是标记，需要反射或框架（如Spring）在运行时解析处理
- Python装饰器：定义时立即执行的函数调用

示例：
@my_decorator
def func():
    pass
# 等价于：
# func = my_decorator(func)  <- 这行代码在函数定义时立即执行！

【和Java的对比】
| 维度 | Python装饰器 | Java注解 |
|-----|-------------|---------|
| 执行时机 | 函数定义时立即执行 | 运行时通过反射解析 |
| 本质 | 高阶函数（函数作为参数） | 元数据标记 |
| 灵活性 | 运行时动态修改行为 | 依赖框架处理 |
| 典型应用 | 日志、权限、缓存、计时 | @Override, @Autowired, @Test |

【使用场景】
✅ 适合用装饰器：
- 日志记录（自动记录函数调用）
- 权限验证（检查用户权限）
- 性能计时（测量执行时间）
- 缓存（memoization）
- 重试机制（失败自动重试）

❌ 不适合用装饰器：
- 简单的一次性逻辑
- 需要复杂参数配置的场景

【最佳实践】
1. 必须使用 @functools.wraps 保留原函数元信息
2. 装饰器应该只做一件事（单一职责）
3. 保持装饰器简单，复杂逻辑放在被装饰函数内
4. 为装饰器编写文档说明用途

【Java开发者迁移建议】
- Java @Before/@After → Python 装饰器
- Java AOP 切面 → Python 装饰器链
- Java 代理模式 → Python 装饰器 + 闭包
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
# 4. 内置装饰器 - Java开发者必读
# ================================

"""
【三种内置装饰器对比】

| 装饰器 | 第一个参数 | 用途 | Java对应 |
|--------|----------|------|---------|
| @staticmethod | 无特殊参数 | 工具方法，不访问实例 | static 方法 |
| @classmethod | cls（类本身） | 工厂方法、修改类状态 | 无直接对应（可用静态方法模拟） |
| @property | self（实例） | 属性访问控制（getter/setter） | getter/setter 方法 |

【和Java的详细对比】

@staticmethod：
- Python: @staticmethod 定义，可以类名.方法名() 调用
- Java: static 关键字定义，无需实例即可调用
- 相似度: 95%（几乎完全相同）

@classmethod：
- Python: @classmethod 第一个参数是类本身（cls），可以访问类属性
- Java: 无直接对应概念（Java没有"类方法"概念，只有静态方法）
- 应用: Python常用作工厂方法（替代构造函数重载）
- 示例: Date.from_timestamp(1234567890) 创建实例

@property：
- Python: @property + @attr.setter 实现属性访问控制
- Java: private字段 + public getter/setter方法
- 差异:
  - Python: 属性访问语法（obj.attr），但实际是方法调用
  - Java: 方法访问语法（obj.getAttr()）
- 优势: Python @property更简洁，支持计算属性、只读属性

【使用场景建议】

✅ @staticmethod:
- 纯工具函数（数学计算、字符串处理）
- 不需要访问实例或类状态

✅ @classmethod:
- 工厂方法（创建实例的替代构造函数）
- 修改类级别的状态（统计实例数量等）
- 继承链中需要访问子类

✅ @property:
- 属性访问控制（验证、转换）
- 计算属性（动态计算返回值）
- 只读属性（只定义getter）
- 延迟初始化（首次访问时计算）

【常见陷阱】
1. @property 不应有副作用（不要在getter里修改状态）
2. @classmethod 继承时，cls是实际调用的子类（不是基类）
3. @staticmethod 无法被重写（子类无法修改行为）
"""

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
# 5. 上下文管理器（with语句）- Java开发者必读
# ================================

"""
【什么是上下文管理器】
上下文管理器是一种资源管理协议，用于定义代码块执行前后的自动操作。
核心机制：自动调用 __enter__ 和 __exit__ 方法。

【和Java的对比】
| 维度 | Python with语句 | Java try-with-resources |
|-----|----------------|------------------------|
| 语法 | with obj as x: | try (Obj x = new Obj()) |
| 接口 | __enter__, __exit__ | 实现 AutoCloseable |
| 资源清理 | __exit__自动调用 | close()自动调用 |
| 异常处理 | __exit__接收异常信息 | catch块处理 |
| 返回值 | __enter__可返回值 | 无返回值 |

Java示例：
try (BufferedReader br = new BufferedReader(new FileReader("test.txt"))) {
    String line = br.readLine();  // 自动调用 br.close()
} catch (IOException e) {
    e.printStackTrace();
}

Python示例：
with open("test.txt", "r") as f:
    content = f.read()  # 自动调用 f.close()（无论是否异常）

【为什么需要上下文管理器】
1. 防止资源泄漏（忘记关闭文件、数据库连接、锁）
2. 异常安全（即使代码块抛出异常，也能正确清理）
3. 代码简洁（减少 try-finally 样板代码）
4. 统一的资源管理模式（所有资源用相同方式管理）

【执行流程】
with Timer() as t:
    ↓ (1) 调用 Timer.__enter__()
    ↓ (2) 将返回值赋给 t
    ↓ (3) 执行代码块
    ↓ (4) 调用 Timer.__exit__()（无论是否异常）

【使用场景】
✅ 必须用上下文管理器：
- 文件操作（open()）
- 数据库连接（自动提交/回滚）
- 线程锁（Lock, RLock）
- 计时器（性能测量）

✅ 建议用上下文管理器：
- 临时修改状态（如临时切换目录）
- 性能测量和日志记录
- 资源池管理（连接池）

【最佳实践】
1. 文件操作**必须**使用 with open()（不要手动close）
2. __exit__ 的三个参数：exc_type, exc_val, exc_tb（异常信息）
3. __exit__ 返回 True 会抑制异常，False 会传播异常（通常返回False）
4. 使用 @contextmanager 装饰器简化实现（第7节）

【Java开发者迁移建议】
- Java try-with-resources → Python with语句
- Java AutoCloseable → Python __enter__/__exit__
- Java Connection.close() → Python with connection:
"""

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
        print('开始执行')
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