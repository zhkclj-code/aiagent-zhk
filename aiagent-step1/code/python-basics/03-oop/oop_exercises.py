"""
Day 3: 面向对象练习（Python 风格）

学习目标：掌握 Python 的面向对象编程
"""


# ================================
# 练习 1：创建一个简单的类
# ================================
"""
任务：创建一个 Student 类，包含以下功能：

1. 属性：
   - name（姓名）
   - age（年龄）
   - grade（年级）

2. 方法：
   - __init__：构造函数，初始化属性
   - __str__：返回学生的字符串表示
   - study：学习方法，打印"{name}正在学习"

3. 测试代码：
   student = Student("张三", 18, "大一")
   print(student)
   student.study()
"""

# TODO: 在这里实现 Student 类




# ================================
# 练习 2：继承和方法重写
# ================================
"""
任务：创建一个 GraduateStudent 类，继承自 Student：

1. 新增属性：
   - thesis（论文题目）

2. 重写 __str__ 方法，包含论文信息

3. 新增 defend_thesis 方法，打印"{name}正在答辩论文：{thesis}"

4. 测试代码：
   grad = GraduateStudent("李四", 25, "博士", "深度学习在NLP中的应用")
   print(grad)
   grad.defend_thesis()
"""

# TODO: 在这里实现 GraduateStudent 类




# ================================
# 练习 3：属性装饰器（@property）
# ================================
"""
任务：创建一个 BankAccount 类：

1. 属性：
   - _balance（余额，私有）

2. 使用 @property 装饰器：
   - 创建 balance 属性（只读，返回余额）
   - 创建 balance_setter（设置余额，需要验证非负）

3. 方法：
   - deposit：存款
   - withdraw：取款（余额不足时打印提示）

4. 测试代码：
   account = BankAccount(1000)
   print(f"当前余额: {account.balance}")
   account.deposit(500)
   account.withdraw(200)
   print(f"取款后余额: {account.balance}")
"""

# TODO: 在这里实现 BankAccount 类




# ================================
# 练习 4：类方法和静态方法
# ================================
"""
任务：创建一个 DateUtils 类：

1. 类方法：
   - from_string(date_string)：从字符串创建日期对象
     格式："2024-01-13"

2. 静态方法：
   - is_leap_year(year)：判断是否为闰年
   - days_in_month(year, month)：返回某年某月的天数

3. 测试代码：
   date = DateUtils.from_string("2024-01-13")
   print(f"闰年？{DateUtils.is_leap_year(2024)}")
   print(f"2024年2月有{DateUtils.days_in_month(2024, 2)}天")
"""

# TODO: 在这里实现 DateUtils 类




# ================================
# 练习 5：魔法方法（__eq__, __lt__）
# ================================
"""
任务：创建一个 Point 类：

1. 属性：
   - x（横坐标）
   - y（纵坐标）

2. 魔法方法：
   - __eq__：判断两个点是否相等（x和y都相等）
   - __lt__：判断点的大小（先比较x，再比较y）
   - __add__：两个点相加（x+x, y+y）

3. 测试代码：
   p1 = Point(1, 2)
   p2 = Point(1, 2)
   p3 = Point(2, 3)
   
   print(f"p1 == p2? {p1 == p2}")
   print(f"p1 < p3? {p1 < p3}")
   print(f"p1 + p3 = {p1 + p3}")
"""

# TODO: 在这里实现 Point 类




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("Day 3 练习验证")
    print("=" * 60)
    
    # 测试练习 1
    print("\n--- 练习 1：Student 类 ---")
    # 取消注释测试你的实现
    # student = Student("张三", 18, "大一")
    # print(student)
    # student.study()
    
    # 测试练习 2
    print("\n--- 练习 2：GraduateStudent 类 ---")
    # grad = GraduateStudent("李四", 25, "博士", "深度学习在NLP中的应用")
    # print(grad)
    # grad.defend_thesis()
    
    # 测试练习 3
    print("\n--- 练习 3：BankAccount 类 ---")
    # account = BankAccount(1000)
    # print(f"当前余额: {account.balance}")
    # account.deposit(500)
    # account.withdraw(200)
    
    # 测试练习 4
    print("\n--- 练习 4：DateUtils 类 ---")
    # print(f"闰年？{DateUtils.is_leap_year(2024)}")
    # print(f"2024年2月有{DateUtils.days_in_month(2024, 2)}天")
    
    # 测试练习 5
    print("\n--- 练习 5：Point 类 ---")
    # p1 = Point(1, 2)
    # p2 = Point(1, 2)
    # p3 = Point(2, 3)
    # print(f"p1 == p2? {p1 == p2}")
    # print(f"p1 < p3? {p1 < p3}")
    # print(f"p1 + p3 = {p1 + p3}")
    
    print("\n✅ Day 3 练习完成！")
    print("提示：取消注释测试代码，验证你的实现")