"""
LLM 调用实验平台
用于测试不同参数对生成结果的影响
"""
import os
import asyncio
from datetime import datetime
from typing import Any
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field

# 加载环境变量
load_dotenv()


class ExperimentResult(BaseModel):
    """实验结果数据模型"""
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    model: str
    prompt: str
    temperature: float
    max_tokens: int
    response: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    latency_seconds: float


class LLMExperiment:
    """LLM 实验平台"""

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )
        self.model = os.getenv("OPENAI_MODEL_NAME", "glm-5.2")
        self.results: list[ExperimentResult] = []

    def run_single_experiment(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> ExperimentResult:
        """运行单次实验"""
        start_time = datetime.now()

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )

        end_time = datetime.now()
        latency = (end_time - start_time).total_seconds()

        result = ExperimentResult(
            model=self.model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            response=response.choices[0].message.content,
            prompt_tokens=response.usage.prompt_tokens,
            completion_tokens=response.usage.completion_tokens,
            total_tokens=response.usage.total_tokens,
            latency_seconds=latency
        )

        self.results.append(result)
        return result

    def print_result(self, result: ExperimentResult):
        """打印实验结果"""
        print("\n" + "=" * 60)
        print(f"📊 实验结果")
        print("=" * 60)
        print(f"模型: {result.model}")
        print(f"Temperature: {result.temperature}")
        print(f"Max Tokens: {result.max_tokens}")
        print(f"\n📝 Prompt:\n{result.prompt}")
        print(f"\n💬 回复:\n{result.response}")
        print(f"\n📈 Token 统计:")
        print(f"  Prompt tokens: {result.prompt_tokens}")
        print(f"  Completion tokens: {result.completion_tokens}")
        print(f"  Total tokens: {result.total_tokens}")
        print(f"\n⏱️  响应时间: {result.latency_seconds:.2f} 秒")
        print("=" * 60)

    def run_temperature_experiment(self, prompt: str):
        """Temperature 参数对比实验"""
        print("\n🔬 Temperature 参数对比实验")
        print("测试不同 Temperature 值对生成结果的影响")

        temperatures = [0.0, 0.3, 0.7, 1.0]

        for temp in temperatures:
            print(f"\n--- Temperature = {temp} ---")
            result = self.run_single_experiment(prompt, temperature=temp)
            self.print_result(result)

    def run_max_tokens_experiment(self, prompt: str):
        """Max Tokens 参数对比实验"""
        print("\n🔬 Max Tokens 参数对比实验")
        print("测试不同 Max Tokens 值对生成结果的影响")

        max_tokens_list = [50, 100, 200, 500]

        for max_tok in max_tokens_list:
            print(f"\n--- Max Tokens = {max_tok} ---")
            result = self.run_single_experiment(prompt, max_tokens=max_tok)
            self.print_result(result)


def main():
    """主函数：运行实验"""
    print("🚀 LLM 调用实验平台启动")
    print("=" * 60)

    # 创建实验平台
    experiment = LLMExperiment()

    # 实验 1：基础调用测试
    print("\n📌 实验 1：基础调用测试")
    prompt = "请用一句话介绍什么是 AI Agent。"
    result = experiment.run_single_experiment(prompt)
    experiment.print_result(result)

    # 实验 2：Temperature 参数对比
    print("\n📌 实验 2：Temperature 参数对比")
    prompt = "写一个关于人工智能的短故事（50字以内）。"
    experiment.run_temperature_experiment(prompt)

    # 实验 3：Max Tokens 参数对比
    print("\n📌 实验 3：Max Tokens 参数对比")
    prompt = "请详细解释什么是机器学习，包括定义、类型和应用场景。"
    experiment.run_max_tokens_experiment(prompt)

    # 统计所有实验
    print("\n📊 实验统计")
    print("=" * 60)
    print(f"总实验次数: {len(experiment.results)}")
    total_tokens = sum(r.total_tokens for r in experiment.results)
    total_latency = sum(r.latency_seconds for r in experiment.results)
    print(f"总 Token 消耗: {total_tokens}")
    print(f"总耗时: {total_latency:.2f} 秒")
    print("=" * 60)


if __name__ == "__main__":
    main()