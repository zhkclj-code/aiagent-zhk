"""
Day 6: 模块和包管理

学习目标：理解 Python 模块系统和包管理
"""

# ================================
# 0. 模块和包核心概念 - Java开发者必读
# ================================

"""
【核心定义】

模块（Module）：
- 一个.py文件就是一个模块
- 模块名 = 文件名（不含.py）
- 可包含：变量、函数、类

包（Package）：
- 一个包含__init__.py的目录
- 用于组织多个模块
- 包可以有子包（嵌套目录）

【Python模块 vs Java Package对比】

| 特性 | Python模块 | Java Package |
|-----|-----------|-------------|
| 定义 | .py文件 | 目录（无特殊文件） |
| 命名 | 文件名（不含.py） | 目录路径 |
| 必需文件 | 无（就是.py文件） | 无（就是目录） |
| 导入语法 | import module | import package.Class |
| 访问控制 | 无（约定：_开头为私有） | public/private/protected |

【Python包 vs Java Package对比】

| 特性 | Python包 | Java Package |
|-----|---------|-------------|
| 定义 | 含__init__.py的目录 | 目录（无特殊文件） |
| 标识文件 | __init__.py（Python 3.3+可省略） | 无 |
| 命名空间包 | 支持（无__init__.py） | 无此概念 |
| 访问控制 | 通过__all__控制from pkg import * | 通过访问修饰符 |

【核心差异】

1. 模块定义：
   Python:
   my_module.py  # 这就是一个模块
   # 导入：import my_module

   Java:
   package com.example;
   // MyClass.java 属于包 com.example

2. 包定义：
   Python:
   my_package/
   ├── __init__.py  # 标识这是一个包
   ├── module1.py
   └── module2.py

   Java:
   src/main/java/
   └── com/example/  # 目录结构决定包名
       ├── Class1.java  # package com.example;
       └── Class2.java  # package com.example;

3. __init__.py的作用：
   - 标识目录为Python包
   - 可在导入时执行初始化代码
   - 可定义__all__控制导出
   - Python 3.3+可省略（命名空间包）

【导入顺序规范】

1. 标准库
2. 第三方库
3. 本地模块

import os
import sys

import numpy as np
import requests

from my_package import my_module

【导入方式对比】

import module：
- ✅ 命名空间清晰（module.func()）
- ✅ 避免命名冲突
- 适用于：标准库、第三方库

from module import func：
- ✅ 代码简洁（直接用func()）
- ❌ 可能命名冲突
- 适用于：常用函数/类

from module import *：
- ❌ 污染命名空间
- ❌ 不明确来源
- ❌ 难以追踪
- ❌ 不推荐使用

【相对导入 vs 绝对导入】

绝对导入（推荐）：
from my_package.submodule import func

相对导入（包内部）：
from . import sibling_module  # 同级模块
from .. import parent_module   # 上级模块
from .submodule import func    # 子模块

【循环导入问题】

场景：模块A导入B，B导入A
解决方案：
1. 重构代码，提取公共部分到第三个模块
2. 在函数内部延迟导入

# 错误：顶层导入
import module_b

def func():
    module_b.do_something()

# 正确：函数内导入
def func():
    import module_b  # 延迟导入
    module_b.do_something()

【__name__ == '__main__'】

用途：区分模块是被导入还是直接运行

if __name__ == '__main__':
    # 直接运行时执行
    main()
else:
    # 被导入时不执行

【最佳实践】

1. 一个模块一个职责
2. 使用绝对导入（避免相对导入）
3. 避免from module import *
4. 在__init__.py中导入公共API
5. 使用__all__控制from pkg import *
6. 循环依赖时重构代码

【常见陷阱】

1. 文件名和模块名冲突：
   # 如果有random.py，会覆盖标准库
   import random  # 导入的是你的random.py！

2. 导入顺序问题：
   # 标准库 → 第三方库 → 本地模块
   # 违反此顺序可能导致混乱

3. 相对导入在脚本中失效：
   python script.py  # 相对导入失败
   python -m package.script  # 正确

【Java开发者迁移建议】

Java Package → Python模块
───────────────────────────────
package com.example.MyClass; → # my_package/my_module.py
import com.example.*; → from my_package import *（不推荐）
import com.example.MyClass; → from my_package import my_module
src/main/java/ → 项目根目录或PYTHONPATH
Maven/Gradle → pip + requirements.txt

【pip vs Maven/Gradle】

| 特性 | pip | Maven/Gradle |
|-----|-----|-------------|
| 配置文件 | requirements.txt | pom.xml / build.gradle |
| 安装命令 | pip install -r requirements.txt | mvn install |
| 版本锁定 | package==1.0.0 | <version>1.0.0</version> |
| 虚拟环境 | venv, virtualenv | 无内置（用容器） |
| 依赖传递 | 支持 | 支持 |
"""

# ================================
# 1. 模块导入基础
# ================================

# Java 导入：
# import java.util.List;
# import java.util.*;

# Python 导入：
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional

print("模块导入示例:")
print(f"当前目录: {os.getcwd()}")
print(f"Python 版本: {sys.version}")
print(f"当前时间: {datetime.now()}")


# ================================
# 2. 导入方式对比
# ================================

print("\n导入方式对比:")

# 方式 1：导入整个模块
import math
print(f"方式 1 - math.pi = {math.pi}")

# 方式 2：导入特定函数
from math import sqrt, pow
print(f"方式 2 - sqrt(16) = {sqrt(16)}")

# 方式 3：导入所有（不推荐）
from math import *
print(f"方式 3 - log10(100) = {log10(100)}")

# 方式 4：使用别名
import numpy as np
print(f"方式 4 - numpy array: {np.array([1, 2, 3])}")


# ================================
# 3. 模块搜索路径
# ================================

print("\n模块搜索路径:")
for i, path in enumerate(sys.path[:5], 1):
    print(f"{i}. {path}")


# ================================
# 4. 创建自定义模块
# ================================

# 创建一个临时模块文件
import tempfile
import os

# 创建临时目录
temp_dir = tempfile.mkdtemp()
module_file = os.path.join(temp_dir, "my_module.py")

# 写入模块代码
with open(module_file, "w", encoding="utf-8") as f:
    f.write("""
\"\"\"自定义模块示例\"\"\"

# 模块变量
MODULE_NAME = "MyModule"
VERSION = "1.0.0"

# 模块函数
def greet(name: str) -> str:
    \"\"\"问候函数\"\"\"
    return f"Hello, {name}!"

# 模块类
class Calculator:
    \"\"\"计算器类\"\"\"
    
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

# 私有函数（约定，非强制）
def _internal_function():
    return "This is internal"
""")

# 将临时目录添加到搜索路径
sys.path.insert(0, temp_dir)

# 导入自定义模块
import my_module

print(f"\n自定义模块:")
print(f"模块名: {my_module.MODULE_NAME}")
print(f"版本: {my_module.VERSION}")
print(f"问候: {my_module.greet('张三')}")
print(f"计算: {my_module.Calculator.add(3, 5)}")


# ================================
# 5. 包结构（Package）
# ================================

# 创建包结构
package_dir = os.path.join(temp_dir, "my_package")
os.makedirs(package_dir, exist_ok=True)

# 创建 __init__.py 文件
init_file = os.path.join(package_dir, "__init__.py")
with open(init_file, "w", encoding="utf-8") as f:
    f.write("""
\"\"\"我的包\"\"\"

from .module_a import func_a
from .module_b import func_b

__version__ = "1.0.0"
__all__ = ["func_a", "func_b"]
""")

# 创建模块 A
module_a_file = os.path.join(package_dir, "module_a.py")
with open(module_a_file, "w", encoding="utf-8") as f:
    f.write("""
def func_a():
    return "Function A"
""")

# 创建模块 B
module_b_file = os.path.join(package_dir, "module_b.py")
with open(module_b_file, "w", encoding="utf-8") as f:
    f.write("""
def func_b():
    return "Function B"
""")

# 导入包
import my_package

print(f"\n包导入:")
print(f"包版本: {my_package.__version__}")
print(f"func_a: {my_package.func_a()}")
print(f"func_b: {my_package.func_b()}")


# ================================
# 6. pip 包管理
# ================================

print("\n包管理命令（pip）:")

# 在命令行执行：
# pip install package_name     # 安装包
# pip uninstall package_name   # 卸载包
# pip list                     # 列出已安装的包
# pip freeze > requirements.txt  # 导出依赖
# pip install -r requirements.txt # 安装依赖

# 查看当前环境已安装的包
import subprocess
result = subprocess.run(
    ["pip", "list"],
    capture_output=True,
    text=True,
    cwd=os.getcwd()
)

print("已安装的包（前 10 个）:")
lines = result.stdout.split('\n')
for line in lines[:12]:
    print(f"  {line}")


# ================================
# 7. requirements.txt 管理
# ================================

print("\nrequirements.txt 示例:")

requirements_content = """
# AI Agent 学习项目依赖

# LLM SDK
openai>=1.0.0
anthropic>=0.18.0

# Agent 框架
langchain>=0.1.0
langgraph>=0.0.20

# 向量数据库
pymilvus>=2.3.0

# 开发工具
jupyter>=1.0.0
pytest>=7.0.0
"""

print(requirements_content)

# 安装依赖：
# pip install -r requirements.txt


# ================================
# 8. 相对导入和绝对导入
# ================================

print("\n导入方式:")

# 绝对导入（推荐）
# from my_package.module_a import func_a

# 相对导入（在包内部使用）
# from .module_a import func_a
# from ..module_b import func_b


# ================================
# 9. 模块的 __name__ 属性
# ================================

# 创建一个可执行的模块
executable_module = os.path.join(temp_dir, "executable.py")
with open(executable_module, "w", encoding="utf-8") as f:
    f.write("""
def main():
    print("模块作为脚本运行")

if __name__ == "__main__":
    main()
else:
    print("模块被导入")
""")

# 作为脚本运行
print("\n模块执行测试:")
import subprocess
import sys
result = subprocess.run(
    [sys.executable, "executable.py"],
    capture_output=True,
    text=True,
    cwd=temp_dir,
    check=False,
)
print(f"脚本输出: {result.stdout.strip()}")

# 作为模块导入
import executable


# ================================
# 10. 模块的常用属性
# ================================

print(f"\n模块属性:")
print(f"模块名: {os.__name__}")
print(f"模块文件: {os.__file__}")
print(f"模块文档: {os.__doc__[:50]}...")
print(f"模块属性列表: {[attr for attr in dir(os) if not attr.startswith('_')][:10]}")


# ================================
# 11. 第三方包使用示例
# ================================

print("\n第三方包示例:")

# requests 库（已安装）
import requests

# 检查是否安装成功
try:
    response = requests.get("https://www.baidu.com", timeout=5)
    print(f"requests 测试: HTTP {response.status_code}")
except Exception as e:
    print(f"requests 测试失败: {e}")


# ================================
# 12. 虚拟环境管理
# ================================

print("\n虚拟环境管理:")

# 创建虚拟环境
# python -m venv .venv

# 激活虚拟环境
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\\Scripts\\activate

# 退出虚拟环境
# deactivate

# 当前虚拟环境信息
import sys
print(f"Python 可执行文件: {sys.executable}")
print(f"虚拟环境: {sys.prefix}")


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)

# 练习 1：创建一个计算器模块
calculator_module = os.path.join(temp_dir, "calculator.py")
with open(calculator_module, "w", encoding="utf-8") as f:
    f.write("""
\"\"\"计算器模块\"\"\"

def add(a: float, b: float) -> float:
    \"\"\"加法\"\"\"
    return a + b

def subtract(a: float, b: float) -> float:
    \"\"\"减法\"\"\"
    return a - b

def multiply(a: float, b: float) -> float:
    \"\"\"乘法\"\"\"
    return a * b

def divide(a: float, b: float) -> float:
    \"\"\"除法\"\"\"
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
""")

import calculator
print(f"练习 1 - 计算器: 10 + 5 = {calculator.add(10, 5)}")


# 练习 2：创建一个包，包含字符串处理工具
string_package = os.path.join(temp_dir, "string_tools")
os.makedirs(string_package, exist_ok=True)

with open(os.path.join(string_package, "__init__.py"), "w", encoding="utf-8") as f:
    f.write("""
from .reverse import reverse_string
from .count import count_chars

__all__ = ["reverse_string", "count_chars"]
""")

with open(os.path.join(string_package, "reverse.py"), "w", encoding="utf-8") as f:
    f.write("""
def reverse_string(s: str) -> str:
    \"\"\"反转字符串\"\"\"
    return s[::-1]
""")

with open(os.path.join(string_package, "count.py"), "w", encoding="utf-8") as f:
    f.write("""
def count_chars(s: str) -> dict:
    \"\"\"统计字符\"\"\"
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result
""")

import string_tools
print(f"练习 2 - 反转字符串: {string_tools.reverse_string('hello')}")
print(f"练习 2 - 统计字符: {string_tools.count_chars('hello')}")


# 练习 3：使用 pip 命令列出所有已安装的包
print("\n练习 3 - 已安装的包（langchain 相关）:")
result = subprocess.run(
    ["pip", "list"],
    capture_output=True,
    text=True
)
for line in result.stdout.split('\n'):
    if 'langchain' in line.lower() or 'langgraph' in line.lower():
        print(f"  {line}")


# 练习 4：创建一个模块，包含主程序入口
main_module = os.path.join(temp_dir, "main_module.py")
with open(main_module, "w", encoding="utf-8") as f:
    f.write("""
\"\"\"主程序模块\"\"\"

def run():
    \"\"\"运行主程序\"\"\"
    print("主程序运行中...")

def helper():
    \"\"\"辅助函数\"\"\"
    return "Helper function"

if __name__ == "__main__":
    run()
""")

import main_module
print(f"练习 4 - 模块导入: {main_module.helper()}")


# 练习 5：创建一个包，模拟文件系统操作
filesystem_package = os.path.join(temp_dir, "filesystem")
os.makedirs(filesystem_package, exist_ok=True)

with open(os.path.join(filesystem_package, "__init__.py"), "w", encoding="utf-8") as f:
    f.write("""
from .operations import create_file, delete_file

__all__ = ["create_file", "delete_file"]
""")

with open(os.path.join(filesystem_package, "operations.py"), "w", encoding="utf-8") as f:
    f.write("""
import os

def create_file(filename: str, content: str = ""):
    \"\"\"创建文件\"\"\"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"文件已创建: {filename}"

def delete_file(filename: str):
    \"\"\"删除文件\"\"\"
    if os.path.exists(filename):
        os.remove(filename)
        return f"文件已删除: {filename}"
    return f"文件不存在: {filename}"
""")

import filesystem
test_file = os.path.join(temp_dir, "test.txt")
print(f"练习 5 - {filesystem.create_file(test_file, 'test content')}")
print(f"练习 5 - {filesystem.delete_file(test_file)}")


# 清理临时文件
import shutil
shutil.rmtree(temp_dir)

print("\n✅ Day 6 学习完成！")
print("要点总结：")
print("1. 模块导入：import、from...import、as 别名")
print("2. 包结构：__init__.py、__all__")
print("3. 包管理：pip install/uninstall/list/freeze")
print("4. 依赖管理：requirements.txt")
print("5. 模块属性：__name__、__file__、__doc__")
print("6. 虚拟环境：python -m venv .venv")
