"""
Day 10: 类型注解练习

学习目标：掌握 Python 类型注解和 Pydantic
"""


# ================================
# 练习 1：基础类型注解
# ================================
"""
任务：为以下函数添加类型注解：

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def get_first(items):
    return items[0] if items else None

要求：
1. 参数类型
2. 返回值类型
3. 使用 typing 模块
"""

# TODO: 在这里为函数添加类型注解




# ================================
# 练习 2：容器类型注解
# ================================
"""
任务：使用容器类型注解：

1. List、Dict、Tuple、Set 的类型注解
2. Optional 表示可选值
3. Union 表示联合类型

示例：
def process_users(users: List[Dict[str, Any]]) -> List[str]:
    return [user["name"] for user in users]

要求：
创建以下函数并添加类型注解：
1. get_user_names(users: List[Dict]) -> List[str]
2. find_user_by_id(users: List[Dict], user_id: int) -> Optional[Dict]
3. format_user(user: Dict[str, Union[str, int]]) -> str
"""

# TODO: 在这里实现带类型注解的函数




# ================================
# 练习 3：自定义类型（TypeAlias）
# ================================
"""
任务：创建自定义类型别名：

1. UserId = int
2. UserName = str
3. User = Dict[str, Union[UserId, UserName, int]]
4. Users = List[User]

然后创建函数：
def create_user(id: UserId, name: UserName, age: int) -> User:
    return {"id": id, "name": name, "age": age}

def get_adults(users: Users) -> Users:
    return [user for user in users if user["age"] >= 18]
"""

# TODO: 在这里创建类型别名和函数




# ================================
# 练习 4：Pydantic 数据模型
# ================================
"""
任务：使用 Pydantic 创建数据模型：

1. User 模型：
   - id: int
   - name: str
   - email: str（验证邮箱格式）
   - age: int（范围 0-150）

2. Product 模型：
   - id: int
   - name: str
   - price: float（正数）
   - tags: List[str]

3. Order 模型：
   - id: int
   - user: User
   - products: List[Product]
   - total_price: float（自动计算）

测试代码：
user = User(id=1, name="张三", email="zhangsan@example.com", age=25)
print(user)

product = Product(id=1, name="Python书", price=99.9, tags=["编程", "书籍"])
print(product)

order = Order(id=1, user=user, products=[product], total_price=99.9)
print(order)
"""

# TODO: 在这里实现 Pydantic 模型




# ================================
# 练习 5：Pydantic 验证器
# ================================
"""
任务：创建带验证器的 Pydantic 模型：

1. User 模型：
   - name：不能为空
   - email：必须是有效邮箱格式
   - age：范围 0-150
   - phone：必须是 11 位数字（可选）

2. 使用 @validator 装饰器：
   - 自定义验证逻辑
   - 错误消息

测试代码：
# 正常情况
user = User(name="张三", email="test@example.com", age=25)
print(user)

# 异常情况
try:
    user = User(name="", email="invalid", age=200)
except ValidationError as e:
    print(e)
"""

# TODO: 在这里实现带验证器的模型




# ================================
# 练习 6：Pydantic 配置
# ================================
"""
任务：配置 Pydantic 模型：

1. User 模型：
   - 使用 Config 类配置
   - orm_mode = True（支持 ORM 对象）
   - use_enum_values = True
   - validate_assignment = True（修改属性时验证）

2. 嵌套模型：
   - Address 模型
   - User 包含 Address

测试代码：
user_dict = {"name": "张三", "email": "test@example.com", "age": 25}
user = User(**user_dict)
print(user)

user.age = 200  # 应该抛出验证错误
"""

# TODO: 在这里实现配置化的 Pydantic 模型




# ================================
# 练习 7：类型守卫（Type Guard）
# ================================
"""
任务：实现类型守卫函数：

功能：
1. is_user(obj) -> TypeGuard[User]：
   - 判断对象是否为 User 类型
   - 用于类型检查器

2. is_valid_email(email: str) -> bool：
   - 验证邮箱格式

测试代码：
def process(obj: Any) -> None:
    if is_user(obj):
        # 这里 obj 被识别为 User 类型
        print(obj.name)
"""

# TODO: 在这里实现类型守卫函数




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    from typing import List, Dict, Optional, Union, Any
    from pydantic import BaseModel, ValidationError, validator
    
    print("=" * 60)
    print("Day 10 练习验证 - 类型注解和 Pydantic")
    print("=" * 60)
    
    # 测试练习 1
    print("\n--- 练习 1：基础类型注解 ---")
    # print(greet("张三"))
    # print(add(3, 5))
    
    # 测试练习 4
    print("\n--- 练习 4：Pydantic 模型 ---")
    # user = User(id=1, name="张三", email="test@example.com", age=25)
    # print(user)
    
    # 测试练习 5
    print("\n--- 练习 5：Pydantic 验证器 ---")
    # try:
    #     user = User(name="", email="invalid", age=200)
    # except ValidationError as e:
    #     print(f"验证错误: {e}")
    
    print("\n✅ Day 10 练习完成！")
    print("重点：类型注解、Pydantic、验证器、类型守卫")