"""
Day 9: 异步编程实战

学习目标：应用异步编程解决实际问题
"""

import asyncio
import time
from typing import List, Dict, Any
import random


# ================================
# 1. 异步 LLM API 调用（模拟）
# ================================

async def call_llm_api(prompt: str, model: str = "gpt-3.5") -> Dict[str, Any]:
    """模拟异步 LLM API 调用"""
    latency = random.uniform(0.5, 2.0)
    await asyncio.sleep(latency)
    
    return {
        "prompt": prompt,
        "model": model,
        "response": f"处理后的响应: {prompt[:20]}...",
        "latency": latency,
        "tokens": len(prompt) + random.randint(50, 200)
    }


async def sequential_llm_calls():
    """顺序调用 LLM API"""
    print("顺序调用 LLM API:")
    start = time.time()
    
    prompts = [
        "什么是机器学习？",
        "什么是深度学习？",
        "什么是自然语言处理？"
    ]
    
    results = []
    for prompt in prompts:
        result = await call_llm_api(prompt)
        results.append(result)
        print(f"  完成调用: {result['prompt'][:15]}...")
    
    elapsed = time.time() - start
    print(f"总耗时: {elapsed:.2f} 秒\n")
    return results


async def concurrent_llm_calls():
    """并发调用 LLM API"""
    print("并发调用 LLM API:")
    start = time.time()
    
    prompts = [
        "什么是机器学习？",
        "什么是深度学习？",
        "什么是自然语言处理？"
    ]
    
    results = await asyncio.gather(
        *[call_llm_api(prompt) for prompt in prompts]
    )
    
    for result in results:
        print(f"  完成调用: {result['prompt'][:15]}...")
    
    elapsed = time.time() - start
    print(f"总耗时: {elapsed:.2f} 秒\n")
    return results


async def compare_llm_performance():
    """对比顺序 vs 并发调用性能"""
    print("=" * 60)
    print("LLM API 调用性能对比")
    print("=" * 60)
    
    await sequential_llm_calls()
    await concurrent_llm_calls()


asyncio.run(compare_llm_performance())


# ================================
# 2. 异步数据处理管道
# ================================

async def fetch_data_batch(batch_id: int) -> List[int]:
    """模拟数据获取"""
    await asyncio.sleep(0.5)
    data = [random.randint(1, 100) for _ in range(10)]
    print(f"批次 {batch_id} 数据获取完成: {data[:5]}...")
    return data


async def process_data_batch(data: List[int]) -> Dict[str, float]:
    """模拟数据处理"""
    await asyncio.sleep(0.3)
    result = {
        "mean": sum(data) / len(data),
        "max": max(data),
        "min": min(data),
        "count": len(data)
    }
    print(f"数据处理完成: 平均值={result['mean']:.1f}")
    return result


async def save_results(results: List[Dict]) -> bool:
    """模拟结果保存"""
    await asyncio.sleep(0.2)
    print(f"已保存 {len(results)} 条结果")
    return True


async def data_pipeline():
    """异步数据处理管道"""
    print("\n" + "=" * 60)
    print("异步数据处理管道")
    print("=" * 60)
    
    start = time.time()
    
    # 并发获取多批数据
    batches = await asyncio.gather(
        *[fetch_data_batch(i) for i in range(1, 4)]
    )
    
    # 并发处理数据
    processed = await asyncio.gather(
        *[process_data_batch(batch) for batch in batches]
    )
    
    # 保存结果
    await save_results(processed)
    
    elapsed = time.time() - start
    print(f"管道总耗时: {elapsed:.2f} 秒")


asyncio.run(data_pipeline())


# ================================
# 3. 异步任务队列
# ================================

class AsyncTaskQueue:
    """异步任务队列"""
    
    def __init__(self, max_concurrent: int = 3):
        self.queue = asyncio.Queue()
        self.max_concurrent = max_concurrent
        self.results = []
    
    async def worker(self, worker_id: int):
        """工作线程"""
        while True:
            task_id, task_func = await self.queue.get()
            
            if task_id is None:
                break
            
            print(f"  Worker {worker_id} 开始任务 {task_id}")
            result = await task_func()
            self.results.append((task_id, result))
            print(f"  Worker {worker_id} 完成任务 {task_id}")
            
            self.queue.task_done()
    
    async def add_task(self, task_id: int, task_func):
        """添加任务"""
        await self.queue.put((task_id, task_func))
    
    async def run(self, tasks: List[tuple]):
        """运行任务队列"""
        # 添加所有任务
        for task_id, task_func in tasks:
            await self.add_task(task_id, task_func)
        
        # 创建工作线程
        workers = [
            asyncio.create_task(self.worker(i))
            for i in range(self.max_concurrent)
        ]
        
        # 等待所有任务完成
        await self.queue.join()
        
        # 停止工作线程
        for _ in range(self.max_concurrent):
            await self.queue.put((None, None))
        
        await asyncio.gather(*workers)
        
        return self.results


async def task_queue_example():
    """任务队列示例"""
    print("\n" + "=" * 60)
    print("异步任务队列")
    print("=" * 60)
    
    queue = AsyncTaskQueue(max_concurrent=2)
    
    async def sample_task():
        await asyncio.sleep(random.uniform(0.2, 0.5))
        return random.randint(1, 100)
    
    tasks = [(i, sample_task) for i in range(1, 7)]
    
    start = time.time()
    results = await queue.run(tasks)
    elapsed = time.time() - start
    
    print(f"\n总耗时: {elapsed:.2f} 秒")
    print(f"结果: {results}")


asyncio.run(task_queue_example())


# ================================
# 4. 异步重试机制
# ================================

class AsyncRetry:
    """异步重试装饰器"""
    
    def __init__(self, max_retries: int = 3, delay: float = 0.5):
        self.max_retries = max_retries
        self.delay = delay
    
    async def __call__(self, func, *args, **kwargs):
        """执行带重试的异步函数"""
        for attempt in range(self.max_retries):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                if attempt < self.max_retries - 1:
                    print(f"  重试 {attempt + 1}/{self.max_retries}: {e}")
                    await asyncio.sleep(self.delay * (attempt + 1))
                else:
                    raise


async def unreliable_api_call(success_rate: float = 0.5) -> str:
    """模拟不稳定的 API 调用"""
    if random.random() > success_rate:
        raise ConnectionError("API 调用失败")
    return "API 调用成功"


async def retry_example():
    """重试示例"""
    print("\n" + "=" * 60)
    print("异步重试机制")
    print("=" * 60)
    
    retry_handler = AsyncRetry(max_retries=3, delay=0.5)
    
    try:
        result = await retry_handler(unreliable_api_call)
        print(f"结果: {result}")
    except Exception as e:
        print(f"最终失败: {e}")


asyncio.run(retry_example())


# ================================
# 5. 异步超时控制
# ================================

async def slow_operation(timeout: float = 2.0):
    """模拟慢操作"""
    print(f"开始慢操作，预计 {timeout} 秒后完成")
    await asyncio.sleep(timeout)
    return "操作完成"


async def timeout_example():
    """超时示例"""
    print("\n" + "=" * 60)
    print("异步超时控制")
    print("=" * 60)
    
    # 成功案例
    try:
        result = await asyncio.wait_for(slow_operation(1.0), timeout=2.0)
        print(f"成功: {result}")
    except asyncio.TimeoutError:
        print("操作超时")
    
    # 超时案例
    try:
        result = await asyncio.wait_for(slow_operation(3.0), timeout=2.0)
        print(f"成功: {result}")
    except asyncio.TimeoutError:
        print("操作超时")


asyncio.run(timeout_example())


# ================================
# 6. 异步缓存机制
# ================================

class AsyncCache:
    """异步缓存"""
    
    def __init__(self):
        self.cache = {}
        self.lock = asyncio.Lock()
    
    async def get(self, key: str):
        """获取缓存"""
        async with self.lock:
            return self.cache.get(key)
    
    async def set(self, key: str, value: Any):
        """设置缓存"""
        async with self.lock:
            self.cache[key] = value
    
    async def get_or_set(self, key: str, func):
        """获取或设置缓存"""
        value = await self.get(key)
        if value is not None:
            print(f"  命中缓存: {key}")
            return value
        
        print(f"  未命中缓存，执行函数: {key}")
        value = await func()
        await self.set(key, value)
        return value


async def cache_example():
    """缓存示例"""
    print("\n" + "=" * 60)
    print("异步缓存机制")
    print("=" * 60)
    
    cache = AsyncCache()
    
    async def expensive_operation():
        await asyncio.sleep(1)
        return "计算结果"
    
    # 第一次调用（未命中缓存）
    start = time.time()
    result1 = await cache.get_or_set("key1", expensive_operation)
    elapsed1 = time.time() - start
    print(f"第一次调用耗时: {elapsed1:.2f} 秒，结果: {result1}")
    
    # 第二次调用（命中缓存）
    start = time.time()
    result2 = await cache.get_or_set("key1", expensive_operation)
    elapsed2 = time.time() - start
    print(f"第二次调用耗时: {elapsed2:.2f} 秒，结果: {result2}")


asyncio.run(cache_example())


# ================================
# 7. 异步并发限制
# ================================

async def limited_concurrent_tasks():
    """限制并发数量的任务"""
    print("\n" + "=" * 60)
    print("异步并发限制")
    print("=" * 60)
    
    semaphore = asyncio.Semaphore(2)
    
    async def limited_task(task_id: int):
        async with semaphore:
            print(f"  任务 {task_id} 开始")
            await asyncio.sleep(1)
            print(f"  任务 {task_id} 完成")
            return task_id
    
    start = time.time()
    results = await asyncio.gather(
        *[limited_task(i) for i in range(1, 6)]
    )
    elapsed = time.time() - start
    
    print(f"总耗时: {elapsed:.2f} 秒")
    print(f"结果: {results}")


asyncio.run(limited_concurrent_tasks())


# ================================
# 练习题
# ================================

print("\n" + "=" * 60)
print("练习题")
print("=" * 60)


# 练习 1：实现异步批量文件处理
async def process_file_async(filename: str) -> Dict[str, Any]:
    """异步文件处理"""
    await asyncio.sleep(0.2)
    return {
        "filename": filename,
        "lines": random.randint(10, 100),
        "size": random.randint(1024, 10240)
    }


async def exercise1():
    """练习 1"""
    print("\n练习 1 - 批量文件处理:")
    
    files = [f"file_{i}.txt" for i in range(1, 6)]
    
    start = time.time()
    results = await asyncio.gather(
        *[process_file_async(f) for f in files]
    )
    elapsed = time.time() - start
    
    for r in results:
        print(f"  {r['filename']}: {r['lines']} 行, {r['size']} 字节")
    
    print(f"总耗时: {elapsed:.2f} 秒")


asyncio.run(exercise1())


# 练习 2：实现异步任务优先级队列
class PriorityAsyncQueue:
    """优先级异步队列"""
    
    def __init__(self):
        self.queue = asyncio.PriorityQueue()
    
    async def add_task(self, priority: int, task_id: int, task_func):
        """添加任务（优先级越小越先执行）"""
        await self.queue.put((priority, task_id, task_func))
    
    async def process_all(self):
        """处理所有任务"""
        results = []
        while not self.queue.empty():
            priority, task_id, task_func = await self.queue.get()
            print(f"  执行优先级 {priority} 的任务 {task_id}")
            result = await task_func()
            results.append((task_id, result))
        return results


async def exercise2():
    """练习 2"""
    print("\n练习 2 - 优先级队列:")
    
    queue = PriorityAsyncQueue()
    
    async def task():
        await asyncio.sleep(0.1)
        return "完成"
    
    await queue.add_task(3, 1, task)
    await queue.add_task(1, 2, task)
    await queue.add_task(2, 3, task)
    
    results = await queue.process_all()
    print(f"结果: {results}")


asyncio.run(exercise2())


# 练习 3：实现异步进度跟踪
class ProgressTracker:
    """异步进度跟踪器"""
    
    def __init__(self, total: int):
        self.total = total
        self.completed = 0
        self.lock = asyncio.Lock()
    
    async def update(self):
        """更新进度"""
        async with self.lock:
            self.completed += 1
            percentage = (self.completed / self.total) * 100
            print(f"  进度: {self.completed}/{self.total} ({percentage:.1f}%)")


async def exercise3():
    """练习 3"""
    print("\n练习 3 - 进度跟踪:")
    
    tracker = ProgressTracker(5)
    
    async def task_with_progress(task_id: int):
        await asyncio.sleep(random.uniform(0.2, 0.5))
        await tracker.update()
        return task_id
    
    await asyncio.gather(
        *[task_with_progress(i) for i in range(1, 6)]
    )
    
    print("所有任务完成！")


asyncio.run(exercise3())


# 练习 4：实现异步超时重试
async def retry_with_timeout(func, max_retries: int = 3, timeout: float = 1.0):
    """带超时的重试"""
    for attempt in range(max_retries):
        try:
            return await asyncio.wait_for(func(), timeout=timeout)
        except asyncio.TimeoutError:
            if attempt < max_retries - 1:
                print(f"  超时，重试 {attempt + 1}/{max_retries}")
            else:
                raise


async def exercise4():
    """练习 4"""
    print("\n练习 4 - 超时重试:")
    
    async def slow_task():
        await asyncio.sleep(2)
        return "任务完成"
    
    try:
        result = await retry_with_timeout(slow_task, max_retries=2, timeout=0.5)
        print(f"结果: {result}")
    except asyncio.TimeoutError:
        print("任务最终超时")


asyncio.run(exercise4())


# 练习 5：实现异步结果聚合
async def aggregate_results(tasks: List[tuple]) -> Dict[str, Any]:
    """聚合多个异步任务的结果"""
    results = await asyncio.gather(*[task() for _, task in tasks])
    
    return {
        "total": len(results),
        "successful": sum(1 for r in results if r.get("success", False)),
        "failed": sum(1 for r in results if not r.get("success", False)),
        "results": results
    }


async def exercise5():
    """练习 5"""
    print("\n练习 5 - 结果聚合:")
    
    async def task():
        await asyncio.sleep(0.2)
        return {"success": random.random() > 0.3, "data": random.randint(1, 100)}
    
    tasks = [(i, task) for i in range(5)]
    
    summary = await aggregate_results(tasks)
    print(f"总任务数: {summary['total']}")
    print(f"成功: {summary['successful']}, 失败: {summary['failed']}")


asyncio.run(exercise5())


print("\n✅ Day 9 学习完成！")
print("要点总结：")
print("1. 并发 vs 顺序：asyncio.gather 大幅提升性能")
print("2. 任务队列：异步队列管理并发任务")
print("3. 重试机制：提升系统健壮性")
print("4. 超时控制：防止任务无限等待")
print("5. 缓存机制：减少重复计算")
print("6. 并发限制：Semaphore 控制并发数")
print("7. 实际应用：LLM API 批量调用、数据处理管道")