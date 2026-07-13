"""
Day 7-8: 异步编程（重点）

学习目标：理解异步编程概念和 asyncio 基础
"""

import asyncio
import time


# ================================
# 1. 同步 vs 异步（对比）
# ================================

# 同步版本
def sync_task(name: str, seconds: int) -> str:
    """同步任务"""
    print(f"开始任务 {name}")
    time.sleep(seconds)  # 阻塞
    print(f"完成任务 {name}")
    return f"{name} 结果"

def sync_main():
    """同步主函数"""
    start = time.time()
    sync_task("A", 2)
    sync_task("B", 2)
    print(f"同步总时间: {time.time() - start:.2f}秒")


# 异步版本
async def async_task(name: str, seconds: int) -> str:
    """异步任务"""
    print(f"开始任务 {name}")
    await asyncio.sleep(seconds)  # 非阻塞
    print(f"完成任务 {name}")
    return f"{name} 结果"

async def async_main():
    """异步主函数"""
    start = time.time()
    results = await asyncio.gather(
        async_task("A", 2),
        async_task("B", 2)
    )
    print(f"异步总时间: {time.time() - start:.2f}秒")
    print(f"结果: {results}")


print("=== 同步执行 ===")
sync_main()

print("\n=== 异步执行 ===")
asyncio.run(async_main())


# ================================
# 2. async/await 基础
# ================================

async def fetch_data(url: str) -> str:
    """模拟异步获取数据"""
    print(f"正在获取: {url}")
    await asyncio.sleep(1)  # 模拟网络延迟
    return f"数据来自 {url}"

async def process_data():
    """处理数据"""
    # 串行执行（慢）
    print("\n--- 串行执行 ---")
    start = time.time()
    data1 = await fetch_data("api/user")
    data2 = await fetch_data("api/orders")
    print(f"串行总时间: {time.time() - start:.2f}秒")

    # 并行执行（快）
    print("\n--- 并行执行 ---")
    start = time.time()
    results = await asyncio.gather(
        fetch_data("api/user"),
        fetch_data("api/orders")
    )
    print(f"并行总时间: {time.time() - start:.2f}秒")
    print(f"结果: {results}")

asyncio.run(process_data())


# ================================
# 3. 并发控制
# ================================

async def download_file(file_id: int) -> str:
    """模拟下载文件"""
    print(f"开始下载文件 {file_id}")
    await asyncio.sleep(1)
    print(f"完成下载文件 {file_id}")
    return f"文件{file_id}"

async def download_with_semaphore():
    """使用信号量控制并发"""
    semaphore = asyncio.Semaphore(2)  # 最多同时下载2个

    async def limited_download(file_id: int):
        async with semaphore:
            return await download_file(file_id)

    tasks = [limited_download(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(f"下载结果: {results}")

print("\n=== 并发控制 ===")
asyncio.run(download_with_semaphore())


# ================================
# 4. 超时和异常处理
# ================================

async def slow_task():
    """慢任务"""
    await asyncio.sleep(5)
    return "完成"

async def timeout_example():
    """超时示例"""
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2.0)
        print(f"结果: {result}")
    except asyncio.TimeoutError:
        print("任务超时！")

async def error_handling():
    """异常处理"""
    async def task_with_error():
        await asyncio.sleep(1)
        raise ValueError("出错了")

    try:
        await task_with_error()
    except ValueError as e:
        print(f"捕获异常: {e}")

print("\n=== 超时处理 ===")
asyncio.run(timeout_example())

print("\n=== 异常处理 ===")
asyncio.run(error_handling())


# ================================
# 5. 异步上下文管理器
# ================================

class AsyncTimer:
    """异步计时器"""

    async def __aenter__(self):
        self.start = time.time()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"异步执行时间: {self.end - self.start:.2f}秒")

async def async_context_example():
    """异步上下文示例"""
    async with AsyncTimer():
        await asyncio.sleep(1)
        print("异步任务执行中...")

print("\n=== 异步上下文管理器 ===")
asyncio.run(async_context_example())


# ================================
# 6. 实战：并发调用 LLM API
# ================================

import os
from dotenv import load_dotenv

load_dotenv()

async def call_llm_async(prompt: str, model: str = "glm-5.2"):
    """异步调用 LLM API"""
    from openai import AsyncOpenAI

    client = AsyncOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE")
    )

    print(f"发送请求: {prompt[:20]}...")
    start = time.time()

    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=50
    )

    latency = time.time() - start
    return {
        "prompt": prompt,
        "response": response.choices[0].message.content,
        "tokens": response.usage.total_tokens,
        "latency": latency
    }

async def batch_llm_calls():
    """批量并发调用 LLM"""
    prompts = [
        "什么是人工智能？",
        "什么是机器学习？",
        "什么是深度学习？"
    ]

    print("\n=== 批量并发调用 ===")
    start = time.time()

    # 并发调用
    results = await asyncio.gather(
        *[call_llm_async(prompt) for prompt in prompts]
    )

    total_time = time.time() - start
    print(f"\n总时间: {total_time:.2f}秒")
    print(f"平均延迟: {sum(r['latency'] for r in results) / len(results):.2f}秒")

    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['prompt']}")
        print(f"   回答: {result['response']}")
        print(f"   Tokens: {result['tokens']}, 延迟: {result['latency']:.2f}s")


# 运行批量调用（取消注释以运行）
# asyncio.run(batch_llm_calls())


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)

# 练习 1：并发下载多个文件
async def practice_concurrent_download():
    """并发下载"""
    async def download(url: str):
        print(f"下载: {url}")
        await asyncio.sleep(1)
        return f"{url} 的内容"

    urls = ["file1.txt", "file2.txt", "file3.txt"]
    results = await asyncio.gather(*[download(url) for url in urls])
    print(f"练习 1 - 下载结果: {results}")

asyncio.run(practice_concurrent_download())


# 练习 2：使用信号量限制并发
async def practice_semaphore():
    """信号量控制"""
    semaphore = asyncio.Semaphore(2)

    async def limited_task(task_id: int):
        async with semaphore:
            print(f"执行任务 {task_id}")
            await asyncio.sleep(1)
            return f"任务{task_id}完成"

    results = await asyncio.gather(*[limited_task(i) for i in range(5)])
    print(f"练习 2 - 信号量结果: {results}")

asyncio.run(practice_semaphore())


# 练习 3：异步计时器
async def practice_async_timer():
    """异步计时"""
    async with AsyncTimer():
        await asyncio.sleep(1)
        print("练习 3 - 异步任务执行")

asyncio.run(practice_async_timer())


print("\n✅ Day 7-8 学习完成！")
print("要点总结：")
print("1. async def 定义异步函数，await 等待异步操作")
print("2. asyncio.gather() 并发执行多个任务")
print("3. asyncio.Semaphore 控制并发数量")
print("4. asyncio.wait_for() 设置超时")
print("5. 异步编程适合 I/O 密集型任务（网络请求、文件读写）")
print("6. Agent 开发中用于并发调用 LLM API")