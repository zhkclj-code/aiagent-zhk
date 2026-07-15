"""
Day 11: 测试框架

学习目标：掌握 Python 测试框架 pytest
"""

# ================================
# 1. pytest 基础
# ================================

# 安装 pytest：
# pip install pytest pytest-cov

# 创建测试文件：test_*.py 或 *_test.py
# 运行测试：pytest test_example.py

import pytest


# 简单的函数测试
def add(a: int, b: int) -> int:
    """加法函数"""
    return a + b


def test_add():
    """测试加法函数"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


# 运行测试（在终端执行）
# pytest test_example.py -v


# ================================
# 2. 断言类型
# ================================

def test_assertions():
    """测试各种断言"""
    # 相等断言
    assert 1 + 1 == 2
    
    # 不等断言
    assert 1 + 1 != 3
    
    # 布尔断言
    assert True
    assert not False
    
    # 包含断言
    assert 1 in [1, 2, 3]
    assert "hello" in "hello world"
    
    # 类型断言
    assert isinstance("hello", str)
    assert isinstance(42, int)
    
    # 异常断言
    with pytest.raises(ZeroDivisionError):
        10 / 0


# ================================
# 3. 参数化测试
# ================================

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add_parametrize(a: int, b: int, expected: int):
    """参数化测试"""
    assert add(a, b) == expected


# 多个参数组合
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_multiply(x: int, y: int):
    """多参数组合测试"""
    assert x * y == x * y


# ================================
# 4. 测试夹具（Fixtures）
# ================================

@pytest.fixture
def sample_data():
    """测试数据夹具"""
    return [1, 2, 3, 4, 5]


def test_with_fixture(sample_data):
    """使用夹具的测试"""
    assert len(sample_data) == 5
    assert sum(sample_data) == 15


# 夹具的作用域
@pytest.fixture(scope="function")
def function_scope():
    """函数级夹具（每个测试函数创建一次）"""
    print("\n  创建函数级夹具")
    yield {"data": "function"}
    print("\n  清理函数级夹具")


@pytest.fixture(scope="class")
def class_scope():
    """类级夹具（每个测试类创建一次）"""
    print("\n  创建类级夹具")
    yield {"data": "class"}
    print("\n  清理类级夹具")


@pytest.fixture(scope="module")
def module_scope():
    """模块级夹具（每个模块创建一次）"""
    print("\n  创建模块级夹具")
    yield {"data": "module"}
    print("\n  清理模块级夹具")


def test_scope_example(function_scope, class_scope, module_scope):
    """测试夹具作用域"""
    assert function_scope["data"] == "function"
    assert class_scope["data"] == "class"
    assert module_scope["data"] == "module"


# ================================
# 5. 测试类
# ================================

class TestCalculator:
    """计算器测试类"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """每个测试方法前执行"""
        self.calculator = Calculator()
    
    def test_add(self):
        """测试加法"""
        assert self.calculator.add(1, 2) == 3
    
    def test_subtract(self):
        """测试减法"""
        assert self.calculator.subtract(5, 3) == 2
    
    def test_multiply(self):
        """测试乘法"""
        assert self.calculator.multiply(3, 4) == 12


class Calculator:
    """计算器类"""
    
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b
    
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b


# ================================
# 6. 异常测试
# ================================

def divide(a: int, b: int) -> float:
    """除法函数"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def test_divide_by_zero():
    """测试除零异常"""
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    
    assert str(exc_info.value) == "除数不能为零"


def test_divide_normal():
    """测试正常除法"""
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0


# ================================
# 7. 跳过和标记测试
# ================================

@pytest.mark.skip(reason="暂时跳过")
def test_skip():
    """跳过的测试"""
    assert False


@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason="需要 Python 3.10+"
)
def test_skipif():
    """条件跳过"""
    assert True


@pytest.mark.xfail(reason="预期失败")
def test_expected_failure():
    """预期失败的测试"""
    assert 1 == 2  # 这个测试预期失败


# ================================
# 8. 测试覆盖率
# ================================

# 运行覆盖率测试：
# pytest --cov=my_module --cov-report=html

# 安装：
# pip install pytest-cov


# ================================
# 9. Mock 和 Patch
# ================================

from unittest.mock import Mock, patch, MagicMock


def get_user_name(user_id: int) -> str:
    """获取用户名（模拟 API 调用）"""
    # 实际应该调用 API
    return f"User_{user_id}"


def test_with_mock():
    """使用 Mock 测试"""
    # 创建 Mock 对象
    mock_api = Mock()
    mock_api.get_user_name.return_value = "Mock User"
    
    # 使用 Mock
    result = mock_api.get_user_name(1)
    assert result == "Mock User"
    
    # 验证调用
    mock_api.get_user_name.assert_called_once_with(1)


@patch('__main__.get_user_name')
def test_with_patch(mock_get_user):
    """使用 Patch 测试"""
    # 设置 Mock 返回值
    mock_get_user.return_value = "Patched User"
    
    # 调用函数
    result = get_user_name(1)
    assert result == "Patched User"


# ================================
# 10. 测试组织
# ================================

# 项目结构：
"""
my_project/
├── src/
│   └── my_module.py
└── tests/
    ├── __init__.py
    ├── conftest.py          # 共享夹具
    ├── test_module_a.py
    └── test_module_b.py
"""

# conftest.py 示例：
"""
import pytest

@pytest.fixture(scope="session")
def db_connection():
    \"\"\"数据库连接夹具\"\"\"
    conn = create_connection()
    yield conn
    conn.close()
"""


# ================================
# 11. 测试运行命令
# ================================

# 运行所有测试
# pytest

# 运行特定文件
# pytest test_example.py

# 运行特定测试函数
# pytest test_example.py::test_add

# 运行特定测试类
# pytest test_example.py::TestCalculator

# 显示打印输出
# pytest -s

# 详细输出
# pytest -v

# 失败时停止
# pytest -x

# 失败次数达到 N 时停止
# pytest --maxfail=3

# 只运行标记的测试
# pytest -m "slow"

# 并行运行
# pytest -n auto


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)


# 练习 1：编写字符串处理函数的测试
def reverse_string(s: str) -> str:
    """反转字符串"""
    return s[::-1]


def test_reverse_string():
    """练习 1 - 测试字符串反转"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


# 练习 2：编写列表处理函数的测试
def filter_positive(numbers: list) -> list:
    """过滤正数"""
    return [n for n in numbers if n > 0]


@pytest.mark.parametrize("input_list, expected", [
    ([1, -1, 2, -2], [1, 2]),
    ([-1, -2, -3], []),
    ([0, 1, 2], [1, 2]),
])
def test_filter_positive(input_list, expected):
    """练习 2 - 测试过滤正数"""
    assert filter_positive(input_list) == expected


# 练习 3：编写异常测试
def set_age(age: int):
    """设置年龄"""
    if age < 0 or age > 150:
        raise ValueError("年龄无效")
    return age


def test_set_age_exception():
    """练习 3 - 测试年龄异常"""
    with pytest.raises(ValueError):
        set_age(-1)
    
    with pytest.raises(ValueError):
        set_age(200)
    
    assert set_age(25) == 25


# 练习 4：编写夹具测试
@pytest.fixture
def test_user():
    """测试用户夹具"""
    return {"name": "测试用户", "age": 25}


def test_user_fixture(test_user):
    """练习 4 - 使用夹具测试"""
    assert test_user["name"] == "测试用户"
    assert test_user["age"] == 25


# 练习 5：编写 Mock 测试
class ExternalAPI:
    """外部 API 类"""
    
    @staticmethod
    def call(data: str) -> str:
        """调用 API"""
        # 实际应该调用外部 API
        return f"Processed: {data}"


def test_api_mock():
    """练习 5 - Mock 测试"""
    mock_api = Mock(spec=ExternalAPI)
    mock_api.call.return_value = "Mocked Result"
    
    result = mock_api.call("test")
    assert result == "Mocked Result"
    mock_api.call.assert_called_once_with("test")


print("\n✅ Day 11 学习完成！")
print("要点总结：")
print("1. pytest 基础：assert 断言")
print("2. 参数化测试：@pytest.mark.parametrize")
print("3. 测试夹具：@pytest.fixture")
print("4. 测试类：class TestXxx")
print("5. 异常测试：pytest.raises()")
print("6. 跳过测试：@pytest.mark.skip")
print("7. 测试覆盖率：pytest --cov")
print("8. Mock 测试：unittest.mock")
print("9. 测试组织：tests/ 目录结构")
print("10. 运行命令：pytest 参数")


if __name__ == "__main__":
    import sys
    pytest.main([__file__, "-v"])