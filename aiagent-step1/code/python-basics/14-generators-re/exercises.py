"""
Day 15 练习：生成器 + 正则 + pathlib

说明：本文件只有练习题，没有答案。
      请参考 generators.py 查看示例和答案。
"""

import re
import shutil
from pathlib import Path
from typing import Generator, List


# ================================
# Part A: 生成器（yield）
# ================================

# 练习 A1：分批读取大文件
# ================================

# TODO: 创建生成器 read_batch(filepath: str, batch_size: int)
#       返回: Generator[List[str], None, None]
#       每次 yield batch_size 行（列表），最后一批也要 yield

# TODO: 创建测试文件 /tmp/batch_demo.txt，写入 10 行
# TODO: for 遍历 read_batch，打印每批内容


# 练习 A2：无限生成器
# ================================

# TODO: 创建 fibonacci() -> Generator[int, None, None]
#       无限生成斐波那契: 0, 1, 1, 2, 3, 5...

# TODO: for + enumerate 取前 15 个数并打印


# 练习 A3：生成器管道
# ================================

# TODO: 创建 read_lines(filename): 逐行 yield，去换行符
# TODO: 创建 filter_contains(lines, keyword): yield 包含 keyword 的行
# TODO: 创建 to_upper(lines): yield 大写后的行
# TODO: 创建测试文件 /tmp/pipe_demo.txt（几行不同内容）
# TODO: 组合: to_upper(filter_contains(read_lines(f), "apple"))，list 化打印


# ================================
# Part B: 正则表达式（re）
# ================================

# 练习 B1：提取邮箱
# ================================

text = "联系方式: zhangsan@example.com, lisi@company.cn, wangwu@gmail.com"

# TODO: re.findall 提取所有邮箱（字母/数字/_ + @ + 字母/数字/.）
# TODO: 打印结果


# 练习 B2：解析 Agent 工具调用
# ================================

llm_output = """
2024-07-15 14:30:00 - Tool: search_weather
2024-07-15 14:30:00 - Args: {"city": "北京"}
2024-07-15 14:30:01 - Tool: search_air_quality
2024-07-15 14:30:01 - Args: {"city": "北京"}
"""

# TODO: re.findall 提取所有 "Tool: xxx" 中的工具名
#       模式: "Tool: " 后面的单词
# TODO: 打印工具名列表


# 练习 B3：提取代码块
# ================================

response = """
```python
def hello():
    return "Hello!"
```

```python
def add(a, b):
    return a + b
```
"""

# TODO: re.findall 提取 ```python\n 和 ``` 之间的内容
#       提示: re.DOTALL 让 . 匹配换行
# TODO: 打印每段代码，.strip() 去掉首尾空白


# 练习 B4：替换与分割
# ================================

# TODO: re.sub 把 "价格: ￥199, 折扣: ￥149" 中的 ￥ 替换为 ¥
# TODO: re.split 把 "apple,  banana; orange  ,grape" 按逗号或分号分割
#       打印结果


# ================================
# Part C: pathlib
# ================================

# 练习 C1：遍历目录
# ================================

# TODO: Path(".").glob("*.py") 列出当前目录所有 .py 文件
# TODO: 打印每个文件名和文件大小（f.stat().st_size）


# 练习 C2：批量重命名
# ================================

# TODO: 创建 /tmp/pathlib_demo 目录（mkdir(exist_ok=True)）
# TODO: 循环创建 file_0.txt 到 file_4.txt，内容写 "content_{i}"
# TODO: iterdir() 遍历，打印文件名
# TODO: rename() 批量改为 new_file_0.txt...
# TODO: 再次遍历打印新文件名
# TODO: shutil.rmtree 清理


# ================================
# 综合练习
# ================================

# TODO: Path("code/python-basics").rglob("*.py") 找到所有 Python 文件
# TODO: 统计：文件数量 + 总行数
#       提示: sum(len(f.read_text().splitlines()) for f in ...)
# TODO: 打印结果


print("\n✅ Day 15 练习完成！")
