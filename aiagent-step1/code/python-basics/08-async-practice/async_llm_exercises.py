"""
Day 8: 异步编程实战 - LLM API 调用

学习目标：掌握异步调用 LLM API
"""

import asyncio
import time
from typing import List, Dict


# ================================
# 练习 1：异步调用单个 API
# ================================
"""
任务：创建异步调用 OpenAI API 的函数：

功能：
1. async_chat_completion(prompt, model, temperature)：
   - 使用 newapi 服务
   - 异步调用 API
   - 返回响应内容

测试代码：
result = await async_chat_completion("你好，介绍一下Python", "glm-5.2", 0.7)
print(result)
"""

# TODO: 在这里实现 async_chat_completion




# ================================
# 练习 2：并发调用多个 API
# ================================
"""
任务：并发调用多个 LLM API：

功能：
1. batch_chat_completion(prompts, model)：
   - 接收多个 prompt
   - 并发调用 API
   - 返回所有响应

测试代码：
prompts = [
    "介绍一下Python",
    "介绍一下Java",
    "介绍一下Go"
]

start = time.time()
results = await batch_chat_completion(prompts, "glm-5.2")
print(f"并发调用 {len(prompts)} 次，总时间: {time.time() - start:.2f}秒")

for i, result in enumerate(results):
    print(f"\n--- 响应 {i+1} ---")
    print(result[:100] + "...")
"""

# TODO: 在这里实现 batch_chat_completion




# ================================
# 练习 3：异步重试机制
# ================================
"""
任务：实现异步重试逻辑：

功能：
1. async_retry(func, max_retries=3, delay=1)：
   - 调用异步函数
   - 失败时重试
   - 记录重试次数

测试代码：
async def unreliable_api():
    import random
    if random.random() < 0.7:  # 70% 失败率
        raise Exception("API 调用失败")
    return "成功"

result = await async_retry(unreliable_api, max_retries=5)
print(result)
"""

# TODO: 在这里实现 async_retry




# ================================
# 练习 4：异步速率限制
# ================================
"""
任务：实现异步速率限制器：

功能：
1. AsyncRateLimiter 类：
   - __init__(max_requests, period)：最大请求数和时间窗口
   - async acquire()：获取令牌，如果超限则等待

2. 使用速率限制器控制 API 调用频率

测试代码：
limiter = AsyncRateLimiter(max_requests=2, period=1)  # 每秒最多2次

async def limited_api_call(i):
    await limiter.acquire()
    print(f"[{time.time():.2f}] 调用 API {i}")
    await asyncio.sleep(0.1)  # 模拟 API 调用

await asyncio.gather(*[limited_api_call(i) for i in range(10)])
"""

# TODO: 在这里实现 AsyncRateLimiter




# ================================
# 练习 5：异步缓存
# ================================
"""
任务：实现异步缓存装饰器：

功能：
1. async_cache 装饰器：
   - 缓存异步函数的结果
   - 基于 func_name 和 args 生成 key
   - 设置缓存过期时间

测试代码：
@async_cache(expire_seconds=60)
async def expensive_api_call(n):
    print(f"计算 {n}...")
    await asyncio.sleep(1)
    return n * n

# 第一次调用（计算）
result1 = await expensive_api_call(5)
# 第二次调用（缓存）
result2 = await expensive_api_call(5)

print(result1, result2)
"""

# TODO: 在这里实现 async_cache 装饰器




# ================================
# 练习 6：异步批量处理
# ================================
"""
任务：实现异步批量处理：

功能：
1. async_batch_process(items, process_func, batch_size=5)：
   - 将 items 分批处理
   - 每批并发执行
   - 汇总所有结果

测试代码：
async def process_item(item):
    await asyncio.sleep(0.5)  # 模拟处理
    return item * 2

items = range(1, 11)
results = await async_batch_process(items, process_item, batch_size=3)
print(results)
"""

# TODO: 在这里实现 async_batch_process




# ================================
# 练习 7：异步超时和取消
# ================================
"""
任务：实现异步任务超时和取消：

功能：
1. run_with_timeout(coro, timeout)：
   - 运行协程
   - 超时后取消任务
   - 返回结果或 None

2. cancel_all_tasks()：
   - 取消所有正在运行的任务

测试代码：
async def slow_task():
    await asyncio.sleep(10)
    return "完成"

# 正常完成
result1 = await run_with_timeout(slow_task(), timeout=15)
print(result1)

# 超时取消
result2 = await run_with_timeout(slow_task(), timeout=1)
print(result2)  # None
"""

# TODO: 在这里实现 run_with_timeout 和 cancel_all_tasks




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("Day 8 练习验证 - 异步 LLM API 调用")
    print("=" * 60)
    
    # 测试练习 1
    print("\n--- 练习 1：单个 API 调用 ---")
    # result = asyncio.run(async_chat_completion("你好", "glm-5.2", 0.7))
    # print(result)
    
    # 测试练习 2
    print("\n--- 练习 2：并发调用 ---")
    # prompts = ["介绍Python", "介绍Java"]
    # results = asyncio.run(batch_chat_completion(prompts, "glm-5.2"))
    # print(f"获得 {len(results)} 个响应")
    
    # 测试练习 3
    print("\n--- 练习 3：异步重试 ---")
    # async def test_retry():
    #     result = await async_retry(unreliable_api, max_retries=5)
    #     print(result)
    # asyncio.run(test_retry())
    
    print("\n✅ Day 8 练习完成！")
    print("重点：并发调用、重试机制、速率限制、缓存")