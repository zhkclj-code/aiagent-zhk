# Python 学习路径（Java 开发者版）

> 从 Java 到 Python：高效学习路径

---

## 学习策略

### 你已经掌握的（Java 经验）

✅ **编程基础**：变量、函数、类、循环、条件判断
✅ **面向对象**：封装、继承、多态、接口
✅ **数据结构**：List、Map、Set
✅ **工程思维**：模块化、设计模式、测试

### 你需要学习的（Python 特色）

❌ **动态类型**：Python 的类型系统
❌ **语法特性**：列表推导式、装饰器、上下文管理器
❌ **异步编程**：asyncio、async/await
❌ **工程化**：包管理、类型注解、测试框架

---

## 学习路径（按优先级）

### 第 1 周：Python 基础（3-4 天）

#### Day 1：语法对比（Python vs Java）

**学习内容**：
1. 变量和类型（动态类型 vs 静态类型）
2. 函数定义（def vs public static）
3. 条件判断和循环
4. 基本数据结构（list、dict、tuple、set）

**练习项目**：
- `code/python-basics/01-syntax/` - 语法对比练习

---

#### Day 2：Python 特色语法

**学习内容**：
1. 列表推导式（List Comprehension）
2. 字典推导式
3. Lambda 表达式
4. 函数参数（*args、**kwargs）

**练习项目**：
- `code/python-basics/02-features/` - 特色语法练习

---

#### Day 3：面向对象（Python 风格）

**学习内容**：
1. 类定义（Python vs Java）
2. 继承和多态
3. 魔法方法（__init__、__str__、__repr__）
4. 属性装饰器（@property）

**练习项目**：
- `code/python-basics/03-oop/` - 面向对象练习

---

### 第 2 周：进阶特性（3-4 天）

#### Day 4：装饰器和上下文管理器

**学习内容**：
1. 装饰器原理和应用
2. 常用装饰器（@staticmethod、@classmethod、@property）
3. 上下文管理器（with 语句）
4. 资源管理（文件、数据库连接）

**练习项目**：
- `code/python-basics/04-decorators/` - 装饰器练习

---

#### Day 5：异常处理和文件操作

**学习内容**：
1. 异常处理（try-except vs try-catch）
2. 自定义异常
3. 文件读写（with open）
4. JSON/CSV 文件处理

**练习项目**：
- `code/python-basics/05-exceptions/` - 异常处理练习

---

#### Day 6：模块和包管理

**学习内容**：
1. 模块导入（import vs Java import）
2. 包结构（__init__.py）
3. 第三方包管理（pip、requirements.txt）
4. 虚拟环境（venv）

**练习项目**：
- `code/python-basics/06-modules/` - 模块练习

---

### 第 3 周：异步编程（重点）

#### Day 7-8：异步编程基础

**学习内容**：
1. 同步 vs 异步（概念理解）
2. asyncio 基础
3. async/await 语法
4. 并发 vs 并行

**练习项目**：
- `code/python-basics/07-async/` - 异步编程练习

---

#### Day 9：异步编程实战

**学习内容**：
1. 并发调用多个 API
2. 异步上下文管理器
3. 异步生成器
4. 性能对比（同步 vs 异步）

**练习项目**：
- `code/python-basics/08-async-practice/` - 异步实战

---

### 第 4 周：工程化实践

#### Day 10：类型注解（Type Hints）

**学习内容**：
1. 类型注解语法（Python 3.5+）
2. 基本类型注解（int、str、List、Dict）
3. 类型联合（Union[A, B] vs A | B）
4. Pydantic 数据验证

**练习项目**：
- `code/python-basics/09-type-hints/` - 类型注解练习

---

#### Day 11：测试框架

**学习内容**：
1. pytest 基础
2. 单元测试编写
3. 测试夹具（fixtures）
4. 测试覆盖率

**练习项目**：
- `code/python-basics/10-testing/` - 测试练习

---

#### Day 12：综合项目

**学习内容**：
1. 项目结构最佳实践
2. 代码风格（PEP 8、Black）
3. 文档编写（Docstring）
4. 版本控制（Git）

**练习项目**：
- `code/python-basics/11-project/` - 综合项目

---

## 学习方法

### 每天学习流程

**理论学习**（30-60 分钟）：
- 阅读官方文档或教程
- 理解核心概念

**动手练习**（60-120 分钟）：
- 编写示例代码
- 对比 Python 和 Java 的差异
- 完成练习项目

**笔记整理**（15-30 分钟）：
- 记录关键差异
- 总结易错点

---

## 学习资源

### 官方文档
- [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- [Python 标准库](https://docs.python.org/zh-cn/3/library/)

### 推荐书籍
- 《Python 编程：从入门到实践》
- 《流畅的 Python》（进阶）

### 视频课程
- [Python for Java Developers](https://www.youtube.com/results?search_query=python+for+java+developers)

### 在线练习
- [LeetCode Python 练习](https://leetcode.cn/)
- [HackerRank Python](https://www.hackerrank.com/domains/tutorials/10-days-of-python)

---

## Python vs Java 核心差异

| 特性 | Java | Python |
|------|------|--------|
| **类型系统** | 静态类型 | 动态类型 |
| **变量声明** | `String name = "张三";` | `name = "张三"` |
| **代码块** | `{}` 大括号 | 缩进 |
| **分号** | 必须有 `;` | 不需要 |
| **函数定义** | `public void func()` | `def func():` |
| **继承** | `class Child extends Parent` | `class Child(Parent):` |
| **接口** | `interface` | 无接口，用抽象类 |
| **泛型** | `<T>` | 无泛型，用类型注解 |
| **多线程** | Thread、Runnable | asyncio（异步） |
| **包管理** | Maven、Gradle | pip、requirements.txt |
| **代码风格** | 驼峰命名 | 蛇形命名（my_function） |

---

## 重点学习内容

### 1. 动态类型理解

**Java（静态类型）**：
```java
String name = "张三";  // 编译时确定类型
name = 123;  // ❌ 编译错误
```

**Python（动态类型）**：
```python
name = "张三"  # 运行时确定类型
name = 123     # ✅ 允许，类型改变
```

---

### 2. 列表推导式

**Java**：
```java
List<Integer> squares = new ArrayList<>();
for (int i = 0; i < 10; i++) {
    squares.add(i * i);
}
```

**Python**：
```python
squares = [i * i for i in range(10)]  # 一行搞定
```

---

### 3. 装饰器

**Java（注解）**：
```java
@Override
public String toString() {
    return "MyClass";
}
```

**Python（装饰器）**：
```python
@property
def name(self):
    return self._name
```

---

### 4. 异步编程

**Java（多线程）**：
```java
ExecutorService executor = Executors.newFixedThreadPool(10);
Future<String> future = executor.submit(() -> fetchData());
```

**Python（异步）**：
```python
async def fetch_data():
    await asyncio.sleep(1)
    return "data"

results = await asyncio.gather(fetch_data(), fetch_data())
```

---

## 学习建议

### 不要做的事
❌ 不要把 Java 的习惯带到 Python（如过度使用类）
❌ 不要忽略 Python 的特色语法（如列表推导式）
❌ 不要跳过异步编程（Agent 开发必备）

### 要做的事
✅ 多写代码，对比 Python 和 Java 的差异
✅ 掌握 Python 的"Pythonic"写法
✅ 重点学习异步编程（后续 Agent 开发关键）
✅ 使用类型注解（提高代码可读性）

---

**现在开始学习！先从第 1 天的语法对比开始。**