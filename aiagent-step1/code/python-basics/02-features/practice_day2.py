"""
Day 2 练习：Python 特色语法

说明：本文件只有练习题，没有答案。
      请参考 pythonic_syntax.py 查看示例和答案。

练习方法：
1. 阅读 pythonic_syntax.py 理解语法
2. 在本文件中编写代码完成练习
3. 运行本文件验证结果
"""


# ================================
# 练习 1：列表推导式
# ================================

# TODO: 使用列表推导式生成 1-20 中所有偶数
numbers = [i for i in range(1, 21) if i % 2 == 0]
print(f"numbers = {numbers}")

# TODO: 使用列表推导式生成 1-10 的平方数
numbers = [ i**2 for i in range(1,11)]
print(f"numbers = {numbers}")

# TODO: 使用列表推导式生成 1-50 中所有 3 的倍数
numbers = [i for i in range(1,51) if i % 3 == 0]
print(f"numbers = {numbers}")

# TODO: 使用列表推导式，从字符串列表中筛选出长度大于 3 的单词
words = ["cat", "dog", "apple", "banana", "hi", "hello"]
# words = list(filter(lambda w : len(w) > 3, words))
words = [word for word in words if len(word) > 3 ]
print(f'words = {words}')

# ================================
# 练习 2：字典推导式
# ================================

# TODO: 使用字典推导式，生成 1-5 的平方字典 {1: 1, 2: 4, ...}
dicts = {i:i**2 for i in range(1,6)}
print(f'dicts = {dicts}')

# TODO: 使用字典推导式，将列表转换为索引-值字典
fruits = ["苹果", "香蕉", "橙子"]
dicts = { i:f for i,f in enumerate(fruits)}
print(f'dicts = {dicts}')

# TODO: 使用字典推导式，筛选成绩大于 80 的学生
students = {"张三": 85, "李四": 92, "王五": 78, "赵六": 88}
students = {name: grade for name, grade in students.items() if grade > 80}
print(f"students = {students}")

# ================================
# 练习 3：集合推导式
# ================================

# TODO: 使用集合推导式，生成 -5 到 5 的平方数（去重）
num_set = set((i**2 for i in range(-5,6)))
print(f'num_set = {num_set}')

# ================================
# 练习 4：Lambda 表达式
# ================================

# TODO: 定义一个 lambda 函数，计算两个数的乘积
mul_method = lambda a,b : a * b
print(f'mul_method(2,3) = {mul_method(1,3)}')

# TODO: 使用 lambda 和 sorted，按成绩降序排序学生列表
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]
# def sorted(
    # iterable: Iterable[SupportsRichComparisonT], /, *, key: None = None, reverse: bool = False
# ) -> list[SupportsRichComparisonT]: ...，这里的/和*代表什么，pyi文件中的
# 疑问1
students = sorted(students, key = lambda student : student['score'], reverse= True)
print(f'students = {students}')


# TODO: 使用 lambda 和 filter，筛选 1-20 中的奇数
ji_numbers = list(filter(lambda a : a % 2 > 0, [i for i in range(1, 21)]))
print(f'ji_numbers = {ji_numbers}')

# ================================
# 练习 5：解构赋值
# ================================

# TODO: 解构列表 [1, 2, 3] 到三个变量 a, b, c
a, b, c = [1, 2, 3]
print(f'a = {a}, b = {b}, c = {c}')

# TODO: 解构列表 [1, 2, 3, 4, 5]，第一个给 first，其余给 rest
first, *rest = [1,2,3,4,5]
print(f'first = {first}, type = {type(first)}, rest = {rest}, type = {type(rest)}')

# TODO: 编写函数 get_stats，返回列表的最小值、最大值、平均值，并解构接收
def get_stats(calList : list):
    return max(calList), min(calList), sum(calList)/len(calList)
# 疑问2: 变量名max能覆盖内置函数名max
max_val,min_val,avg = get_stats([1,2,3,4])
print(f'max={max_val}, min={min_val}, avg={avg}')
lista = get_stats([1,2,3,4])
print(f'list = {lista}, {type(lista)}')

# ================================
# 练习 6：字符串格式化
# ================================

# TODO: 使用 f-string 格式化输出（保留 2 位小数）
price = 99.9876
quantity = 5
print(f'price = {price:.2f}, quantity = {quantity}')
string = 'price = {:.2f}, quantity = {}'.format(price, quantity)
print(string)


# ================================
# 练习 7：enumerate 和 zip
# ================================

# TODO: 使用 enumerate 打印水果列表，格式："第 1 个水果：苹果"
fruits = ["苹果", "香蕉", "橙子"]
for index,item in enumerate(fruits, 1):
    print(f'第 {index} 个水果，{item}')
    

# TODO: 使用 zip 合并三个列表为字典
names = ["张三", "李四", "王五"]
ages = [25, 30, 35]
cities = ["北京", "上海", "广州"]
ziped_info = zip(names, ages, cities)
info_dicts = []
for name,age,city in ziped_info:
    info_dict = {'name':name, 'age':age, 'city':city}
    info_dicts.append(info_dict)
print(f'info_dicts = {info_dicts}')


# ================================
# 练习 8：any() 和 all()
# ================================

# TODO: 使用 any() 检查列表中是否有负数
numbers = [1, 2, -3, 4, 5]
print(any(n < 0 for n in numbers))


# TODO: 使用 all() 检查列表中是否全部为偶数
numbers = [2, 4, 6, 8, 10]
is_all_ou = all(n % 2 == 0 for n in numbers)
print(f'is_all_ou = {is_all_ou}')

# ================================
# 综合练习
# ================================

# TODO: 使用列表推导式，生成九九乘法表的字符串列表
# 格式："1 × 1 = 1", "2 × 1 = 2", "2 × 2 = 4", ...
rst_99 = []
for i in range(1,10):
    for j in range(i,10):
        rst_99.append(f'{i} × {j} = {i*j}')
print(f'99_mul = {rst_99}')

rst_99 = [f'{i} × {j} = {i*j}' for i in range(1,10) for j in range(i,10)]
print(f'rst_99 = {rst_99}')


# TODO: 使用字典推导式，统计字符串中每个字符出现的次数
text = "hello world"
number_times = {}
for ch in text:
    existNum = number_times.get(ch)
    if existNum is None:
        existNum = 1
    else:
        existNum += 1
    number_times.update({ch:existNum})
print(f'number_times = {number_times}')


# TODO: 使用 zip 和 enumerate，创建学生成绩单
# 输出格式：[{index: 0, name: "张三", score: 85}, ...]
names = ["张三", "李四", "王五"]
scores = [85, 92, 78]
rst_score = []
for index,item  in enumerate(dict(zip(names, scores)).items()):
    element = {'index':index, 'name':item[0], 'score':item[1]}
    rst_score.append(element)
print(f'rst_score = {rst_score}')
    

# ================================
# 验证区域
# ================================

print("\n" + "="*60)
print("Day 2 练习验证")
print("="*60)

# 在这里添加验证代码
# 例如：
# print(f"练习 1: 偶数列表={evens}")
# print(f"练习 2: 平方字典={square_dict}")
# print(f"练习 4: 排序后={sorted_students}")

print("\n✅ 完成所有练习后，取消上面的注释并运行！")