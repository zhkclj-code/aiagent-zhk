"""
Day 5: 异常处理和文件操作

学习目标：掌握 Python 异常处理和文件操作
"""

# ================================
# 0. 异常处理核心概念 - Java开发者必读
# ================================

"""
【Python异常 vs Java异常对比】

| 维度 | Python | Java |
|-----|--------|------|
| 检查类型 | 无检查型异常 | 检查型+非检查型 |
| 异常层次 | BaseException → Exception | Throwable → Exception/Error |
| 必须捕获 | 否 | 检查型异常必须捕获/声明 |
| try语法 | try/except/finally/else | try/catch/finally |
| 抛出异常 | raise Exception() | throw new Exception() |

【核心差异】

1. 检查型异常：
   Java:
   public void readFile() throws IOException {
       // 必须声明或捕获IOException
   }

   Python:
   def read_file():
       # 无需声明可能抛出的异常
       # 不强制捕获任何异常

2. 异常层次：
   Python:
   BaseException
   ├── SystemExit（sys.exit()）
   ├── KeyboardInterrupt（Ctrl+C）
   └── Exception（所有应用异常）
       ├── ValueError
       ├── TypeError
       └── IOError

   Java:
   Throwable
   ├── Error（JVM错误，不应捕获）
   └── Exception
       ├── IOException（检查型）
       ├── SQLException（检查型）
       └── RuntimeException（非检查型）
           ├── NullPointerException
           └── IllegalArgumentException

【最佳实践】

1. ❌ 不要使用裸except：
   # 错误示例：
   except:  # 会捕获所有异常，包括KeyboardInterrupt、SystemExit
       pass

   # 正确示例：
   except Exception as e:  # 只捕获Exception及其子类
       pass

2. ✅ 明确指定异常类型：
   # 好
   except FileNotFoundError as e:
       handle_file_error(e)

   # 不好
   except Exception:
       pass  # 吞掉所有异常

3. ✅ 使用异常链保留上下文：
   try:
       process_data()
   except ValueError as e:
       raise DataProcessingError("处理失败") from e
       # 保留原始异常的堆栈信息

4. ✅ 使用else子句（无异常时执行）：
   try:
       data = read_file()
   except FileNotFoundError:
       print("文件不存在")
   else:
       # 只有try块成功时才执行
       process(data)

5. ✅ 使用finally清理资源：
   try:
       f = open('file.txt')
       process(f)
   finally:
       f.close()  # 无论是否异常都会执行

   # 更好：使用with语句
   with open('file.txt') as f:
       process(f)  # 自动关闭

【异常处理原则】

1. 只捕获你能处理的异常
2. 不要用异常做流程控制
3. 在合适的层次捕获异常
4. 保留有意义的异常信息
5. 记录异常日志

【常见陷阱】

1. 捕获过于宽泛：
   ❌ except Exception:
   ✅ except (ValueError, TypeError):

2. 吞掉异常：
   ❌ except: pass
   ✅ except Exception as e: logger.error(...)

3. 忘记重新抛出：
   try:
       operation()
   except Exception as e:
       cleanup()
       # 忘记raise，异常被吞掉
       raise  # 重新抛出当前异常

【何时创建自定义异常】

✅ 需要自定义异常：
- 区分不同类型的错误
- 携带额外错误信息
- 特定异常需要特殊处理

示例：
class AgentError(Exception):
    \"\"\"Agent相关错误的基类\"\"\"
    pass

class ToolNotFoundError(AgentError):
    \"\"\"工具未找到\"\"\"
    def __init__(self, tool_name: str):
        self.tool_name = tool_name
        super().__init__(f"工具 '{tool_name}' 不存在")

class LLMTimeoutError(AgentError):
    \"\"\"LLM调用超时\"\"\"
    def __init__(self, timeout: float):
        self.timeout = timeout
        super().__init__(f"LLM调用超时 ({timeout}s)")

【Java开发者迁移建议】

try-catch-finally → try-except-finally-else
throws声明 → 无需声明
throw new X() → raise X()
catch(Exception e) → except Exception as e
catch(IOException | SQLException e) → except (IOError, SQLError) as e
"""

# ================================
# 1. 异常处理基础
# ================================

# Java 异常处理：
# try {
#     int result = 10 / 0;
# } catch (ArithmeticException e) {
#     System.out.println("数学错误: " + e.getMessage());
# } catch (Exception e) {
#     System.out.println("未知错误: " + e.getMessage());
# } finally {
#     System.out.println("清理资源");
# }

# Python 异常处理：
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"捕获除零错误: {e}")
except Exception as e:
    print(f"捕获其他错误: {e}")
finally:
    print("清理资源（总是执行）")


# ================================
# 2. 捕获多个异常
# ================================

def divide(a: int, b: int) -> float:
    """除法函数，处理多种异常"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return 0.0
    except TypeError as e:
        print(f"错误：类型不正确 - {e}")
        return 0.0
    except Exception as e:
        print(f"未知错误: {e}")
        return 0.0


# 测试
print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")
print(f"'10' / 2 = {divide('10', 2)}")


# ================================
# 3. else 和 finally 子句
# ================================

def safe_divide(a: int, b: int) -> float | None:
    """安全的除法函数"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数为零")
        return None
    else:
        # 没有异常时执行
        print(f"计算成功: {a} / {b} = {result}")
        return result
    finally:
        # 总是执行
        print("函数执行完毕")


print("\n测试 else 和 finally:")
safe_divide(10, 2)
safe_divide(10, 0)


# ================================
# 4. 抛出异常（raise）
# ================================

# Java 抛出异常：
# if (age < 0) {
#     throw new IllegalArgumentException("年龄不能为负数");
# }

# Python 抛出异常：
def set_age(age: int):
    """设置年龄"""
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不合理")
    print(f"年龄设置为: {age}")


# 测试抛出异常
try:
    set_age(25)   # 正常
    set_age(-5)   # 抛出异常
except ValueError as e:
    print(f"捕获异常: {e}")


# ================================
# 5. 自定义异常
# ================================

# Java 自定义异常：
# public class InvalidAgeException extends Exception {
#     public InvalidAgeException(String message) {
#         super(message);
#     }
# }

# Python 自定义异常：
class InvalidAgeError(Exception):
    """自定义异常：无效年龄"""
    def __init__(self, age: int, message: str = "年龄无效"):
        self.age = age
        self.message = message
        super().__init__(f"{message}: {age}")


def validate_age(age: int):
    """验证年龄"""
    if age < 0:
        raise InvalidAgeError(age, "年龄不能为负数")
    if age > 150:
        raise InvalidAgeError(age, "年龄超出合理范围")
    print(f"年龄验证通过: {age}")


# 测试自定义异常
try:
    validate_age(25)
    validate_age(200)
except InvalidAgeError as e:
    print(f"捕获自定义异常: {e}")
    print(f"无效的年龄值: {e.age}")


# ================================
# 6. 文件操作基础
# ================================

# Java 文件读取：
# try (BufferedReader br = new BufferedReader(new FileReader("test.txt"))) {
#     String line;
#     while ((line = br.readLine()) != null) {
#         System.out.println(line);
#     }
# } catch (IOException e) {
#     e.printStackTrace();
# }

# Python 文件读取（with 语句自动管理资源）：
import os

# 创建测试文件
test_file = "test_file.txt"
with open(test_file, "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

print("\n文件读取方式：")

# 方式 1：读取全部内容
print("1. 读取全部内容:")
with open(test_file, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 方式 2：逐行读取
print("2. 逐行读取:")
with open(test_file, "r", encoding="utf-8") as f:
    for line in f:
        print(f"  {line.strip()}")

# 方式 3：读取为列表
print("3. 读取为列表:")
with open(test_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"  共 {len(lines)} 行")


# ================================
# 7. 文件写入
# ================================

print("\n文件写入方式：")

# 覆盖写入（w 模式）
with open("output1.txt", "w", encoding="utf-8") as f:
    f.write("覆盖写入\n")
    f.write("第二行\n")

# 追加写入（a 模式）
with open("output2.txt", "a", encoding="utf-8") as f:
    f.write("追加写入\n")
    f.write("第二行\n")

# 读写模式（r+ 模式）
with open("output1.txt", "r+", encoding="utf-8") as f:
    content = f.read()
    f.write("\n追加内容\n")

print("文件写入完成")


# ================================
# 8. 处理文件异常
# ================================

def read_file_safe(filename: str) -> str | None:
    """安全的文件读取"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"错误：文件不存在 - {filename}")
        return None
    except PermissionError:
        print(f"错误：没有权限 - {filename}")
        return None
    except Exception as e:
        print(f"错误：{e}")
        return None


# 测试文件异常处理
print("\n文件异常处理测试:")
content = read_file_safe("nonexistent.txt")
content = read_file_safe(test_file)


# ================================
# 9. JSON 文件处理
# ================================

import json

# Python 对象
data = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "Java", "AI"],
    "is_active": True
}

# 写入 JSON 文件
json_file = "data.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nJSON 文件已保存: {json_file}")

# 读取 JSON 文件
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(f"读取的 JSON 数据: {loaded_data}")


# ================================
# 10. CSV 文件处理
# ================================

import csv

# 写入 CSV 文件
csv_file = "data.csv"
students = [
    {"name": "张三", "age": 25, "score": 88},
    {"name": "李四", "age": 30, "score": 92},
    {"name": "王五", "age": 28, "score": 85}
]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "score"])
    writer.writeheader()
    writer.writerows(students)

print(f"\nCSV 文件已保存: {csv_file}")

# 读取 CSV 文件
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("读取的 CSV 数据:")
    for row in reader:
        print(f"  {row}")


# ================================
# 11. 上下文管理器（with 语句）
# ================================

# 自定义上下文管理器
class Timer:
    """计时器上下文管理器"""
    
    def __enter__(self):
        """进入上下文"""
        import time
        self.start_time = time.time()
        print("计时开始...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        import time
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"计时结束，耗时: {elapsed:.2f} 秒")
        return False  # 不抑制异常


# 使用自定义上下文管理器
print("\n上下文管理器测试:")
with Timer():
    # 模拟耗时操作
    import time
    time.sleep(0.1)
    print("执行任务...")


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)

# 练习 1：编写函数，安全地将字符串转换为整数
def safe_str_to_int(s: str) -> int | None:
    """安全的字符串转整数"""
    try:
        return int(s)
    except ValueError as e:
        print(f"转换失败: {e}")
        return None

print(f"练习 1 - '123' 转换: {safe_str_to_int('123')}")
print(f"练习 1 - 'abc' 转换: {safe_str_to_int('abc')}")


# 练习 2：编写函数，读取文件并统计行数
def count_lines(filename: str) -> int:
    """统计文件行数"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return len(f.readlines())
    except FileNotFoundError:
        print(f"文件不存在: {filename}")
        return 0

print(f"练习 2 - 文件行数: {count_lines(test_file)}")


# 练习 3：编写函数，将字典列表写入 CSV 文件
def write_dict_to_csv(data: list[dict], filename: str):
    """将字典列表写入 CSV"""
    if not data:
        return
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"CSV 文件已保存: {filename}")

write_dict_to_csv(students, "exercise.csv")


# 练习 4：自定义异常类，验证邮箱格式
class InvalidEmailError(Exception):
    """无效邮箱异常"""
    pass

def validate_email(email: str):
    """验证邮箱格式"""
    if "@" not in email or "." not in email:
        raise InvalidEmailError(f"邮箱格式无效: {email}")
    print(f"邮箱验证通过: {email}")

try:
    validate_email("test@example.com")
    validate_email("invalid-email")
except InvalidEmailError as e:
    print(f"练习 4 - 捕获异常: {e}")


# 练习 5：使用上下文管理器，实现文件备份
class FileBackup:
    """文件备份上下文管理器"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.backup_file = f"{filename}.bak"
    
    def __enter__(self):
        """备份原文件"""
        import shutil
        try:
            shutil.copy(self.filename, self.backup_file)
            print(f"已备份: {self.backup_file}")
        except FileNotFoundError:
            print(f"原文件不存在，无需备份")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """恢复备份（如果出错）"""
        if exc_type:
            import shutil
            try:
                shutil.copy(self.backup_file, self.filename)
                print(f"已恢复备份")
            except FileNotFoundError:
                pass
        return False

print("\n练习 5 - 文件备份:")
with FileBackup(test_file):
    print("修改文件...")
    # 这里如果出错，会自动恢复备份

# 清理测试文件
import os
for f in ["test_file.txt", "output1.txt", "output2.txt", "data.json", "data.csv", "exercise.csv"]:
    if os.path.exists(f):
        os.remove(f)

print("\n✅ Day 5 学习完成！")
print("要点总结：")
print("1. 异常处理：try-except-finally-else")
print("2. 抛出异常：raise ValueError()")
print("3. 自定义异常：class MyError(Exception)")
print("4. 文件操作：with open() as f")
print("5. JSON/CSV：json.dump/load, csv.DictWriter/DictReader")
print("6. 上下文管理器：__enter__ 和 __exit__")