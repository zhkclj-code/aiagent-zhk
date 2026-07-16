"""
Day 7-8: 异步编程基础

学习目标：理解 Python 异步编程原理和应用
"""

# ================================
# 0. 异步编程核心概念 - Java开发者必读
# ================================

"""
【什么是异步编程】
异步编程是一种非阻塞的编程范式，允许程序在等待I/O操作时继续执行其他任务。
核心机制：协程+ 事件循环

【和Java的对比】
| 维度 | Python async/await | Java并发方案 |
|-----|-------------------|------------|
| 并发单位 | 协程 | 线程 |
| 调度方式 | 协作式（主动让出） | 抢占式（OS切换） |
| 内存开销 | ~2KB | ~1MB |
| 并行能力 | 单线程（受GIL限制） | 多线程真正并行 |
| 适用场景 | I/O密集型 | I/O密集型 + CPU密集型 |

【关键概念对比表】

Python async                      Java 对应方案
─────────────────────────────────────────────────────
async def                         Runnable/Callable
await task                        Future.get()
asyncio.run()                     ExecutorService.submit()
asyncio.gather()                  CompletableFuture.allOf()
asyncio.create_task()             CompletableFuture.supplyAsync()
asyncio.Semaphore                 java.util.concurrent.Semaphore
asyncio.Queue                     BlockingQueue

【Python协程 vs Java线程的本质区别】

1. 调度机制：
   - Python: 协程在单线程内协作式调度（await主动让出控制权）
   - Java: 线程由操作系统抢占式调度（可能随时被切换）

2. GIL（全局解释器锁）的影响：
   - Python: 同一时刻只有一个线程执行Python字节码
   - Java: 多线程真正并行执行

3. 创建开销：
   - Python协程: 创建成本极低（~2KB），可以轻松创建10万+协程
   - Java线程: 创建成本高（~1MB），通常限制线程池大小

4. 适用场景：
   Python async ✅ 适用：
   - HTTP API调用
   - 数据库查询
   - 文件I/O
   - 网络通信

   Python async ❌ 不适用：
   - CPU密集计算（GIL限制，用multiprocessing代替）
   - 简单脚本（增加复杂度不值得）

   Java线程 ✅ 适用：
   - CPU密集计算
   - I/O密集型
   - 阻塞操作

【async/await的工作原理】

async def my_func():
    result = await other_func()
    # ↑ 等价于：
    # 1. 暂停当前协程，保存状态
    # 2. 让出控制权给事件循环
    # 3. 事件循环调度其他协程执行
    # 4. other_func()完成后恢复当前协程

【事件循环】
Python asyncio的事件循环类似于Java的ExecutorService，负责：
- 调度协程执行
- 管理I/O事件
- 处理定时任务
- 协调协程间的切换

【常见陷阱】
1. 在async函数中调用阻塞函数（如time.sleep、requests.get）
   → 会阻塞整个事件循环！必须用asyncio.sleep、aiohttp
2. 忘记await协程
   → 协程不会执行，只是创建了一个coroutine对象
3. 混用同步和异步代码
   → 需要用asyncio.run_in_executor()包装同步代码

【最佳实践】
1. I/O密集型任务优先用异步
2. CPU密集型用multiprocessing（绕过GIL）
3. 已有的同步库用run_in_executor包装
4. 使用aiohttp代替requests
5. 使用asyncpg/aiomysql代替psycopg2/mysql-connector

【Java开发者迁移建议】
- Java Thread → Python asyncio.create_task()
- Java ExecutorService → Python asyncio.run()
- Java Future.get() → Python await task
- Java CompletableFuture.thenApply() → Python async函数组合
- Java synchronized → Python asyncio.Lock()
"""

# ================================
# 1. 同步 vs 异步（概念理解）
# ================================

import time

# 同步代码（顺序执行）
def sync_task(name: str, duration: float) -> str:
    """同步任务"""
    print(f"开始任务: {name}")
    time.sleep(duration)  # 阻塞等待
    print(f"完成任务: {name}")
    return f"{name} 完成"


def sync_main():
    """同步主函数"""
    start = time.time()
    
    result1 = sync_task("任务1", 1)
    result2 = sync_task("任务2", 1)
    result3 = sync_task("任务3", 1)
    
    elapsed = time.time() - start
    print(f"\n同步执行总耗时: {elapsed:.2f} 秒")
    print(f"结果: {result1}, {result2}, {result3}")


print("同步执行:")
sync_main()


# ================================
# 2. 异步编程基础
# ================================

import asyncio

# 异步函数（协程）
async def async_task(name: str, duration: float) -> str:
    """异步任务"""
    print(f"开始任务: {name}")
    await asyncio.sleep(duration)  # 非阻塞等待
    print(f"完成任务: {name}")
    return f"{name} 完成"


async def async_main():
    """异步主函数"""
    start = time.time()
    
    # 并发执行 3 个任务
    result1, result2, result3 = await asyncio.gather(
        async_task("任务1", 1),
        async_task("任务2", 1),
        async_task("任务3", 1)
    )
    
    elapsed = time.time() - start
    print(f"\n异步执行总耗时: {elapsed:.2f} 秒")
    print(f"结果: {result1}, {result2}, {result3}")


print("\n异步执行:")
asyncio.run(async_main())


# ================================
# 3. async/await 语法
# ================================

async def fetch_data(url: str) -> str:
    """模拟异步获取数据"""
    print(f"正在获取: {url}")
    await asyncio.sleep(0.5)  # 模拟网络延迟
    return f"数据来自 {url}"


async def process_data(data: str) -> str:
    """处理数据"""
    print(f"正在处理: {data}")
    await asyncio.sleep(0.2)
    return f"处理后的 {data}"


async def workflow():
    """工作流"""
    # 顺序执行
    data = await fetch_data("https://api.example.com")
    processed = await process_data(data)
    return processed


# 运行异步函数
print("\n异步工作流:")
result = asyncio.run(workflow())
print(f"结果: {result}")


# ================================
# 4. 并发执行多个任务
# ================================

async def concurrent_tasks():
    """并发执行多个任务"""
    start = time.time()
    
    # 方式 1：使用 gather
    results = await asyncio.gather(
        fetch_data("api1.example.com"),
        fetch_data("api2.example.com"),
        fetch_data("api3.example.com")
    )
    
    elapsed = time.time() - start
    print(f"\n并发执行耗时: {elapsed:.2f} 秒")
    print(f"结果: {results}")
    
    return results


asyncio.run(concurrent_tasks())


# ================================
# 5. 任务创建和管理
# ================================

async def task_management():
    """任务管理"""
    print("\n任务管理:")
    
    # 创建任务
    task1 = asyncio.create_task(fetch_data("api1.com"))
    task2 = asyncio.create_task(fetch_data("api2.com"))
    task3 = asyncio.create_task(fetch_data("api3.com"))
    
    print("任务已创建，开始等待...")
    
    # 等待任务完成
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(f"任务结果: {result1}, {result2}, {result3}")


asyncio.run(task_management())


# ================================
# 6. 超时处理
# ================================

async def slow_task():
    """慢任务"""
    await asyncio.sleep(5)
    return "慢任务完成"


async def timeout_example():
    """超时示例"""
    print("\n超时处理:")
    
    try:
        # 设置 1 秒超时
        result = await asyncio.wait_for(slow_task(), timeout=1.0)
        print(f"结果: {result}")
    except asyncio.TimeoutError:
        print("任务超时！")


asyncio.run(timeout_example())


# ================================
# 7. 异步迭代器和生成器
# ================================

async def async_generator():
    """异步生成器"""
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i


async def async_iteration():
    """异步迭代"""
    print("\n异步迭代:")
    
    # 方式 1：使用 async for
    async for num in async_generator():
        print(f"  生成: {num}")
    
    # 方式 2：转换为列表
    numbers = [num async for num in async_generator()]
    print(f"  列表: {numbers}")


asyncio.run(async_iteration())


# ================================
# 8. 异步上下文管理器
# ================================

class AsyncTimer:
    """异步计时器"""
    
    async def __aenter__(self):
        """进入上下文"""
        self.start = time.time()
        print("计时开始...")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        elapsed = time.time() - self.start
        print(f"计时结束，耗时: {elapsed:.2f} 秒")


async def async_context_example():
    """异步上下文管理器示例"""
    print("\n异步上下文管理器:")
    
    async with AsyncTimer():
        await asyncio.sleep(0.5)
        print("执行异步任务...")


asyncio.run(async_context_example())


# ================================
# 9. 异步队列
# ================================

async def producer(queue: asyncio.Queue, name: str):
    """生产者"""
    for i in range(3):
        item = f"{name}-item-{i}"
        await queue.put(item)
        print(f"生产: {item}")
        await asyncio.sleep(0.1)


async def consumer(queue: asyncio.Queue, name: str):
    """消费者"""
    while True:
        item = await queue.get()
        print(f"  消费者 {name} 消费: {item}")
        queue.task_done()
        await asyncio.sleep(0.2)


async def queue_example():
    """队列示例"""
    print("\n异步队列:")
    
    queue = asyncio.Queue()
    
    # 启动生产者和消费者
    producers = [
        asyncio.create_task(producer(queue, f"生产者{i}"))
        for i in range(2)
    ]
    
    consumers = [
        asyncio.create_task(consumer(queue, f"消费者{i}"))
        for i in range(2)
    ]
    
    # 等待生产者完成
    await asyncio.gather(*producers)
    
    # 等待队列清空
    await queue.join()
    
    # 取消消费者
    for c in consumers:
        c.cancel()


asyncio.run(queue_example())


# ================================
# 10. 并发限制
# ================================

async def limited_concurrency():
    """限制并发数量"""
    print("\n并发限制:")
    
    # 信号量：限制同时运行的任务数
    semaphore = asyncio.Semaphore(2)
    
    async def limited_task(task_id: int):
        """受限任务"""
        async with semaphore:
            print(f"  任务 {task_id} 开始")
            await asyncio.sleep(1)
            print(f"  任务 {task_id} 完成")
            return task_id
    
    # 启动 5 个任务，但最多同时运行 2 个
    tasks = [limited_task(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(f"结果: {results}")


asyncio.run(limited_concurrency())


# ================================
# 11. 异步 HTTP 请求（实际应用）
# ================================

async def async_http_request():
    """异步 HTTP 请求"""
    print("\n异步 HTTP 请求:")
    
    import aiohttp
    
    urls = [
        "https://www.baidu.com",
        "https://www.qq.com",
        "https://www.taobao.com"
    ]
    
    async def fetch(url: str) -> tuple:
        """获取网页"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                return url, response.status
    
    # 并发请求
    start = time.time()
    try:
        results = await asyncio.gather(
            *[fetch(url) for url in urls],
            return_exceptions=True
        )
        elapsed = time.time() - start
        
        for result in results:
            if isinstance(result, Exception):
                print(f"  请求失败: {result}")
            else:
                print(f"  {result[0]}: HTTP {result[1]}")
        
        print(f"总耗时: {elapsed:.2f} 秒")
    except Exception as e:
        print(f"HTTP 请求失败: {e}")


# 网络示例需要显式开启，避免课程运行依赖外部网络。
import os

if os.getenv("RUN_NETWORK_EXAMPLES") == "1":
    try:
        import aiohttp
    except ImportError:
        print("\n未安装 aiohttp，跳过 HTTP 请求示例")
        print("安装命令: pip install aiohttp")
    else:
        asyncio.run(async_http_request())
else:
    print("\n网络示例默认关闭；设置 RUN_NETWORK_EXAMPLES=1 后运行")


# ================================
# 练习题
# ================================

print("\n" + "="*60)
print("练习题")
print("="*60)


# 练习 1：编写异步函数，模拟数据库查询
async def query_database(query: str) -> str:
    """模拟数据库查询"""
    await asyncio.sleep(0.5)
    return f"查询结果: {query}"


async def exercise1():
    """练习 1"""
    start = time.time()
    results = await asyncio.gather(
        query_database("SELECT * FROM users"),
        query_database("SELECT * FROM orders"),
        query_database("SELECT * FROM products")
    )
    elapsed = time.time() - start
    print(f"练习 1 - 数据库查询耗时: {elapsed:.2f} 秒")
    for r in results:
        print(f"  {r}")


asyncio.run(exercise1())


# 练习 2：使用异步生成器生成斐波那契数列
async def async_fibonacci(n: int):
    """异步斐波那契生成器"""
    a, b = 0, 1
    for _ in range(n):
        await asyncio.sleep(0.05)
        yield a
        a, b = b, a + b


async def exercise2():
    """练习 2"""
    print("\n练习 2 - 异步斐波那契数列:")
    numbers = [num async for num in async_fibonacci(10)]
    print(f"  前 10 项: {numbers}")


asyncio.run(exercise2())


# 练习 3：实现异步倒计时
async def countdown(name: str, seconds: int):
    """异步倒计时"""
    for i in range(seconds, 0, -1):
        print(f"  {name}: {i}")
        await asyncio.sleep(0.5)
    return f"{name} 完成"


async def exercise3():
    """练习 3"""
    print("\n练习 3 - 并发倒计时:")
    results = await asyncio.gather(
        countdown("倒计时1", 3),
        countdown("倒计时2", 3)
    )
    print(f"结果: {results}")


asyncio.run(exercise3())


# 练习 4：实现异步任务超时和重试
async def retry_task(task, max_retries: int = 3, timeout: float = 1.0):
    """带重试的任务"""
    for attempt in range(max_retries):
        try:
            result = await asyncio.wait_for(task(), timeout=timeout)
            return result
        except asyncio.TimeoutError:
            print(f"  重试 {attempt + 1}/{max_retries}")
            if attempt == max_retries - 1:
                raise
    return None


async def slow_task_func():
    """模拟慢任务"""
    await asyncio.sleep(2)
    return "任务完成"


async def exercise4():
    """练习 4"""
    print("\n练习 4 - 超时重试:")
    try:
        result = await retry_task(slow_task_func, max_retries=2, timeout=0.5)
        print(f"  结果: {result}")
    except asyncio.TimeoutError:
        print("  任务最终超时")


asyncio.run(exercise4())


# 练习 5：实现异步任务调度器
class AsyncTaskScheduler:
    """异步任务调度器"""
    
    def __init__(self, max_concurrent: int = 3):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.results = []
    
    async def run_task(self, task_id: int, duration: float):
        """运行任务"""
        async with self.semaphore:
            print(f"  任务 {task_id} 开始")
            await asyncio.sleep(duration)
            result = f"任务 {task_id} 完成"
            print(f"  任务 {task_id} 结束")
            return result
    
    async def run_all(self, tasks: list[tuple[int, float]]):
        """运行所有任务"""
        results = await asyncio.gather(
            *[self.run_task(task_id, duration) for task_id, duration in tasks]
        )
        return results


async def exercise5():
    """练习 5"""
    print("\n练习 5 - 任务调度器:")
    scheduler = AsyncTaskScheduler(max_concurrent=2)
    
    tasks = [
        (1, 0.5),
        (2, 0.5),
        (3, 0.5),
        (4, 0.5),
        (5, 0.5)
    ]
    
    start = time.time()
    results = await scheduler.run_all(tasks)
    elapsed = time.time() - start
    
    print(f"总耗时: {elapsed:.2f} 秒")
    print(f"结果: {results}")


asyncio.run(exercise5())


print("\n✅ Day 7-8 学习完成！")
print("要点总结：")
print("1. 异步关键字：async def、await")
print("2. 并发执行：asyncio.gather()")
print("3. 任务管理：asyncio.create_task()")
print("4. 超时处理：asyncio.wait_for()")
print("5. 异步迭代：async for、async with")
print("6. 并发限制：asyncio.Semaphore()")
print("7. 异步队列：asyncio.Queue()")
print("8. 实际应用：异步 HTTP 请求、数据库查询")
