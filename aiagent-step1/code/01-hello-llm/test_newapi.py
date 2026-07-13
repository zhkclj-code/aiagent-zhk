"""
测试 newapi API 连接
验证 opencode 配置的 newapi 服务是否可用
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

# 初始化客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

# 测试调用
try:
    print("🔄 测试 newapi 连接...")
    print(f"   API Base: {os.getenv('OPENAI_API_BASE')}")
    print(f"   Model: {os.getenv('OPENAI_MODEL_NAME', 'glm-5.2')}")

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL_NAME", "glm-5.2"),
        messages=[
            {"role": "user", "content": "你好，我是AI Agent学习者，请用一句话介绍自己。"}
        ],
        temperature=0.7,
        max_tokens=100
    )

    print("\n✅ 连接成功！")
    print(f"\n模型回复：{response.choices[0].message.content}")
    print(f"\n📊 Token 使用：")
    print(f"   Prompt tokens: {response.usage.prompt_tokens}")
    print(f"   Completion tokens: {response.usage.completion_tokens}")
    print(f"   Total tokens: {response.usage.total_tokens}")

except Exception as e:
    print(f"\n❌ 连接失败：{str(e)}")
    print("\n可能的原因：")
    print("   1. newapi 服务不可用")
    print("   2. API Key 无效")
    print("   3. 模型名称不正确")
    print("   4. 网络连接问题")