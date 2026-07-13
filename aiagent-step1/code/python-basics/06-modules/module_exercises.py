"""
Day 6: 模块和包管理练习

学习目标：掌握模块导入和包管理
"""


# ================================
# 练习 1：创建自定义模块
# ================================
"""
任务：创建一个 math_utils 模块（math_utils.py）：

包含以下函数：
1. add(a, b)：加法
2. subtract(a, b)：减法
3. multiply(a, b)：乘法
4. divide(a, b)：除法（处理除零）
5. PI：圆周率常量

然后在当前文件中导入并使用：
import math_utils
from math_utils import add, PI

测试代码：
print(math_utils.add(3, 5))
print(f"圆周率: {math_utils.PI}")
"""

# TODO: 创建 math_utils.py 文件，并在这里导入测试




# ================================
# 练习 2：包结构
# ================================
"""
任务：创建一个 shapes 包：

包结构：
shapes/
├── __init__.py
├── circle.py（包含 Circle 类）
└── rectangle.py（包含 Rectangle 类）

Circle 类：
- 属性：radius
- 方法：area()、perimeter()

Rectangle 类：
- 属性：width、height
- 方法：area()、perimeter()

测试代码：
from shapes import Circle, Rectangle

circle = Circle(5)
print(f"圆面积: {circle.area()}")

rect = Rectangle(4, 6)
print(f"矩形面积: {rect.area()}")
"""

# TODO: 创建 shapes 包，并在这里导入测试




# ================================
# 练习 3：相对导入
# ================================
"""
任务：扩展 shapes 包，添加 utils.py 模块：

utils.py 功能：
- distance(x1, y1, x2, y2)：计算两点距离

在 circle.py 中使用相对导入：
from .utils import distance

Circle 新增方法：
- distance_to(self, other_circle)：计算两圆心距离

测试代码：
c1 = Circle(0, 0)
c2 = Circle(3, 4)
print(f"圆心距离: {c1.distance_to(c2)}")
"""

# TODO: 创建 utils.py，修改 circle.py，在这里测试




# ================================
# 练习 4：__all__ 和 __name__
# ================================
"""
任务：修改 shapes/__init__.py：

1. 使用 __all__ 限制导出：
   __all__ = ["Circle", "Rectangle"]

2. 添加模块级别的函数：
   def describe():
       return "这是一个几何图形包"

3. 添加 __name__ 检测：
   if __name__ == "__main__":
       print("shapes 模块测试")

测试代码：
from shapes import *
print(Circle(5).area())
print(describe())
"""

# TODO: 修改 __init__.py，在这里测试




# ================================
# 练习 5：pip 和 requirements.txt
# ================================
"""
任务：管理项目依赖：

1. 创建 requirements.txt：
   requests>=2.28.0
   pydantic>=2.0.0

2. 安装依赖：
   pip install -r requirements.txt

3. 验证安装：
   import requests
   import pydantic

4. 导出当前依赖：
   pip freeze > requirements.txt

测试代码：
import requests
response = requests.get("https://httpbin.org/get")
print(f"状态码: {response.status_code}")
"""

# TODO: 创建 requirements.txt，安装依赖，在这里测试




# ================================
# 练习 6：创建可执行脚本
# ================================
"""
任务：创建一个命令行工具（cli.py）：

功能：
1. 使用 argparse 解析命令行参数
2. 支持 --name 和 --greet 参数
3. 打印问候语

运行方式：
python cli.py --name 张三 --greet

预期输出：
你好, 张三!
"""

# TODO: 创建 cli.py 文件（在项目根目录）




# ================================
# 练习 7：setup.py 打包
# ================================
"""
任务：创建一个可安装的包：

1. 创建 setup.py：
   from setuptools import setup, find_packages
   
   setup(
       name="shapes",
       version="1.0.0",
       packages=find_packages(),
       install_requires=[
           "requests>=2.28.0"
       ]
   )

2. 安装包：
   pip install -e .

3. 验证：
   from shapes import Circle
   print(Circle(5).area())
"""

# TODO: 创建 setup.py，安装包，在这里验证




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("Day 6 练习验证")
    print("=" * 60)
    
    # 测试练习 1
    print("\n--- 练习 1：自定义模块 ---")
    # import math_utils
    # print(math_utils.add(3, 5))
    
    # 测试练习 2
    print("\n--- 练习 2：包结构 ---")
    # from shapes import Circle, Rectangle
    # circle = Circle(5)
    # print(f"圆面积: {circle.area()}")
    
    # 测试练习 3
    print("\n--- 练习 3：相对导入 ---")
    # c1 = Circle(0, 0)
    # c2 = Circle(3, 4)
    # print(f"圆心距离: {c1.distance_to(c2)}")
    
    # 测试练习 4
    print("\n--- 练习 4：__all__ ---")
    # from shapes import *
    # print(Circle(5).area())
    
    # 测试练习 5
    print("\n--- 练习 5：pip 管理 ---")
    # import requests
    # response = requests.get("https://httpbin.org/get")
    # print(f"状态码: {response.status_code}")
    
    print("\n✅ Day 6 练习完成！")
    print("提示：需要创建额外的文件（math_utils.py、shapes/）")