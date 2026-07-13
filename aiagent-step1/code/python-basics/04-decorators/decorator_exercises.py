"""
Day 4: 装饰器和上下文管理器练习

学习目标：掌握装饰器和上下文管理器的使用
"""


# ================================
# 练习 1：简单装饰器
# ================================
"""
任务：创建一个 log_decorator 装饰器：

功能：
1. 在函数调用前打印："调用函数：{函数名}"
2. 在函数调用后打印："函数 {函数名} 执行完毕"
3. 打印执行时间（秒）

测试代码：
@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")
    time.sleep(1)

say_hello("张三")
"""

# TODO: 在这里实现 log_decorator 装饰器




# ================================
# 练习 2：带参数的装饰器
# ================================
"""
任务：创建一个 repeat 装饰器，重复执行函数 N 次：

功能：
1. 接收参数 n（重复次数）
2. 重复执行被装饰的函数 n 次
3. 打印每次执行的结果

测试代码：
@repeat(n=3)
def greet(name):
    return f"你好, {name}!"

result = greet("李四")
"""

# TODO: 在这里实现 repeat 装饰器




# ================================
# 练习 3：类装饰器
# ================================
"""
任务：创建一个 CountCalls 类装饰器：

功能：
1. 统计函数被调用的次数
2. 通过函数的 count 属性访问调用次数

测试代码：
@CountCalls
def add(a, b):
    return a + b

print(add(1, 2))
print(add(3, 4))
print(f"调用次数: {add.count}")  # 应该输出 2
"""

# TODO: 在这里实现 CountCalls 类装饰器




# ================================
# 练习 4：上下文管理器（with 语句）
# ================================
"""
任务：创建一个 Timer 上下文管理器：

功能：
1. 进入时记录开始时间
2. 退出时打印执行时间
3. 可以通过 with 语句使用

测试代码：
with Timer("测试代码"):
    time.sleep(1)
    
输出：
测试代码 执行时间: 1.00 秒
"""

# TODO: 在这里实现 Timer 上下文管理器（使用 __enter__ 和 __exit__）




# ================================
# 练习 5：上下文管理器（contextlib）
# ================================
"""
任务：使用 @contextmanager 创建一个文件处理上下文：

功能：
1. 打开文件
2. 自动关闭文件
3. 处理异常（文件不存在）

测试代码：
with safe_open("test.txt", "w") as f:
    f.write("Hello, Python!")
"""

# TODO: 在这里实现 safe_open 上下文管理器（使用 @contextmanager）




# ================================
# 练习 6：实战 - 缓存装饰器
# ================================
"""
任务：创建一个 cache 装饰器，缓存函数结果：

功能：
1. 缓存函数的返回值（基于参数）
2. 相同参数直接返回缓存结果
3. 不同参数重新计算

测试代码：
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 第一次计算
print(fibonacci(10))  # 直接返回缓存
"""

# TODO: 在这里实现 cache 装饰器




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    import time
    
    print("=" * 60)
    print("Day 4 练习验证")
    print("=" * 60)
    
    # 测试练习 1
    print("\n--- 练习 1：log_decorator ---")
    # @log_decorator
    # def say_hello(name):
    #     print(f"Hello, {name}!")
    #     time.sleep(1)
    # say_hello("张三")
    
    # 测试练习 2
    print("\n--- 练习 2：repeat 装饰器 ---")
    # @repeat(n=3)
    # def greet(name):
    #     return f"你好, {name}!"
    # print(greet("李四"))
    
    # 测试练习 3
    print("\n--- 练习 3：CountCalls 类装饰器 ---")
    # @CountCalls
    # def add(a, b):
    #     return a + b
    # print(add(1, 2))
    # print(add(3, 4))
    # print(f"调用次数: {add.count}")
    
    # 测试练习 4
    print("\n--- 练习 4：Timer 上下文管理器 ---")
    # with Timer("测试代码"):
    #     time.sleep(1)
    
    # 测试练习 5
    print("\n--- 练习 5：safe_open ---")
    # with safe_open("test.txt", "w") as f:
    #     f.write("Hello, Python!")
    
    # 测试练习 6
    print("\n--- 练习 6：cache 装饰器 ---")
    # @cache
    # def fibonacci(n):
    #     if n < 2:
    #         return n
    #     return fibonacci(n-1) + fibonacci(n-2)
    # print(fibonacci(10))
    # print(fibonacci(10))
    
    print("\n✅ Day 4 练习完成！")