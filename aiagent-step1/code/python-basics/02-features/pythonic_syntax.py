"""
Day 2: Python 特色语法

学习目标：掌握 Python 特有的语法特性
"""

# ================================
# 1. 列表推导式（List Comprehension）
# ================================

# 传统方式（类似 Java）
numbers = []
for i in range(10):
    numbers.append(i * 2)
print(f"传统方式: {numbers}")

# 列表推导式（Pythonic）
numbers = [i * 2 for i in range(10)]
print(f"列表推导式: {numbers}")


# 带条件的列表推导式
# 传统方式
evens = []
for i in range(20):
    if i % 2 == 0:
        evens.append(i)
print(f"偶数（传统）: {evens}")

# 列表推导式
evens = [i for i in range(20) if i % 2 == 0]
print(f"偶数（推导式）: {evens}")


# 复杂示例：生成平方数，过滤小于 50 的
squares = [i**2 for i in range(10) if i**2 < 50]
print(f"平方数（<50）: {squares}")


# ================================
# 2. 字典推导式
# ================================

# 传统方式
square_dict = {}
for i in range(5):
    square_dict[i] = i**2
print(f"传统字典: {square_dict}")

# 字典推导式
square_dict = {i: i**2 for i in range(5)}
print(f"字典推导式: {square_dict}")


# 带条件的字典推导式
words = ["apple", "banana", "cat", "dog"]
word_lengths = {word: len(word) for word in words if len(word) > 3}
print(f"单词长度（>3）: {word_lengths}")


# ================================
# 3. 集合推导式
# ================================

# 集合推导式（自动去重）
unique_squares = {i**2 for i in range(-5, 6)}
print(f"唯一平方数: {unique_squares}")


# ================================
# 4. Lambda 表达式
# ================================

# Java Lambda：
# (a, b) -> a + b

# Python Lambda：
add = lambda a, b: a + b
print(f"Lambda 加法: {add(3, 5)}")


# 实际应用：排序
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]

# 按成绩排序
students_sorted = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"按成绩排序: {students_sorted}")


# ================================
# 5. map()、filter()、reduce()
# ================================

# map：对每个元素应用函数
numbers = [1, 2, 3, 4, 5]

# 传统方式
squares = []
for num in numbers:
    squares.append(num ** 2)
print(f"传统平方: {squares}")

# map 方式
squares = list(map(lambda x: x**2, numbers))
print(f"map 平方: {squares}")

# 列表推导式（推荐）
squares = [x**2 for x in numbers]
print(f"推导式平方: {squares}")


# filter：过滤元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter 偶数: {evens}")

# 列表推导式（推荐）
evens = [x for x in numbers if x % 2 == 0]
print(f"推导式偶数: {evens}")


# reduce：累积计算
from functools import reduce

# 求和
total = reduce(lambda x, y: x + y, numbers)
print(f"reduce 求和: {total}")

# 传统方式（推荐）
total = sum(numbers)
print(f"sum 求和: {total}")


# ================================
# 6. 解构赋值（Unpacking）
# ================================

# 列表解构
a, b, c = [1, 2, 3]
print(f"解构赋值: a={a}, b={b}, c={c}")

# 解构 + 剩余
first, *rest = [1, 2, 3, 4, 5]
print(f"第一个: {first}, 剩余: {rest}")

# 字典解构
person = {"name": "张三", "age": 25}
name, age = person.values()
print(f"姓名: {name}, 年龄: {age}")


# 函数返回多值（自动解构）
def get_min_max(numbers: list) -> tuple:
    """返回最小值和最大值"""
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print(f"最小值: {min_val}, 最大值: {max_val}")


# ================================
# 7. 字符串格式化
# ================================

name = "张三"
age = 25
score = 88.5

# % 格式化（类似 C 语言）
print("姓名: %s, 年龄: %d, 成绩: %.1f" % (name, age, score))

# format() 方法
print("姓名: {}, 年龄: {}, 成绩: {:.1f}".format(name, age, score))

# f-string（推荐）
print(f"姓名: {name}, 年龄: {age}, 成绩: {score:.1f}")


# ================================
# 8. 枚举（enumerate）
# ================================

fruits = ["苹果", "香蕉", "橙子"]

# 传统方式
for i in range(len(fruits)):
    print(f"索引 {i}: {fruits[i]}")

# enumerate（推荐）
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"第 {index} 个水果: {fruit}")


# ================================
# 9. zip：并行遍历
# ================================

names = ["张三", "李四", "王五"]
ages = [25, 30, 35]
cities = ["北京", "上海", "广州"]

# 传统方式
for i in range(len(names)):
    print(f"姓名: {names[i]}, 年龄: {ages[i]}, 城市: {cities[i]}")

# zip（推荐）
for name, age, city in zip(names, ages, cities):
    print(f"姓名: {name}, 年龄: {age}, 城市: {city}")

# 创建字典
user_dict = dict(zip(names, ages))
print(f"用户字典: {user_dict}")


# ================================
# 10. any() 和 all()
# ================================

numbers = [1, 2, 3, 4, 5]

# any：至少一个为 True
has_even = any(x % 2 == 0 for x in numbers)
print(f"有偶数吗？{has_even}")

# all：全部为 True
all_positive = all(x > 0 for x in numbers)
print(f"全部为正数吗？{all_positive}")


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)

# 练习 1：使用列表推导式生成 1-100 中所有 3 的倍数
multiples_of_3 = [i for i in range(1, 101) if i % 3 == 0]
print(f"练习 1 - 3的倍数（前10个）: {multiples_of_3[:10]}")


# 练习 2：使用字典推导式，将列表转换为索引-值字典
words = ["apple", "banana", "cherry"]
word_dict = {i: word for i, word in enumerate(words)}
print(f"练习 2 - 索引字典: {word_dict}")


# 练习 3：使用 lambda 和 sorted，按字符串长度排序
words = ["apple", "banana", "cat", "dog", "elephant"]
sorted_words = sorted(words, key=lambda x: len(x))
print(f"练习 3 - 按长度排序: {sorted_words}")


# 练习 4：使用 zip 合并两个列表为字典
keys = ["name", "age", "city"]
values = ["张三", 25, "北京"]
user = dict(zip(keys, values))
print(f"练习 4 - 用户字典: {user}")


# 练习 5：使用列表推导式，生成九九乘法表
multiplication_table = [
    f"{i} × {j} = {i*j}"
    for i in range(1, 10)
    for j in range(1, i+1)
]
print("练习 5 - 九九乘法表（前5个）:")
for item in multiplication_table[:5]:
    print(f"  {item}")

print("\n✅ Day 2 学习完成！")
print("要点总结：")
print("1. 列表推导式：[x for x in list if condition]")
print("2. 字典推导式：{k: v for k, v in dict.items()}")
print("3. Lambda：lambda x: x * 2")
print("4. map/filter：推荐用列表推导式替代")
print("5. 解构赋值：a, b = [1, 2]")
print("6. f-string：f\"姓名: {name}\"")
print("7. enumerate：for i, x in enumerate(list)")
print("8. zip：并行遍历多个列表")