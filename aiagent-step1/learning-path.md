# 企业级 AI Agent 开发学习路径

> 从 Java 后端到企业级 AI Agent 架构师

## 学习路径总览

**总时长**：12-16 周（3-4个月）

**学习节奏**：
- 每周投入 20-30 小时（工作日 2-3小时，周末 8-10小时）
- 理论学习：30% | 实践编码：50% | 项目实战：20%

**核心里程碑**：
- 第 3 周：完成 Python 强化，能独立调用 LLM API
- 第 7 周：掌握单体 Agent 开发，实现工具调用和记忆管理
- 第 11 周：完成知识库集成，能设计 Multi-Agent 系统
- 第 15 周：具备企业级架构设计能力，完成生产级项目

---

## 阶段 1：基础准备（2-3周）

### 学习目标

1. **Python 工程化能力**
   - 掌握 Python 异步编程、装饰器、类型注解
   - 熟悉 Python 项目结构、依赖管理、测试框架
   - 理解 Python 与 Java 的差异点（动态类型、GIL、内存管理）

2. **LLM 基础概念**
   - 理解大语言模型原理（Transformer、注意力机制）
   - 掌握 Prompt Engineering 核心技巧
   - 理解 Token、Temperature、Context Window 等概念

3. **开发环境搭建**
   - 配置 Python 开发环境（虚拟环境、依赖管理）
   - 掌握 VS Code + Jupyter Notebook 开发流
   - 配置 LLM API（OpenAI、Anthropic Claude）

### 核心技术栈

| 技术项 | 学习重点 | 对应任职要求 |
|--------|----------|-------------|
| Python 3.10+ | 异步编程、类型系统、Pydantic | 熟练掌握编程语言 |
| OpenAI SDK | API 调用、参数调优、错误处理 | LLM 应用场景理解 |
| Anthropic SDK | Claude API、安全 Prompt 设计 | LLM 基础原理 |
| Jupyter Notebook | 实验记录、可视化调试 | 学习工具 |
| Pydantic | 数据验证、模型定义 | 工程化编码习惯 |

### 实战项目

#### 项目 1：LLM 调用实验工具

**目标**：构建一个 LLM 调用实验平台，用于测试不同 Prompt 和参数效果

**功能**：
- 支持 OpenAI 和 Claude 双模型切换
- 参数可视化调整（Temperature、Max Tokens、Top P）
- Prompt 模板管理（保存、加载、对比）
- Token 消耗统计与成本计算
- 响应时间记录与性能对比

**技术要点**：
- Python 异步编程（asyncio）处理并发请求
- Pydantic 数据模型定义请求参数
- Jupyter Notebook 可视化实验记录
- dotenv 管理敏感配置

**验收标准**：
- [ ] 能同时调用 OpenAI 和 Claude API
- [ ] 参数调整可视化，效果对比清晰
- [ ] Token 消耗统计准确
- [ ] Prompt 模板保存与复用

**代码目录**：`code/01-hello-llm/llm-experiment-platform/`

#### 项目 2：Prompt 工程实战

**目标**：掌握 Prompt Engineering 核心技巧，建立 Prompt 模板库

**实验内容**：
- Zero-shot、Few-shot、Chain-of-Thought Prompt 对比
- 角色设定、任务拆解、输出格式控制
- Prompt 注入攻击防护实验
- 长文本处理技巧（分段、摘要、检索）

**交付物**：
- Prompt 模板库（至少 10 个高质量模板）
- Prompt 效果对比报告（Markdown 文档）
- Prompt 注入防护方案

**验收标准**：
- [ ] 能根据任务设计合适的 Prompt 策略
- [ ] Prompt 模板库结构化、可复用
- [ ] 理解 Prompt 注入风险，有防护意识

**代码目录**：`code/02-prompt-engineering/`

### 学习资源

**官方文档**：
- [Python 官方文档 - 异步编程](https://docs.python.org/3/library/asyncio.html)
- [Pydantic 文档](https://docs.pydantic.dev/)
- [OpenAI API 文档](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com/)

**推荐阅读**：
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

**视频课程**：
- [DeepLearning.AI - ChatGPT Prompt Engineering](https://www.deeplearning.ai/)

### 阶段验收标准

**能力自查表**：
- [ ] Python 异步编程：能编写并发 LLM 调用代码
- [ ] 类型注解：熟练使用 Pydantic 定义数据模型
- [ ] LLM API 调用：独立完成 OpenAI/Claude API 集成
- [ ] Prompt 设计：掌握至少 5 种 Prompt 策略
- [ ] Token 管理：理解 Context Window 限制，能优化 Token 消耗
- [ ] 成本意识：能估算 API 调用成本，有优化意识

---

## 阶段 2：单体 Agent 实战（3-4周）

### 学习目标

1. **Agent 核心模式**
   - 理解 ReAct（Reasoning + Acting）模式原理与实现
   - 掌握 Planning & Executor 模式设计
   - 实现 Agent 执行循环（思考-行动-观察-反思）

2. **工具调用系统**
   - 理解 Function Calling API 原理
   - 设计工具定义格式（参数、返回值、描述）
   - 实现工具注册与动态调用机制
   - 工具错误处理与重试策略

3. **记忆管理机制**
   - 理解对话记忆类型（短期、长期、工作记忆）
   - 实现记忆存储与检索（内存、文件、数据库）
   - 记忆摘要与压缩策略
   - 记忆管理对 Token 消耗的影响

### 核心技术栈

| 技术项 | 学习重点 | 对应任职要求 |
|--------|----------|-------------|
| LangChain | Agent 构建、工具集成、记忆管理 | Agent 核心模式理解 |
| LangGraph | Agent 状态图、流程编排 | Planning & Executor |
| Function Calling | 工具定义、参数验证、动态调用 | 工具调用系统设计 |
| Memory 系统 | 对话历史管理、记忆检索 | 记忆管理机制 |

### 实战项目

#### 项目 1：智能助手 Agent

**目标**：实现一个具备工具调用和记忆管理的单体 Agent

**功能**：
- 集成 5+ 实用工具（天气查询、搜索、计算、文件读写、代码执行）
- 记忆管理（短期对话记忆 + 长期记忆存储）
- ReAct 执行循环（思考-行动-观察）
- 错误处理与重试机制
- 执行日志记录与可视化

**技术要点**：
- LangChain Agent 架构（AgentExecutor、Tool、Memory）
- Function Calling 工具定义（JSON Schema）
- 记忆存储（ConversationBufferMemory、VectorStoreMemory）
- 异步工具调用处理

**验收标准**：
- [ ] Agent 能自主选择工具完成任务
- [ ] 记忆管理有效，多轮对话连贯
- [ ] ReAct 循环可视化，执行过程清晰
- [ ] 工具错误自动重试，成功率 >80%

**代码目录**：`code/03-simple-agent/smart-assistant/`

#### 项目 2：Planning Agent

**目标**：实现 Planning & Executor 模式的任务规划 Agent

**功能**：
- 任务分解：将复杂任务拆解为子任务序列
- 计划生成：生成可执行的任务计划（Plan）
- 任务执行：按计划逐步执行，动态调整
- 进度追踪：任务执行进度可视化
- 异常恢复：执行失败时的计划调整

**技术要点**：
- LangGraph 状态图设计（Planning → Execution → Reflection）
- 任务 DAG（有向无环图）构建
- 计划调整算法（失败重试、任务重排）
- 进度状态管理

**验收标准**：
- [ ] 能将复杂任务自动拆解为子任务
- [ ] 计划生成合理，执行顺序正确
- [ ] 执行失败能自动调整计划
- [ ] 进度可视化，状态清晰

**代码目录**：`code/03-simple-agent/planning-agent/`

### 学习资源

**官方文档**：
- [LangChain Agent 文档](https://python.langchain.com/docs/modules/agents/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)

**核心论文**：
- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) ⭐ 必读
- [Toolformer](https://arxiv.org/abs/2302.04761)

**开源项目参考**：
- [LangChain Templates](https://github.com/langchain-ai/langchain/tree/master/templates)
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)

### 阶段验收标准

**能力自查表**：
- [ ] ReAct 模式：理解原理，能独立实现 ReAct Agent
- [ ] Planning & Executor：能设计任务规划系统
- [ ] 工具调用：熟练使用 Function Calling，能定义复杂工具
- [ ] 记忆管理：实现多种记忆类型，理解 Token 消耗影响
- [ ] Agent 架构：理解 LangChain Agent 组件关系
- [ ] 错误处理：设计 Agent 容错机制，重试策略合理

---

## 阶段 3：进阶能力集成（3-4周）

### 学习目标

1. **知识库与向量数据库**
   - 理解向量检索原理（Embedding、相似度计算）
   - 掌握 Milvus/PGVector 向量数据库使用
   - 实现知识库构建流程（文档处理、向量存储、检索）
   - RAG（检索增强生成）架构设计

2. **Skills 与工具生态**
   - 设计 Skills 定义格式（技能描述、参数、执行逻辑）
   - Skills 注册与动态加载机制
   - Skills 组合与编排策略
   - 与 Agent 框架集成（LangChain、LangGraph）

3. **Agent 性能优化**
   - Token 消耗优化（Prompt 精简、记忆压缩、文档分段）
   - 响应延迟优化（流式输出、异步调用、缓存）
   - 并发能力提升（异步 Agent、批量处理）
   - 成本控制策略（模型选择、请求合并）

### 核心技术栈

| 技术项 | 学习重点 | 对应任职要求 |
|--------|----------|-------------|
| Milvus | 向量数据库部署、索引优化、检索 | 向量数据库使用经验 |
| PGVector | PostgreSQL 向量扩展、SQL 检索 | 向量数据库使用经验 |
| RAG | 文档处理、向量存储、检索增强 | 知识库相关技术 |
| Embedding | 文本向量化、相似度计算 | 知识库集成 |
| LangSmith | Agent 追踪、性能分析、调试 | 性能优化能力 |

### 实战项目

#### 项目 1：企业知识库问答系统

**目标**：构建一个基于向量数据库的知识库问答 Agent

**功能**：
- 文档处理：PDF、Word、Markdown 自动解析与分段
- 向量存储：Milvus 部署、向量索引构建
- 智能检索：相似度检索、多路召回、重排序
- RAG 问答：检索增强生成，上下文注入
- 知识库管理：文档增删改、版本管理

**技术要点**：
- Milvus 安装与配置（Docker 部署）
- Embedding 模型选择（OpenAI、HuggingFace）
- 文档分段策略（固定长度、语义分段）
- RAG Prompt 设计（上下文注入、答案生成）

**验收标准**：
- [ ] 支持多种文档格式解析
- [ ] 向量检索准确率 >85%
- [ ] RAG 问答连贯，答案准确
- [ ] 知识库管理功能完整

**代码目录**：`code/06-knowledge-base/enterprise-kb-agent/`

#### 项目 2：Skills 集成平台

**目标**：构建一个 Skills 注册与管理平台，集成到 Agent 系统

**功能**：
- Skills 定义格式（YAML/JSON Schema）
- Skills 注册与动态加载
- Skills 搜索与匹配（基于任务描述）
- Skills 组合编排（Skills Chain）
- Skills 执行日志与监控

**技术要点**：
- Skills 元数据设计（技能描述、参数、依赖）
- Skills 注册中心（内存、数据库）
- Skills 动态调用（反射、动态加载）
- Skills 与 LangChain Tool 集成

**验收标准**：
- [ ] Skills 定义格式规范，易于扩展
- [ ] Skills 注册与加载机制完整
- [ ] Skills 搜索匹配准确
- [ ] Skills 执行日志清晰，可追踪

**代码目录**：`code/04-tools/skills-platform/`

#### 项目 3：Agent 性能优化实战

**目标**：对已有 Agent 进行性能优化，降低延迟和成本

**优化方向**：
- Token 消耗：Prompt 精简、记忆压缩、文档分段
- 响应延迟：流式输出、异步调用、结果缓存
- 并发能力：异步 Agent、批量请求、任务队列
- 成本控制：模型选择（GPT-3.5 vs GPT-4）、请求合并

**技术要点**：
- LangSmith 追踪分析（Token 消耗、响应时间）
- 流式输出实现（OpenAI Stream API）
- 异步 Agent 架构（asyncio、并发控制）
- 缓存策略（LRU Cache、Redis）

**验收标准**：
- [ ] Token 消耗降低 >30%
- [ ] 响应延迟降低 >20%
- [ ] 并发处理能力提升 >50%
- [ ] 成本优化策略清晰，效果可量化

**代码目录**：`code/03-simple-agent/agent-optimization/`

### 学习资源

**官方文档**：
- [Milvus 官方文档](https://milvus.io/docs)
- [PGVector GitHub](https://github.com/pgvector/pgvector)
- [LangSmith 文档](https://docs.smith.langchain.com/)

**核心论文**：
- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) ⭐ RAG 原理
- [Dense Passage Retrieval](https://arxiv.org/abs/2005.11401)

**开源项目参考**：
- [Dify](https://github.com/langgenius/dify) - 企业级 AI 平台
- [FastGPT](https://github.com/labring/FastGPT) - 知识库问答

### 阶段验收标准

**能力自查表**：
- [ ] 向量数据库：熟练使用 Milvus/PGVector，理解索引优化
- [ ] 知识库构建：完整实现文档处理→向量存储→检索流程
- [ ] RAG 架构：理解 RAG 原理，能设计检索增强生成系统
- [ ] Skills 集成：设计 Skills 系统，与 Agent 框架集成
- [ ] 性能优化：Token、延迟、并发优化策略清晰，效果可量化
- [ ] 成本意识：能估算成本，有优化意识，策略可落地

---

## 阶段 4：企业级架构设计（3-4周）

### 学习目标

1. **Multi-Agent 编排系统**
   - 理解 Multi-Agent 协作模式（分工、协调、竞争）
   - 设计 Agent 编排架构（中心式、分布式、混合式）
   - 实现 Agent 通信机制（消息传递、共享状态）
   - Agent 决策与调度策略

2. **AI 平台架构设计**
   - AI Gateway 设计（请求路由、负载均衡、安全认证）
   - Agent MarketPlace 设计（Agent 注册、搜索、调用）
   - 智能体构建平台设计（可视化编排、模板管理）
   - 知识库平台设计（多租户、权限管理、版本控制）

3. **容器化部署与运维**
   - Docker 容器化（Agent 服务打包、镜像管理）
   - Kubernetes 部署（Pod、Service、Ingress、ConfigMap）
   - 监控与日志（Prometheus、Grafana、ELK）
   - CI/CD 流程设计（自动化部署、版本管理）

### 核心技术栈

| 技术项 | 学习重点 | 对应任职要求 |
|--------|----------|-------------|
| LangGraph Multi-Agent | Agent 协作、状态图、消息传递 | Multi-Agent 编排 |
| Docker | 容器化、镜像构建、部署 | 容器化部署能力 |
| Kubernetes | Pod 管理、Service、Ingress | 容器化运维能力 |
| Prometheus/Grafana | 监控指标、可视化 | 生产级运维 |
| FastAPI | Agent API 服务化 | 服务标准化 |

### 实战项目

#### 项目 1：Multi-Agent 协作系统

**目标**：实现一个 Multi-Agent 协作系统，完成复杂任务

**场景**：数据分析助手（数据收集 Agent + 分析 Agent + 可视化 Agent + 报告 Agent）

**功能**：
- Agent 分工：根据任务类型自动分配 Agent
- Agent 通信：消息传递、共享状态、任务协调
- Agent 调度：优先级调度、负载均衡
- 执行监控：Agent 执行状态可视化
- 异常恢复：Agent 失败时的任务重分配

**技术要点**：
- LangGraph Multi-Agent 架构（StateGraph、Node、Edge）
- Agent 通信机制（消息队列、共享内存）
- 调度算法（优先级队列、负载均衡）
- 状态管理（全局状态、Agent 状态）

**验收标准**：
- [ ] 多 Agent 协作流畅，任务分配合理
- [ ] Agent 通信机制完整，消息传递清晰
- [ ] 调度策略合理，负载均衡有效
- [ ] 执行状态可视化，异常恢复机制完整

**代码目录**：`code/07-multi-agent/data-analysis-team/`

#### 项目 2：AI Gateway 服务

**目标**：设计并实现一个 AI Gateway，统一管理 Agent 服务

**功能**：
- 请求路由：根据任务类型路由到不同 Agent
- 负载均衡：Agent 服务负载均衡（轮询、权重）
- 安全认证：API Key 管理、请求签名验证
- 速率限制：防止滥用，限流策略
- 日志追踪：请求日志、执行追踪

**技术要点**：
- FastAPI 框架（异步 API、请求处理）
- 负载均衡算法（轮询、权重、最少连接）
- API Key 管理（生成、验证、权限）
- Redis 速率限制（令牌桶、滑动窗口）

**验收标准**：
- [ ] 请求路由准确，负载均衡有效
- [ ] 安全认证机制完整，防滥用
- [ ] 速率限制生效，请求可控
- [ ] 日志追踪清晰，可调试

**代码目录**：`code/07-multi-agent/ai-gateway/`

#### 项目 3：容器化部署实战

**目标**：将 Agent 服务容器化，部署到 Kubernetes

**部署架构**：
- Agent 服务容器化（Docker 镜像）
- Kubernetes 部署（Deployment、Service、Ingress）
- 配置管理（ConfigMap、Secret）
- 监控集成（Prometheus、Grafana）

**技术要点**：
- Docker 镜像构建（多阶段构建、优化）
- Kubernetes YAML 配置（Deployment、Service、Ingress）
- ConfigMap 管理环境变量
- Prometheus 监控指标暴露

**验收标准**：
- [ ] Agent 服务容器化成功，镜像可复用
- [ ] Kubernetes 部署完整，服务可访问
- [ ] 配置管理清晰，环境变量可控
- [ ] 监控指标可视化，状态可追踪

**代码目录**：`code/07-multi-agent/container-deployment/`

### 学习资源

**官方文档**：
- [LangGraph Multi-Agent](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/)
- [Docker 官方文档](https://docs.docker.com/)
- [Kubernetes 官方文档](https://kubernetes.io/docs/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)

**开源项目参考**：
- [LangFlow](https://github.com/logspace-ai/langflow) - Agent 可视化编排
- [Dify](https://github.com/langgenius/dify) - 企业级 AI 平台架构参考

### 阶段验收标准

**能力自查表**：
- [ ] Multi-Agent 编排：设计并实现多 Agent 协作系统
- [ ] Agent 通信：理解消息传递、共享状态机制
- [ ] AI Gateway：设计请求路由、负载均衡、安全认证
- [ ] 容器化部署：熟练 Docker 镜像构建、Kubernetes 部署
- [ ] 监控运维：配置 Prometheus/Grafana 监控
- [ ] API 服务化：使用 FastAPI 构建 Agent API 服务

---

## 阶段 5：生产级优化与实战（2-3周）

### 学习目标

1. **生产级稳定性保障**
   - 错误容灾机制设计（重试、降级、熔断）
   - 数据备份与恢复策略
   - 服务监控与告警（异常检测、自动恢复）
   - 安全防护（Prompt 注入、数据泄露、权限控制）

2. **AI 编程工具理解**
   - 理解 Claude Code、Open Code 等工具原理
   - Agent 工具化设计（可复用、可配置）
   - 二次开发能力（插件、扩展）
   - 与现有工作流集成

3. **综合项目实战**
   - 完整项目从 0 到 1 实现
   - 项目文档与交付物整理
   - 能力验证与复盘

### 核心技术栈

| 技术项 | 学习重点 | 对应任职要求 |
|--------|----------|-------------|
| 错误容灾 | 重试、降级、熔断机制 | 错误容灾机制设计 |
| 监控告警 | Prometheus、AlertManager | 稳定性保障 |
| 安全防护 | Prompt 注入防护、权限控制 | 安全意识 |
| Claude Code/Open Code | AI 编程工具原理、二次开发 | AI 编程工具经验 |

### 实战项目

#### 项目 1：生产级 Agent 系统优化

**目标**：对已有 Agent 系统进行生产级优化，保障稳定性

**优化方向**：
- 错误容灾：重试策略、降级方案、熔断机制
- 监控告警：异常检测、自动告警、恢复策略
- 安全防护：Prompt 注入检测、数据脱敏、权限控制
- 日志追踪：执行日志、错误日志、审计日志

**技术要点**：
- 重试策略（指数退避、最大重试次数）
- 熔断器模式（Circuit Breaker）
- Prompt 注入检测（规则匹配、模型检测）
- 数据脱敏（正则匹配、隐私字段识别）

**验收标准**：
- [ ] 错误容灾机制完整，成功率 >95%
- [ ] 监控告警生效，异常自动恢复
- [ ] 安全防护有效，注入攻击可检测
- [ ] 日志追踪清晰，可审计

**代码目录**：`code/07-multi-agent/production-optimization/`

#### 项目 2：AI 编程工具二次开发

**目标**：基于 Claude Code/Open Code 进行二次开发，定制 Agent 工具

**开发方向**：
- 插件开发（自定义 Skills、工具扩展）
- 配置定制（Agent 模板、Prompt 模板）
- 工作流集成（与现有工具链集成）
- 性能优化（缓存、异步、批量）

**技术要点**：
- Claude Code/Open Code 架构理解
- 插件开发规范（接口、配置、注册）
- Skills 定义与集成
- 工作流编排（CI/CD、自动化）

**验收标准**：
- [ ] 理解 AI 编程工具架构原理
- [ ] 完成至少 1 个插件或扩展开发
- [ ] 与现有工作流集成成功
- [ ] 性能优化效果可量化

**代码目录**：`code/07-multi-agent/ai-tool-extension/`

#### 项目 3：综合实战项目（自由选题）

**目标**：从 0 到 1 实现一个完整的企业级 Agent 应用

**选题建议**：
- 企业知识库问答系统（完整版）
- Multi-Agent 数据分析平台
- AI Gateway + Agent MarketPlace
- Agent 编排平台（可视化）

**交付物**：
- 完整代码（GitHub 仓库）
- 项目文档（架构设计、部署指南）
- 技术复盘（学习笔记、能力验证）
- Demo 视频（功能演示）

**验收标准**：
- [ ] 项目功能完整，符合任职要求能力点
- [ ] 文档清晰，架构设计合理
- [ ] 部署成功，服务稳定运行
- [ ] 技术复盘深刻，能力提升明显

**代码目录**：`projects/final-project/`

### 学习资源

**AI 编程工具**：
- [Claude Code](https://claude.ai/code)
- [Cursor](https://cursor.sh/)
- [Continue](https://continue.dev/)

**生产级参考**：
- [Dify 生产部署文档](https://docs.dify.ai/getting-started/install-self-hosted)
- [LangServe 生产指南](https://python.langchain.com/docs/langserve)

### 阶段验收标准

**能力自查表**：
- [ ] 错误容灾：设计重试、降级、熔断机制，成功率 >95%
- [ ] 监控运维：配置 Prometheus/Grafana，异常自动告警
- [ ] 安全防护：Prompt 注入检测，数据脱敏，权限控制
- [ ] AI 工具理解：理解 Claude Code/Open Code 原理，有二次开发经验
- [ ] 综合实战：完成完整项目，文档清晰，能力验证达标

---

## 学习资源清单

详见：[resources/learning-resources.md](resources/learning-resources.md)

---

## 验收标准对照表

| 任职要求 | 对应学习阶段 | 验收标准 |
|---------|-------------|---------|
| AI 平台架构设计（AI网关、MarketPlace、智能体构建平台、知识库平台） | 阶段 4 | 完成 AI Gateway + MarketPlace 设计，智能体构建平台原型 |
| 生产级 Agent 系统（任务规划、工具调用、记忆管理、Multi-Agent 编排） | 阶段 2-4 | 完成 ReAct Agent、Planning Agent、Multi-Agent 协作系统 |
| 性能优化（响应延迟、并发能力） | 阶段 3-5 | Token 消耗降低 >30%，响应延迟降低 >20%，并发提升 >50% |
| 错误容灾机制 | 阶段 5 | 重试、降级、熔断机制完整，成功率 >95% |
| 记忆库、知识库、Skills | 阶段 3 | 完成知识库问答系统、Skills 平台 |
| 向量数据库（Milvus/PGVector） | 阶段 3 | 熟练使用 Milvus，完成 RAG 问答系统 |
| ReAct、Planning & Executor | 阶段 2 | 理解原理，独立实现 ReAct Agent 和 Planning Agent |
| Docker、Kubernetes | 阶段 4 | 完成容器化部署，Kubernetes 部署成功 |
| Claude Code、Open Code | 阶段 5 | 理解原理，有二次开发经验 |
| Python 工程化编码 | 阶段 1 | 熟练 Python 异步编程、类型注解、项目结构 |

---

## 学习方法建议

### 每周学习节奏

**工作日（每天 2-3 小时）**：
- 1 小时：理论学习（文档、论文）
- 1-2 小时：代码实践（实验、调试）

**周末（每天 8-10 小时）**：
- 3 小时：理论学习（深度阅读）
- 5 小时：项目实战（完整项目）
- 2 小时：笔记整理、复盘

### 学习笔记规范

每个阶段创建独立笔记目录（`notes/01-基础准备/`），包含：
- **概念笔记**：核心概念理解、原理分析
- **实验记录**：Jupyter Notebook 实验、结果分析
- **项目复盘**：项目设计、技术要点、问题解决
- **资源收集**：优质资源、开源项目、论文

### 实践优先原则

- 理论学习后**立即实践**（不超过 24 小时）
- 每个概念至少完成 **1 个实验**
- 每个阶段至少完成 **2 个项目**
- 代码提交到 GitHub，建立作品集

### 问题解决策略

遇到问题时：
1. **查阅官方文档**（首选）
2. **搜索 GitHub Issues**（找类似问题）
3. **使用 AI 编程工具**（Claude Code、Cursor）
4. **询问社区**（LangChain Discord、Stack Overflow）

---

## 下一步行动

1. **立即开始**：安装 VS Code 插件，配置 Python 环境
2. **第一周任务**：完成阶段 1 的 Python 强化 + LLM 调用实验
3. **建立习惯**：每天固定学习时间，每周复盘进度

**祝你学习顺利，早日达到企业级 AI Agent 开发能力！**