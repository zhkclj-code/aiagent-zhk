"""
LLM 基础实验 - 简化版
运行单个实验，快速验证
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

def main():
    """运行基础实验"""
    print("🚀 LLM 基础实验")
    print("=" * 60)

    # 创建客户端
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE")
    )

    model = os.getenv("OPENAI_MODEL_NAME", "glm-5.2")

    # 实验 1：不同 Temperature 对比
    print("\n📌 实验 1：Temperature 参数对比")
    prompt = "用一句话介绍 AI Agent。"

    for temp in [0.0, 0.7, 1.0]:
        print(f"\n--- Temperature = {temp} ---")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=100
        )
        print(f"回复: {response.choices[0].message.content}")
        print(f"Tokens: {response.usage.total_tokens}")

    # 实验 2：不同 Max Tokens 对比
    print("\n\n📌 实验 2：Max Tokens 参数对比")
    prompt = "详细解释什么是机器学习。"

    for max_tok in [50, 100, 200]:
        print(f"\n--- Max Tokens = {max_tok} ---")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=max_tok
        )
        print(f"回复: {response.choices[0].message.content}")
        print(f"实际 Tokens: {response.usage.completion_tokens}/{max_tok}")

    print("\n✅ 实验完成！")

if __name__ == "__main__":
    main()