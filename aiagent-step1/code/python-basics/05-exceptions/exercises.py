"""
Day 5: 异常处理和文件操作练习

学习目标：掌握异常处理和文件读写
"""


# ================================
# 练习 1：异常处理
# ================================
"""
任务：实现一个安全的除法函数：

功能：
1. 接收两个参数 a 和 b
2. 处理 ZeroDivisionError（除零错误）
3. 处理 TypeError（类型错误）
4. 返回结果或错误消息

测试代码：
print(safe_divide(10, 2))   # 输出：5.0
print(safe_divide(10, 0))   # 输出：错误：除数不能为零
print(safe_divide(10, "2")) # 输出：错误：参数类型不正确
"""

# TODO: 在这里实现 safe_divide 函数
def devide_0(a, b) -> float:
    try:
        return a/b
    except ZeroDivisionError as e:
        print("错误：除数不能为零")
    except TypeError as e:
        print('错误：参数类型不正确')

    return 0

rst0 = devide_0(1,0)
rst1 = devide_0(1,2)
print(f'rst0={rst0},rst1={rst1}')

# ================================
# 练习 2：自定义异常
# ================================
"""
任务：创建自定义异常和验证函数：

1. 自定义异常：
   - InvalidAgeError（年龄无效）
   - InvalidEmailError（邮箱无效）

2. 验证函数：
   - validate_age(age)：验证年龄（0-150）
   - validate_email(email)：验证邮箱格式（包含@）

测试代码：
try:
    validate_age(-5)
except InvalidAgeError as e:
    print(e)

try:
    validate_email("invalid-email")
except InvalidEmailError as e:
    print(e)
"""

# TODO: 在这里实现自定义异常和验证函数
class InvalidAgeError(Exception):
    def __init__(self, age, message):
        self._age = age
        self._message = message
        super().__init__(f'{message}:{age}')

def validate_age(age) -> bool:
    if age < 1 or age > 200:
        raise InvalidAgeError(age, '年龄无效')
    return True

print(f'年龄验证：{validate_age(88)}')
try:
    validate_age(800)
except InvalidAgeError as e:
    print(f'异常了:{e}')




# ================================
# 练习 3：文件读取
# ================================
"""
任务：实现一个读取文件并统计行数的函数：

功能：
1. 接收文件路径
2. 返回文件行数
3. 处理 FileNotFoundError
4. 使用 with 语句自动关闭文件

测试代码：
lines = count_lines("test.txt")
print(f"文件有 {lines} 行")
"""

# TODO: 在这里实现 count_lines 函数
def read_count(path: str) -> int:
    try:
        with open(path, 'r', encoding='utf8') as f:
            return len(f.readlines())
    except FileNotFoundError as e:
        print('文件不存在')
        return 0

rows = read_count('py5_test.txt')
print(f'rows = {rows}')




# ================================
# 练习 4：文件写入
# ================================
"""
任务：实现一个写入日志的函数：

功能：
1. 接收日志文件路径和消息
2. 在消息前添加时间戳
3. 追加写入文件（不覆盖）
4. 处理权限错误

测试代码：
write_log("app.log", "系统启动")
write_log("app.log", "用户登录")
"""
import time
# TODO: 在这里实现 write_log 函数
def write_log(path:str, logMsg:str):
    # note：时间格式化不是yyyy-MM-dd这张
    logMsg = time.strftime('%Y-%m-%d %H:%M:%S   ') +  logMsg

    try:
        with open(path, 'a', encoding='utf8') as f:
            f.write(logMsg)
    except PermissionError as e:
        pass

write_log('py5_test.txt', '系统启动完成\n')



# ================================
# 练习 5：JSON 文件处理
# ================================
"""
任务：实现 JSON 配置文件读写：

功能：
1. read_config(path)：读取 JSON 配置文件
2. write_config(path, config)：写入 JSON 配置文件
3. 处理 JSON 解析错误

测试代码：
config = {"name": "张三", "age": 25, "city": "北京"}
write_config("config.json", config)

loaded_config = read_config("config.json")
print(loaded_config)
"""
import json
# TODO: 在这里实现 read_config 和 write_config 函数
def read_config(path):
    with open(path, 'r', encoding='utf8') as f:
        return json.load(f)

def write_config(path, config):
    with open(path, 'w', encoding='utf8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


config = {"name": "张三", "age": 25, "city": "北京"}

json_obj = read_config('py5_config.json')
print(f'{json_obj["name"]}')
print(f'json_obj = {json_obj}')

write_config('py5_config.json', config)



# ================================
# 练习 6：CSV 文件处理
# ================================
"""
任务：实现 CSV 文件读写：

功能：
1. read_csv(path)：读取 CSV 文件，返回字典列表
2. write_csv(path, data)：写入 CSV 文件

测试代码：
students = [
    {"name": "张三", "age": 18, "score": 90},
    {"name": "李四", "age": 19, "score": 85}
]

write_csv("students.csv", students)
loaded_students = read_csv("students.csv")
for student in loaded_students:
    print(student)
"""
import csv
# TODO: 在这里实现 read_csv 和 write_csv 函数
def read_csv(path):
    with open(path, 'r', encoding='utf8') as f:
        csv_dict = csv.DictReader(f)
        for row in csv_dict:
            print(f'csv_dict row= {row}')

read_csv('py5.csv')

students = [
    {"name": "张三feng", "age": 18, "score": 90},
    {"name": "李四gou", "age": 19, "score": 85}
]
def write_csv(path, data):
    # note:为什么需要处理newline，才能避免空行
    with open(path, 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'age', 'score'])
        writer.writeheader()
        writer.writerows(data)
write_csv('py5.csv', students)




# ================================
# 练习 7：文件搜索
# ================================
"""
任务：实现一个在文件中搜索关键词的函数：

功能：
1. 接收文件路径和关键词
2. 返回包含关键词的行号和内容
3. 处理文件不存在错误

测试代码：
results = search_in_file("test.txt", "Python")
for line_num, line in results:
    print(f"第 {line_num} 行: {line}")
"""

# TODO: 在这里实现 search_in_file 函数
def search_in_file(path, keyword):
    rst = []
    with open(path, 'r', encoding='utf8') as f:
        for index, line in enumerate(f.readlines(), 1):
            findRst = str(line).find(keyword)
            if findRst >= 0:
                rst_tmp = {index:line}
                rst.append(rst_tmp)
    return rst

rst = search_in_file('py5.csv', '张三')
print(f'rst = {rst}')




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    import json
    import csv
    from datetime import datetime

    print("=" * 60)
    print("Day 5 练习验证")
    print("=" * 60)

    # 测试练习 1
    print("\n--- 练习 1：safe_divide ---")
    # print(safe_divide(10, 2))
    # print(safe_divide(10, 0))
    # print(safe_divide(10, "2"))

    # 测试练习 2
    print("\n--- 练习 2：自定义异常 ---")
    # try:
    #     validate_age(-5)
    # except InvalidAgeError as e:
    #     print(e)

    # 测试练习 3
    print("\n--- 练习 3：count_lines ---")
    # lines = count_lines("test.txt")
    # print(f"文件有 {lines} 行")

    # 测试练习 4
    print("\n--- 练习 4：write_log ---")
    # write_log("app.log", "系统启动")

    # 测试练习 5
    print("\n--- 练习 5：JSON 配置 ---")
    # config = {"name": "张三", "age": 25}
    # write_config("config.json", config)
    # print(read_config("config.json"))

    # 测试练习 6
    print("\n--- 练习 6：CSV 文件 ---")
    # students = [{"name": "张三", "age": 18}]
    # write_csv("students.csv", students)
    # print(read_csv("students.csv"))

    # 测试练习 7
    print("\n--- 练习 7：文件搜索 ---")
    # results = search_in_file("test.txt", "Python")
    # for line_num, line in results:
    #     print(f"第 {line_num} 行: {line}")

    print("\n✅ Day 5 练习完成！")
