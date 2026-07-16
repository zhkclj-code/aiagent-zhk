"""
Day 15: 生成器 & 正则 & pathlib

学习目标：掌握生成器（yield）、正则表达式（re）、现代路径处理（pathlib）
"""

import re
import sys
from pathlib import Path
from typing import Iterator, Generator


# ================================
# 0. Generator核心概念 - Java开发者必读
# ================================

"""
【什么是生成器】
生成器是一种特殊的迭代器，使用yield关键字逐个产出值。
核心特性：惰性求值（Lazy Evaluation）+ 固定内存开销。

【Generator vs Java Stream/Iterator对比】

| 特性 | Python Generator | Java Stream | Java Iterator |
|-----|-----------------|------------|-------------|
| 语法 | yield关键字 | Stream API | Iterator接口 |
| 惰性求值 | ✅ 天然支持 | ✅ 支持 | ✅ 支持 |
| 无限序列 | ✅ 支持 | ✅ 支持 | ✅ 支持 |
| 管道操作 | ❌ 无内置 | ✅ filter/map/reduce | ❌ 无 |
| 并行处理 | ❌ 不支持 | ✅ parallelStream() | ❌ 不支持 |
| 内存开销 | ~100 bytes | ~100 bytes | ~100 bytes |
| 多次遍历 | ❌ 一次性 | ❌ 一次性 | ❌ 一次性 |

【核心差异】

1. 语法风格：
   Python:
   def squares(n):
       for i in range(n):
           yield i * i

   Java Stream:
   IntStream.range(0, n)
            .map(i -> i * i)
            .forEach(System.out::println);

2. 管道操作：
   Java Stream有丰富的中间操作：
   list.stream()
       .filter(x -> x > 10)
       .map(x -> x * 2)
       .sorted()
       .collect(Collectors.toList());

   Python生成器需要手写循环：
   (x * 2 for x in list if x > 10)  # 生成器表达式

3. 并行处理：
   Java:
   list.parallelStream().map(...)

   Python:
   无内置并行（可用multiprocessing替代）

【内存效率对比】

处理1,000,000个数字：

Python:
def squares(n):
    for i in range(n):
        yield i * i

gen = squares(1_000_000)
# 内存占用：~100 bytes（固定开销）

Java Stream:
IntStream squares = IntStream.range(0, 1_000_000).map(i -> i * i);
// 内存占用：~100 bytes（固定开销）

Java List:
List<Integer> list = new ArrayList<>();
for (int i = 0; i < 1_000_000; i++) {
    list.add(i * i);
}
// 内存占用：~40 MB（存储所有元素）

【使用场景】

✅ Python Generator适用：
- 大文件读取（逐行处理）
- 数据流处理（LLM流式输出）
- 无限序列（数学序列、传感器数据）
- 内存敏感场景（处理GB级文件）

✅ Java Stream适用：
- 集合转换和过滤
- 并行数据处理
- 函数式编程风格
- 复杂的管道操作

【核心概念】

yield关键字：
- 暂停函数执行，返回一个值
- 保存函数状态（局部变量、执行位置）
- 下次调用从yield后继续执行

def count_up(n):
    for i in range(n):
        yield i  # 暂停，返回i
        # 下次调用从这里继续

# 执行流程：
gen = count_up(3)  # 创建生成器对象
next(gen)  # 执行到yield，返回0
next(gen)  # 从上次yield后继续，返回1
next(gen)  # 返回2
next(gen)  # StopIteration异常

【和Java Iterator的区别】

Java Iterator:
public interface Iterator<E> {
    boolean hasNext();
    E next();
}

Python Generator:
- 自动实现__iter__和__next__
- 无需手写hasNext逻辑
- 函数结束时自动抛出StopIteration

【最佳实践】

1. 大数据流式处理：
   def read_large_file(file_path):
       with open(file_path) as f:
           for line in f:
               yield line.strip()

2. 无限序列：
   def fibonacci():
       a, b = 0, 1
       while True:
           yield a
           a, b = b, a + b

3. yield from（委托生成器）：
   def chain(*iterables):
       for it in iterables:
           yield from it

【常见陷阱】

1. 生成器是一次性的：
   gen = (x for x in range(3))
   list(gen)  # [0, 1, 2]
   list(gen)  # []（已耗尽）

2. 无法获取长度：
   gen = (x for x in range(100))
   len(gen)  # TypeError

3. 无法回溯：
   gen = (x for x in range(5))
   next(gen)  # 0
   # 无法回到开始，只能继续向前

【Java开发者迁移建议】

Java Stream API → Python Generator
─────────────────────────────────────
stream.filter() → (x for x in gen if condition)
stream.map() → (f(x) for x in gen)
stream.forEach() → for x in gen: ...
stream.collect() → list(gen)
Stream.iterate() → while True: yield
parallelStream() → multiprocessing.Pool

【性能考量】

生成器开销：
- 优点：固定内存，适合大数据
- 缺点：每次yield有函数调用开销

列表开销：
- 优点：O(1)随机访问，可重复遍历
- 缺点：内存随元素数量增长

决策：
- 数据量小（<1000）且需多次访问 → 用列表
- 数据量大（>10000）或流式处理 → 用生成器
- 需要随机访问 → 用列表
- 只需顺序遍历 → 用生成器
"""

# ================================
# Part A: 生成器（yield）
# ================================

# 1. 生成器基础
# 普通函数：一次性返回所有结果
def get_squares_normal(n: int) -> list[int]:
    result = []
    for i in range(n):
        result.append(i * i)
    return result

# 生成器函数：逐个产出结果（懒惰求值）
def get_squares_generator(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i * i


print("生成器 vs 列表:")
print(f"  列表: {get_squares_normal(5)}    ← 一次性生成全部")
print(f"  生成器: {list(get_squares_generator(5))}  ← 逐个产出")


# 2. 生成器节省内存
print("\n内存对比:")
normal = get_squares_normal(1_000_000)
gen = get_squares_generator(1_000_000)
print(f"  列表占用: {sys.getsizeof(normal) / 1024 / 1024:.1f} MB")
print(f"  生成器占用: {sys.getsizeof(gen)} bytes（固定开销）")


# 3. 流式处理（Agent 场景）
def chunk_text(text: str, chunk_size: int = 10) -> Generator[str, None, None]:
    """将长文本分块（模拟 LLM 流式输出）"""
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]


text = "这是一段模拟LLM流式输出的长文本用来演示生成器的实际应用场景"
print("\n流式输出:")
for chunk in chunk_text(text, 8):
    print(f"  → {chunk}")


# 4. 无限生成器
def fibonacci() -> Generator[int, None, None]:
    """无限斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n无限生成器（前 10 个）:")
fib = fibonacci()
fib_list = [next(fib) for _ in range(10)]
print(f"  {fib_list}")


# 5. 生成器表达式
# 类似列表推导式，但用 () 而不是 []
squares_gen = (i * i for i in range(5))
evens_gen = (i for i in range(20) if i % 2 == 0)

print("\n生成器表达式:")
print(f"  平方: {list(squares_gen)}")
print(f"  偶数: {list(evens_gen)}")


# ================================
# Part B: 正则表达式（re）
# ================================

# 1. 基础匹配
text = "联系邮箱: zhangsan@example.com, 电话: 13812345678"

# search：查找第一个匹配
email_match = re.search(r"[\w.]+@[\w.]+", text)
print(f"\n提取邮箱: {email_match.group() if email_match else '未找到'}")

# findall：查找所有匹配
phone_match = re.findall(r"\d{11}", text)
print(f"提取电话: {phone_match}")

# match：从字符串开头匹配
print(f"开头匹配: {re.match(r'联系', text).group() if re.match(r'联系', text) else '未匹配'}")


# 2. 分组捕获
text = "2024-07-15 14:30:00"
pattern = r"(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})"
match = re.search(pattern, text)

if match:
    print(f"\n分组捕获:")
    print(f"  完整: {match.group(0)}")
    print(f"  日期: {match.group(1)}-{match.group(2)}-{match.group(3)}")
    print(f"  时间: {match.group(4)}:{match.group(5)}:{match.group(6)}")


# 3. 命名分组
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, "2024-07-15")
if match:
    print(f"\n命名分组: {match.group('year')}年{match.group('month')}月{match.group('day')}日")


# 4. Agent 场景：提取 LLM 输出中的代码块
llm_output = """
以下是 Python 代码：

```python
def hello():
    print("Hello, World!")
```

你可以直接运行这段代码。
"""

code_blocks = re.findall(r"```python\n(.*?)```", llm_output, re.DOTALL)
print(f"\n提取代码块:")
for i, block in enumerate(code_blocks, 1):
    print(f"  --- 代码块 {i} ---")
    print(block.strip())


# 5. 解析多行结构化输出
llm_response = """
TOOL: search_weather
ARGS: {"city": "北京", "date": "2024-07-15"}
RESULT: {"temperature": 35, "condition": "晴天"}
---
TOOL: search_air_quality
ARGS: {"city": "北京"}
RESULT: {"aqi": 85, "level": "良"}
"""

tool_calls = re.findall(
    r"TOOL: (\w+)\nARGS: ({[^}]+})\nRESULT: ({[^}]+})",
    llm_response
)

print(f"\n解析 Agent 工具调用记录:")
for tool, args, result in tool_calls:
    print(f"  工具: {tool}, 参数: {args}, 结果: {result}")


# 6. sub：替换
text = "价格是 ￥199 和 ￥299"
result = re.sub(r"￥(\d+)", r"¥\1", text)
print(f"\n替换: {text} → {result}")

# 7. split：正则分割
text = "apple,  banana; orange  ,grape"
fruits = re.split(r"[;,]\s*", text)
print(f"正则分割: {fruits}")


# ================================
# Part C: pathlib（现代路径处理）
# ================================

# os.path（旧）
# pathlib（新，Python 3.4+）

# 1. 路径创建
p = Path("/Users/admin/projects/agent/main.py")
print(f"\n路径对象: {p}")
print(f"  文件名: {p.name}")
print(f"  后缀: {p.suffix}")
print(f"  父目录: {p.parent}")
print(f"  所有部分: {p.parts}")


# 2. 路径操作（用 / 拼接）
base = Path("/Users/admin/IdeaProjects/python-pros/aiagent-step1")
code_dir = base / "code" / "python-basics"
log_file = base / "logs" / "agent.log"

print(f"\n路径拼接:")
print(f"  code 目录: {code_dir}")
print(f"  日志文件: {log_file}")


# 3. 遍历目录
print(f"\n当前目录 Python 文件:")

current = Path(".").resolve()
for py_file in sorted(current.glob("code/python-basics/**/*.py"))[:8]:
    print(f"  {py_file}")


# 4. 读写文件
demo_file = Path("/tmp") / "pathlib_demo.txt"
demo_file.write_text("Pathlib example\n第二行", encoding="utf-8")

content = demo_file.read_text(encoding="utf-8")
print(f"\n文件内容:\n{content}")
demo_file.unlink()  # 删除文件


# 5. 检查路径
print(f"\n路径检查:")
print(f"  exists: {code_dir.exists()}")
print(f"  is_dir:  {code_dir.is_dir()}")
print(f"  is_file: {code_dir.is_file()}")


# 6. 创建目录
log_dir = base / "temp_dir"
log_dir.mkdir(exist_ok=True)
(log_dir / "temp.txt").write_text("test")
print(f"\n创建目录: {log_dir}")
# 清理
import shutil
shutil.rmtree(log_dir)


# ================================
# 练习题
# ================================

print("\n" + "=" * 60)
print("练习题")
print("=" * 60)

# 练习 1：生成器实现分页
def paginate(items: list, page_size: int) -> Generator[list, None, None]:
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

data = list(range(25))
print("练习 1 - 分页（每页 10 条）:")
for page_num, page in enumerate(paginate(data, 10), 1):
    print(f"  第 {page_num} 页: {page}")


# 练习 2：正则提取 Markdown 链接
md_text = """
[Python](https://python.org) 是一种语言。
[LangChain](https://langchain.com) 是 Agent 框架。
"""
links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", md_text)
print("\n练习 2 - Markdown 链接:")
for name, url in links:
    print(f"  {name}: {url}")


# 练习 3：pathlib 统计项目代码
py_count = len(list(Path("code").rglob("*.py")))
total_lines = sum(
    len(f.read_text(encoding="utf-8").splitlines())
    for f in Path("code").rglob("*.py")
)
print(f"\n练习 3 - 项目统计: {py_count} 个 .py 文件, 共 {total_lines} 行代码")


print("\n✅ Day 15 学习完成！")
print("要点总结：")
print("1. yield：逐个产出，懒惰求值，省内存")
print("2. 生成器表达式：(x for x in ...) 替代列表推导式")
print("3. re 常用：search/findall/sub/split + 分组捕获")
print("4. re.DOTALL 让 . 匹配换行符")
print("5. pathlib / 拼接路径，比 os.path.join 更直观")
print("6. Path.glob 遍历目录，Path.read_text 读写文件")
