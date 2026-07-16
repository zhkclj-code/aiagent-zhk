"""
Day 10: 类型注解（Type Hints）

学习目标：掌握 Python 类型注解系统
"""

# ================================
# 0. 类型注解核心概念 - Java开发者必读
# ================================

"""
【⚠️ 关键警告：Python类型注解运行时不检查！】

Python类型注解是**静态提示**，运行时**不强制检查**！

# Java（编译时检查 + 运行时检查）
String name = 123;  // 编译错误！类型不匹配

# Python（运行时不检查）
name: str = 123  # 运行正常！但mypy会报静态错误
print(type(name))  # 输出: <class 'int'>

【和Java强类型系统的本质区别】

| 特性 | Java | Python |
|-----|------|--------|
| 类型检查时机 | 编译时（强制） | 静态分析时（可选） |
| 运行时检查 | 强制类型安全 | 不检查 |
| 类型擦除 | 否 | 是（运行时注解可被忽略） |
| IDE支持 | 完整 | 部分依赖类型注解 |
| 错误后果 | 编译失败 | 运行时可能出错 |

【为什么Python需要类型注解？】

1. IDE智能提示和自动补全（VS Code、PyCharm）
2. 静态检查发现潜在错误（mypy、pyright）
3. 代码文档和可读性（函数签名即文档）
4. 团队协作规范（大型项目必需）
5. 重构工具支持（安全重命名、类型感知重构）

【工具配置】

# 安装mypy
pip install mypy

# 运行类型检查
mypy your_script.py

# VS Code配置（settings.json）
{
    "python.analysis.typeCheckingMode": "basic"
}

# pyproject.toml配置
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true

【类型注解的工作原理】

def greet(name: str) -> str:
    return f"Hello, {name}"

# 运行时：name: str 只是注解，存储在 __annotations__
print(greet.__annotations__)  # {'name': <class 'str'>, 'return': <class 'str'>}

# 运行时：类型注解不影响执行
greet(123)  # 正常运行！返回 "Hello, 123"

# 静态检查时：mypy会发现类型错误
# mypy output: error: Argument 1 to "greet" has incompatible type "int"; expected "str"

【常见陷阱】

1. 类型注解不等于类型强制
   value: int = "string"  # mypy报错，但运行正常

2. Optional vs None
   def func(x: Optional[str]): pass
   func(None)  # 正确
   func(123)   # mypy报错，但运行正常

3. 泛型类型需要导入
   from typing import List, Dict, Optional

4. 类型别名需要TypeAlias
   from typing import TypeAlias
   UserId: TypeAlias = int  # Python 3.10+

【最佳实践】

1. 公共API必须添加类型注解（函数签名、参数、返回值）
2. 使用mypy进行静态检查（CI/CD集成）
3. 复杂类型定义类型别名
4. 使用Protocol代替抽象基类（鸭子类型）
5. 结合Pydantic做运行时验证（API数据验证）

【Java开发者迁移建议】

Java类型 → Python类型注解
───────────────────────────────
String → str
int → int
boolean → bool
List<String> → list[str] 或 List[str]
Map<K,V> → dict[K, V] 或 Dict[K, V]
Optional<T> → Optional[T] 或 T | None (3.10+)
Object → Any
void → None

Java注解 → Python类型注解
───────────────────────────────
@NotNull → 不需要（默认可None）
@Nullable → Optional[T]
@Override → 无对应（装饰器）
@interface → typing.Protocol 或 typing.TypedDict
"""

# ================================
# 1. 基础类型注解
# ================================

# Java 类型声明：
# String name = "张三";
# int age = 25;
# boolean isActive = true;

# Python 类型注解：
name: str = "张三"
age: int = 25
price: float = 99.9
is_active: bool = True

print(f"基础类型: name={name}, age={age}, price={price}, is_active={is_active}")


# ================================
# 2. 函数类型注解
# ================================

# Java 方法声明：
# public static int add(int a, int b) {
#     return a + b;
# }

# Python 函数类型注解：
def add(a: int, b: int) -> int:
    """加法函数"""
    return a + b


def greet(name: str, age: int = 25) -> str:
    """带默认参数的函数"""
    return f"你好，{name}，今年 {age} 岁"


# 可选类型（Optional）
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    """查找用户（可能返回 None）"""
    if user_id > 0:
        return f"用户{user_id}"
    return None


result = find_user(1)
print(f"查找结果: {result}")


# ================================
# 3. 容器类型注解
# ================================

from typing import List, Dict, Set, Tuple

# 列表类型
numbers: List[int] = [1, 2, 3, 4, 5]
names: List[str] = ["张三", "李四", "王五"]

# 字典类型
user_scores: Dict[str, int] = {
    "张三": 85,
    "李四": 92,
    "王五": 78
}

# 集合类型
unique_numbers: Set[int] = {1, 2, 3, 4, 5}

# 元组类型
point: Tuple[int, int] = (10, 20)

print(f"列表: {numbers}")
print(f"字典: {user_scores}")
print(f"集合: {unique_numbers}")
print(f"元组: {point}")


# ================================
# 4. 复杂类型注解
# ================================

from typing import Union, Any

# 联合类型（Union）
def process_data(data: Union[int, str, float]) -> str:
    """处理多种类型的数据"""
    return str(data)


# Python 3.10+ 新语法（类型联合运算符）
def process_data_new(data: int | str | float) -> str:
    """使用 | 运算符的联合类型"""
    return str(data)


# Any 类型（任意类型）
def flexible_function(data: Any) -> Any:
    """接受任意类型"""
    return data


# ================================
# 5. 自定义类型别名
# ================================

from typing import TypeAlias

# 类型别名
UserId: TypeAlias = int
UserName: TypeAlias = str
UserScore: TypeAlias = float

# 使用类型别名
def get_user_score(user_id: UserId) -> UserScore:
    """获取用户分数"""
    return 85.5


# 字典类型别名
JsonDict: TypeAlias = Dict[str, Any]

def parse_json(data: JsonDict) -> JsonDict:
    """解析 JSON 数据"""
    return {"parsed": True, "data": data}


# ================================
# 6. 类的类型注解
# ================================

class User:
    """用户类（带类型注解）"""
    
    def __init__(self, name: str, age: int, email: str):
        self.name: str = name
        self.age: int = age
        self.email: str = email
    
    def introduce(self) -> str:
        """自我介绍"""
        return f"我是 {self.name}，今年 {self.age} 岁"
    
    def update_email(self, new_email: str) -> None:
        """更新邮箱"""
        self.email = new_email


# 使用类型注解的类
user: User = User("张三", 25, "zhangsan@example.com")
print(user.introduce())


# ================================
# 7. 泛型类型注解
# ================================

from typing import TypeVar, Generic, Sequence

# 定义类型变量
T = TypeVar('T')

# 泛型容器类
class Container(Generic[T]):
    """泛型容器"""
    
    def __init__(self, value: T):
        self.value: T = value
    
    def get_value(self) -> T:
        return self.value
    
    def set_value(self, value: T) -> None:
        self.value = value


# 使用泛型容器
int_container: Container[int] = Container(42)
str_container: Container[str] = Container("Hello")

print(f"整型容器: {int_container.get_value()}")
print(f"字符串容器: {str_container.get_value()}")


# 泛型函数
def get_first_item(items: Sequence[T]) -> T:
    """获取序列的第一个元素"""
    return items[0]


first_number: int = get_first_item([1, 2, 3])
first_name: str = get_first_item(["张三", "李四"])

print(f"第一个数字: {first_number}")
print(f"第一个名字: {first_name}")


# ================================
# 8. 协议（Protocol）
# ================================

from typing import Protocol

# 定义协议（类似 Java 接口）
class Drawable(Protocol):
    """可绘制协议"""
    
    def draw(self) -> str:
        """绘制方法"""
        ...


class Circle:
    """圆形类（实现 Drawable 协议）"""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"绘制半径为 {self.radius} 的圆形"


class Square:
    """正方形类（实现 Drawable 协议）"""
    
    def __init__(self, side: float):
        self.side = side
    
    def draw(self) -> str:
        return f"绘制边长为 {self.side} 的正方形"


def render(shape: Drawable) -> str:
    """渲染形状"""
    return shape.draw()


circle = Circle(5.0)
square = Square(3.0)

print(render(circle))
print(render(square))


# ================================
# 9. 类型守卫（Type Guard）
# ================================

from typing import TypeGuard

def is_string_list(value: list) -> TypeGuard[List[str]]:
    """判断是否为字符串列表"""
    return all(isinstance(item, str) for item in value)


def process_items(items: list) -> None:
    """处理项目列表"""
    if is_string_list(items):
        # 类型推断：items 是 List[str]
        print(f"字符串列表: {items}")
    else:
        print(f"其他类型列表: {items}")


process_items(["张三", "李四"])
process_items([1, 2, 3])


# ================================
# 10. Pydantic 数据验证
# ================================

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import List

class UserPydantic(BaseModel):
    """使用 Pydantic 的用户模型"""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "张三",
                "age": 25,
                "email": "zhangsan@example.com",
                "tags": ["Python", "AI"],
            }
        }
    )

    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=150)
    email: EmailStr
    tags: List[str] = Field(default_factory=list)


# 创建用户（自动验证）
try:
    user_pydantic = UserPydantic(
        name="张三",
        age=25,
        email="zhangsan@example.com",
        tags=["Python", "AI"]
    )
    print(f"\nPydantic 用户: {user_pydantic}")
    print(f"JSON: {user_pydantic.model_dump_json()}")
except Exception as e:
    print(f"验证失败: {e}")


# ================================
# 11. 类型检查工具
# ================================

# mypy：静态类型检查工具
# 安装：pip install mypy
# 使用：mypy your_script.py

# pyright：微软类型检查工具
# 安装：pip install pyright
# 使用：pyright your_script.py

# VS Code 集成：
# "python.analysis.typeCheckingMode": "basic"


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)


# 练习 1：为函数添加类型注解
def calculate_average(numbers: List[float]) -> float:
    """计算平均值"""
    return sum(numbers) / len(numbers) if numbers else 0.0

print(f"练习 1 - 平均值: {calculate_average([1.0, 2.0, 3.0])}")


# 练习 2：创建带类型注解的类
class BankAccount:
    """银行账户类"""
    
    def __init__(self, account_number: str, balance: float):
        self.account_number: str = account_number
        self.balance: float = balance
    
    def deposit(self, amount: float) -> None:
        """存款"""
        self.balance += amount
    
    def withdraw(self, amount: float) -> bool:
        """取款"""
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self) -> float:
        """获取余额"""
        return self.balance

account = BankAccount("123456", 1000.0)
account.deposit(500.0)
print(f"练习 2 - 账户余额: {account.get_balance()}")


# 练习 3：使用 Union 类型
def process_value(value: int | str | float) -> str:
    """处理多种类型的值"""
    if isinstance(value, int):
        return f"整数: {value}"
    elif isinstance(value, str):
        return f"字符串: {value}"
    else:
        return f"浮点数: {value}"

print(f"练习 3 - {process_value(42)}")
print(f"练习 3 - {process_value('hello')}")
print(f"练习 3 - {process_value(3.14)}")


# 练习 4：创建泛型类
class Stack(Generic[T]):
    """栈（泛型）"""
    
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        """入栈"""
        self.items.append(item)
    
    def pop(self) -> Optional[T]:
        """出栈"""
        return self.items.pop() if self.items else None
    
    def is_empty(self) -> bool:
        """是否为空"""
        return len(self.items) == 0

int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(f"练习 4 - 出栈: {int_stack.pop()}")


# 练习 5：使用 Pydantic 验证数据
class Product(BaseModel):
    """商品模型"""
    
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

try:
    product = Product(name="Python 书籍", price=99.9, quantity=10)
    print(f"练习 5 - 商品: {product.name}, 价格: {product.price}")
except Exception as e:
    print(f"验证失败: {e}")


print("\n✅ Day 10 学习完成！")
print("要点总结：")
print("1. 基础类型：str、int、float、bool")
print("2. 容器类型：List、Dict、Set、Tuple")
print("3. 联合类型：Union[A, B] 或 A | B（Python 3.10+）")
print("4. 可选类型：Optional[T] 等同于 T | None")
print("5. 类型别名：TypeAlias 简化复杂类型")
print("6. 泛型：TypeVar、Generic 创建泛型类")
print("7. 协议：Protocol 定义接口规范")
print("8. 类型守卫：TypeGuard 类型判断")
print("9. Pydantic：数据验证和序列化")
print("10. 类型检查：mypy、pyright 静态检查")
