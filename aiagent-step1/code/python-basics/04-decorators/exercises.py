"""
Day 4 练习：装饰器和上下文管理器

说明：本文件只有练习题，没有答案。
      请参考 decorators.py 查看示例和答案。
"""
import time

# ================================
# 练习 1：创建简单装饰器
# ================================

# TODO: 创建装饰器 uppercase_decorator，将函数返回值转为大写
def uppercase_decorator(func):
    def warpper(*args, **keywords):
        rst = func(*args, **keywords)
        if isinstance(rst, str):
            return rst.upper()
        else:
            return rst
    # 需要返回warpper，否则被装饰的方法调用时会报错TypeError: 'NoneType' object is not callable，想到于给被装饰的函数包了一层，然后作为调用的方法执行，如果没return那就没函数调
    return warpper

@uppercase_decorator
def test_0() -> str:
    return 'hello'

rst = test_0()
print(f'rst = {rst}')


# TODO: 创建函数 get_message()，使用装饰器
@uppercase_decorator
def get_message():
    return 'python'


# TODO: 测试装饰器
print(f'{get_message()}')

# ================================
# 练习 2：计时装饰器
# ================================

# TODO: 创建装饰器 measure_time，测量函数执行时间
def measure_time(func):
    def warpper(*args, **kwargs):
        start = time.time()
        # note：原样转发参数，不能写成 func(args, kwargs)，会导致传参失败
        func(*args, **kwargs)
        end = time.time()
        print(f'函数{func}执行所用时长为{end-start}')
    return warpper

# TODO: 创建慢函数，使用装饰器测量时间
@measure_time
def exe_slow(sec):
    time.sleep(sec)

exe_slow(1)


# ================================
# 练习 3：验证装饰器
# ================================

# TODO: 创建装饰器 validate_input，验证函数参数为正数
def validate_input(func):
    def warpper(*args, **kwargs):
        valid = all(i > 0 for i in args)
        if not valid:
            raise ValueError('参数必须为正数')
        return func(*args, **kwargs)

    return warpper

# TODO: 创建函数 calculate_area(width, height)，使用装饰器
@validate_input
def calculate_area(width, height):
    return width * height

print(f'面积={calculate_area(2,3)}')

# ================================
# 练习 4：内置装饰器
# ================================

# TODO: 创建 Temperature 类，包含：
# - 属性：_celsius
# - @property celsius：getter
# - @celsius.setter：setter，验证温度范围
# - @property fahrenheit：计算华氏温度
class Temperature:

    def __init__(self, celsius) -> None:
        self._celsius = celsius
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > 1000 or value < 0:
            raise ValueError("参数必须0-1000")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius + 200

# TODO: 测试属性装饰器
t = Temperature(1)
t.celsius = 100
print(f't.fahrenheit = {t.fahrenheit}')

# ================================
# 练习 5：上下文管理器
# ================================

# TODO: 创建 FileManager 类，使用 __enter__ 和 __exit__ 管理文件
class FileManager:

    def __enter__(self):
        print('获取资源')
        # note:一定要返回self，因为with默认会触发这个，并且返回值赋值给变量f使用
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc is not None:
            print(f'发生异常{exc_type}, {exc}')
            print(f'tb = {tb}')
        print('释放资源')

    def write(self, path):
        if not isinstance(path, str):
            raise TypeError("只支持字符串类型")
        print(f'文件{path}开始写入')

# TODO: 测试文件管理器
with FileManager() as f:
    f.write('/usrs/admin/aa.txt')
    # note:能catch处理异常，最后exit能成功调用，但是最后异常还会在finally raise原样抛出对吧
    # f.write(1111)
    f.write("/aaa")

with FileManager() as f:
    f.write("/aaa")

# ================================
# 练习 6：contextlib
# ================================

# TODO: 使用 @contextmanager 创建计时上下文管理器
from contextlib import contextmanager

@contextmanager
def exe_test1():
    start = time.time()
    yield
    end = time.time()
    print(f'耗时 = {end-start}')

# TODO: 测试上下文管理器
with exe_test1():
    time.sleep(1)
    print('开始测试')

# note：只有with才能用上下文管理并执行，否则只有exe_test1()不会按上下文管理顺序执行，只会创建包装的管理器对象contextlib._GeneratorContextManager
obj = exe_test1()
print(f'obj = {obj}')

# ================================
# 验证区域
# ================================

print("\n" + "="*60)
print("Day 4 练习验证")
print("="*60)

# 在这里添加验证代码

print("\n✅ 完成所有练习后，取消上面的注释并运行！")
