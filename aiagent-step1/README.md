# AI Agent 学习项目 - 第一阶段

> 从 Java 后端到企业级 AI Agent 架构师的学习之路

## 项目简介

本项目用于系统学习企业级 AI Agent 开发，基于长鑫公司的任职要求定制学习路径。

**目标岗位能力**：
- 企业级 AI 平台架构设计（AI网关、MarketPlace、智能体构建平台、知识库平台）
- 生产级 Agent 系统开发（任务规划、工具调用、记忆管理、Multi-Agent 编排）
- 性能优化与稳定性保障
- 记忆库、知识库、向量数据库集成
- 容器化部署与运维

## 学习路径

详见：[learning-path.md](learning-path.md)

**阶段规划**（12-16周）：
- 阶段 1：基础准备（2-3周）
- 阶段 2：单体 Agent 实战（3-4周）
- 阶段 3：进阶能力集成（3-4周）
- 阶段 4：企业级架构设计（3-4周）
- 阶段 5：生产级优化与实战（2-3周）

## 目录结构

```
aiagent-step1/
├── README.md                 # 项目说明
├── learning-path.md         # 详细学习路径
├── notes/                   # 学习笔记
│   ├── 01-基础准备/
│   ├── 02-单体Agent实战/
│   ├── 03-进阶能力集成/
│   ├── 04-企业级架构/
│   └── 05-生产级优化/
├── code/                    # 实验代码
│   ├── 01-hello-llm/        # LLM 基础调用
│   ├── 02-prompt-engineering/ # Prompt 工程
│   ├── 03-simple-agent/     # 单体 Agent
│   ├── 04-tools/            # 工具调用
│   ├── 05-memory/           # 记忆管理
│   ├── 06-knowledge-base/   # 知识库集成
│   └── 07-multi-agent/      # Multi-Agent 编排
├── projects/                # 实战项目
└── resources/               # 学习资源
```

## 当前进度

### ✅ 环境配置完成
- [x] 项目初始化
- [x] 目录结构创建
- [x] 学习路径文档生成（learning-path.md）
- [x] Python 环境配置（Python 3.11.9）
- [x] VS Code 插件安装（Python、Jupyter、YAML、GitLens）
- [x] 依赖安装完成（langchain、langgraph、openai、anthropic 等）
- [x] API 配置完成（使用 newapi 代理服务）
- [x] API 连接测试通过（glm-5.2 模型）

### 📊 环境信息
- **Python 版本**: 3.11.9
- **虚拟环境**: `.venv/`
- **API 服务**: newapi（http://newapi.raycloud.cn/v1）
- **可用模型**: glm-5.2, deepseek-v3.2, qwen3-coder-plus, kimi-k2.5 等

## 下一步行动

1. 开始阶段 1 学习（基础准备）
   - 学习 Python 异步编程和现代语法
   - 理解 LLM 基础概念（Token、Temperature、Context Window）
   - 完成 Prompt 工程实验
2. 实验项目：
   - `code/01-hello-llm/test_newapi.py` - API 连接测试 ✅
   - `code/01-hello-llm/` - LLM 调用实验平台（待创建）
3. 学习笔记：记录到 `notes/01-基础准备/`

## 学习资源

- [LangChain 官方文档](https://python.langchain.com/)
- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
- [OpenAI API 文档](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [Milvus 向量数据库](https://milvus.io/)