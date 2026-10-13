# TODO: 使用列表推导式生成 1-20 中所有偶数
numbers = [i for i in range(20) if i%2 == 0]
print(f"20以内偶数有 = {numbers}")

# TODO: 使用字典推导式，将列表转换为索引-值字典
fruits = ["苹果", "香蕉", "橙子"]
dicts = {index:f for index,f in enumerate(fruits)}
print(f"水果字典 = {dicts}")

# TODO: 使用集合推导式，生成 -5 到 5 的平方数（去重）
setitems = set(i**2 for i in range(-5,6))
print(f"集合 = {setitems}")


# TODO: 定义一个 lambda 函数，计算两个数的乘积
multi_function = lambda a,b : a*b
rst = multi_function(2,3)
print(rst)

# TODO: 使用 lambda 和 sorted，按成绩降序排序学生列表
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]
sorted_students = sorted(students, key = lambda stu : stu["score"], reverse=True)
print(f"排序过的 ：{sorted_students}")
