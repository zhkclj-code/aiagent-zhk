# 环境配置指南

## Python 环境

### 1. 安装 Python（推荐 3.10+）

**检查现有版本**：
```bash
python3 --version
```

**如需升级**（macOS）：
```bash
brew install python@3.10
```

### 2. 创建虚拟环境

```bash
cd /Users/admin/IdeaProjects/python-pros/aiagent-step1
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 验证安装

```bash
python -c "import langchain; print(langchain.__version__)"
python -c "import openai; print(openai.__version__)"
```

---

## API Key 配置

### 创建环境变量文件

```bash
touch .env
```

### 配置 API Keys

在 `.env` 文件中添加：
```bash
# OpenAI API（必需）
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1

# Anthropic Claude API（可选）
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# 其他配置
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
```

**获取方式**：
- [OpenAI API Key](https://platform.openai.com/api-keys)
- [Anthropic API Key](https://console.anthropic.com/)
- [LangSmith API Key](https://smith.langchain.com/)（可选，用于调试追踪）

---

## VS Code 插件安装

### 核心插件（必装）

在 VS Code 中按 `Cmd + Shift + P`，输入以下命令逐个安装：

```
ext install ms-python.python
ext install ms-python.debugpy
ext install ms-toolsai.jupyter
ext install redhat.vscode-yaml
ext install eamodio.gitlens
```

### 推荐配置

已自动生成 `.vscode/settings.json`，配置包括：
- Python 解释器路径
- Black 代码格式化
- Jupyter Notebook 支持
- 自动导入整理

---

## 验证环境

### 测试 Python 环境

```bash
python --version  # 应显示 3.10+
pip list | grep langchain  # 应显示已安装版本
```

### 测试 API 连接

创建测试文件 `code/01-hello-llm/test_connection.py`：

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, AI Agent learning!"}]
)

print(response.choices[0].message.content)
```

运行测试：
```bash
python code/01-hello-llm/test_connection.py
```

---

## 常见问题

### Q: 虚拟环境激活失败
**解决**：
```bash
chmod +x .venv/bin/activate
source .venv/bin/activate
```

### Q: pip 安装速度慢
**解决**：使用国内镜像
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q: API Key 报错
**解决**：检查 `.env` 文件是否在项目根目录，确保变量名正确

---

## 下一步

环境配置完成后，开始：
1. 阅读 [learning-path.md](learning-path.md)
2. 创建第一个 LLM 调用实验（`code/01-hello-llm/`）
3. 学习笔记记录到 `notes/01-基础准备/`