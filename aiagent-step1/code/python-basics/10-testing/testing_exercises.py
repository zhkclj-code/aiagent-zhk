"""
Day 11: 测试框架练习

学习目标：掌握 pytest 测试框架
"""


# ================================
# 练习 1：基础测试
# ================================
"""
任务：编写基础单元测试：

需要测试的函数（先实现）：
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

测试文件（test_math.py）：
def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(0, 5) == 0
    assert multiply(-1, 5) == -5

运行：pytest test_math.py
"""

# TODO: 在这里实现函数和测试




# ================================
# 练习 2：参数化测试
# ================================
"""
任务：使用 @pytest.mark.parametrize：

测试函数：
def is_even(n: int) -> bool:
    return n % 2 == 0

参数化测试：
@pytest.mark.parametrize("num, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-2, True),
    (-3, False)
])
def test_is_even(num, expected):
    assert is_even(num) == expected
"""

# TODO: 在这里实现参数化测试




# ================================
# 练习 3：测试异常
# ================================
"""
任务：测试函数抛出的异常：

函数：
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

测试：
def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert str(exc_info.value) == "除数不能为零"
"""

# TODO: 在这里实现异常测试




# ================================
# 练习 4：测试夹具
# ================================
"""
任务：使用 pytest.fixture：

夹具：
@pytest.fixture
def sample_users():
    return [
        {"id": 1, "name": "张三", "age": 25},
        {"id": 2, "name": "李四", "age": 30},
        {"id": 3, "name": "王五", "age": 35}
    ]

测试函数：
def get_user_by_id(users: List[Dict], user_id: int) -> Optional[Dict]:
    for user in users:
        if user["id"] == user_id:
            return user
    return None

测试：
def test_get_user_by_id(sample_users):
    user = get_user_by_id(sample_users, 1)
    assert user["name"] == "张三"
    
    user = get_user_by_id(sample_users, 999)
    assert user is None
"""

# TODO: 在这里实现测试夹具和测试




# ================================
# 练习 5：Mock 和补丁
# ================================
"""
任务：使用 unittest.mock：

场景：测试调用外部 API 的函数

函数：
def fetch_user_data(user_id: int) -> Dict:
    # 模拟调用 API
    import requests
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

测试：
from unittest.mock import Mock, patch

@patch('requests.get')
def test_fetch_user_data(mock_get):
    # 模拟 API 响应
    mock_response = Mock()
    mock_response.json.return_value = {"id": 1, "name": "张三"}
    mock_get.return_value = mock_response
    
    result = fetch_user_data(1)
    
    assert result["name"] == "张三"
    mock_get.assert_called_once_with("https://api.example.com/users/1")
"""

# TODO: 在这里实现 Mock 测试




# ================================
# 练习 6：测试覆盖率
# ================================
"""
任务：使用 pytest-cov 测试覆盖率：

1. 安装：pip install pytest-cov

2. 运行：pytest --cov=my_module test_my_module.py

3. 生成 HTML 报告：pytest --cov=my_module --cov-report=html

要求：
创建 calculator.py：
def calculator(a: int, b: int, operation: str) -> float:
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b
    else:
        raise ValueError(f"未知操作: {operation}")

创建 test_calculator.py，确保覆盖率 > 90%
"""

# TODO: 在这里创建 calculator.py 和 test_calculator.py




# ================================
# 练习 7：测试驱动开发（TDD）
# ================================
"""
任务：使用 TDD 方式开发：

要求：先写测试，再实现功能

场景：验证密码强度

测试文件（先写）：
def test_password_strength():
    # 弱密码
    assert check_password_strength("123") == "weak"
    assert check_password_strength("abc") == "weak"
    
    # 中等密码
    assert check_password_strength("abc123") == "medium"
    
    # 强密码
    assert check_password_strength("Abc123!@#") == "strong"

然后实现 check_password_strength 函数
"""

# TODO: 使用 TDD 方式实现密码强度检查器




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("Day 11 练习验证 - pytest 测试框架")
    print("=" * 60)
    
    print("\n提示：")
    print("1. 创建测试文件（test_*.py）")
    print("2. 运行：pytest test_*.py")
    print("3. 查看覆盖率：pytest --cov --cov-report=html")
    
    print("\n✅ Day 11 练习完成！")
    print("重点：单元测试、参数化、夹具、Mock、覆盖率、TDD")