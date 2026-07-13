"""
Day 7: 异步编程基础练习

学习目标：理解异步编程概念和 asyncio 基础
"""


# ================================
# 练习 1：理解同步 vs 异步
# ================================
"""
任务：对比同步和异步代码的执行时间：

1. 同步版本：
   def sync_task(name, seconds):
       print(f"开始任务 {name}")
       time.sleep(seconds)
       print(f"完成任务 {name}")
       return f"{name} 结果"

   def sync_main():
       start = time.time()
       sync_task("A", 2)
       sync_task("B", 2)
       print(f"总时间: {time.time() - start:.2f}秒")

2. 异步版本：
   async def async_task(name, seconds):
       print(f"开始任务 {name}")
       await asyncio.sleep(seconds)
       print(f"完成任务 {name}")
       return f"{name} 结果"

   async def async_main():
       start = time.time()
       await asyncio.gather(
           async_task("A", 2),
           async_task("B", 2)
       )
       print(f"总时间: {time.time() - start:.2f}秒")

测试：
分别运行 sync_main() 和 async_main()
观察执行时间差异
"""

# TODO: 在这里实现同步和异步版本，对比执行时间




# ================================
# 练习 2：基础异步函数
# ================================
"""
任务：创建异步函数：

1. async_hello(name)：延迟 1 秒后打印 "Hello, {name}!"

2. async_count(start, end)：从 start 到 end 计数，每秒打印一个数字

测试代码：
async def main():
    await async_hello("张三")
    await async_count(1, 5)

asyncio.run(main())

预期输出：
(1秒后) Hello, 张三!
(每秒) 1 2 3 4 5
"""

# TODO: 在这里实现 async_hello 和 async_count




# ================================
# 练习 3：asyncio.gather 并发执行
# ================================
"""
任务：使用 asyncio.gather 并发执行多个任务：

1. 创建 fetch_url(url) 异步函数：
   - 模拟网络请求（延迟 1-3 秒）
   - 返回 "数据来自 {url}"

2. 创建 fetch_all(urls) 异步函数：
   - 并发获取所有 URL 的数据
   - 返回结果列表

测试代码：
urls = ["url1", "url2", "url3", "url4", "url5"]
results = await fetch_all(urls)
for result in results:
    print(result)

观察：总时间应接近最长单个请求时间（而不是所有请求时间之和）
"""

# TODO: 在这里实现 fetch_url 和 fetch_all




# ================================
# 练习 4：asyncio.wait 和超时
# ================================
"""
任务：实现带超时的异步操作：

1. 创建 slow_task(name, seconds) 异步函数：
   - 延迟指定秒数
   - 返回 "{name} 完成"

2. 创建 run_with_timeout(tasks, timeout) 异步函数：
   - 并发执行任务
   - 如果超时，取消未完成的任务
   - 返回已完成的结果

测试代码：
tasks = [slow_task("A", 1), slow_task("B", 5), slow_task("C", 2)]
results = await run_with_timeout(tasks, timeout=3)
print(results)

预期输出：任务 A 和 C 完成，B 因超时被取消
"""

# TODO: 在这里实现 slow_task 和 run_with_timeout




# ================================
# 练习 5：异步上下文管理器
# ================================
"""
任务：创建异步上下文管理器：

1. AsyncTimer 类：
   - __aenter__：记录开始时间
   - __aexit__：打印执行时间

2. AsyncFile 类：
   - __aenter__：异步打开文件
   - __aexit__：异步关闭文件

测试代码：
async with AsyncTimer("测试"):
    await asyncio.sleep(1)
    
async with AsyncFile("test.txt", "w") as f:
    await f.write("异步写入")
"""

# TODO: 在这里实现 AsyncTimer 和 AsyncFile




# ================================
# 练习 6：异步生成器
# ================================
"""
任务：创建异步生成器：

1. async_count_generator(start, end) 异步生成器：
   - 每秒生成一个数字
   - 使用 async for 迭代

2. async_fibonacci(n) 异步生成器：
   - 生成斐波那契数列前 n 项
   - 每项延迟 0.1 秒

测试代码：
async for num in async_count_generator(1, 5):
    print(num)

async for fib in async_fibonacci(10):
    print(fib)
"""

# TODO: 在这里实现异步生成器




# ================================
# 练习 7：异步队列
# ================================
"""
任务：使用 asyncio.Queue 实现生产者-消费者：

1. producer(queue, items) 异步函数：
   - 将 items 放入队列
   - 每次放入延迟 0.5 秒

2. consumer(queue, name) 异步函数：
   - 从队列取出项目
   - 处理项目（延迟 1 秒）
   - 打印 "{name} 处理了 {item}"

3. main() 异步函数：
   - 创建队列
   - 启动生产者和多个消费者
   - 等待完成

测试代码：
await main()

预期输出：
生产者放入项目
消费者并发处理
"""

# TODO: 在这里实现生产者-消费者模式




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    import asyncio
    import time
    
    print("=" * 60)
    print("Day 7 练习验证")
    print("=" * 60)
    
    # 测试练习 1
    print("\n--- 练习 1：同步 vs 异步 ---")
    # sync_main()
    # asyncio.run(async_main())
    
    # 测试练习 2
    print("\n--- 练习 2：基础异步函数 ---")
    # asyncio.run(main())
    
    # 测试练习 3
    print("\n--- 练习 3：并发执行 ---")
    # urls = ["url1", "url2", "url3"]
    # results = asyncio.run(fetch_all(urls))
    # print(results)
    
    # 测试练习 4
    print("\n--- 练习 4：超时控制 ---")
    # tasks = [slow_task("A", 1), slow_task("B", 5)]
    # results = asyncio.run(run_with_timeout(tasks, timeout=3))
    # print(results)
    
    # 测试练习 5
    print("\n--- 练习 5：异步上下文 ---")
    # async def test_timer():
    #     async with AsyncTimer("测试"):
    #         await asyncio.sleep(1)
    # asyncio.run(test_timer())
    
    # 测试练习 6
    print("\n--- 练习 6：异步生成器 ---")
    # async def test_gen():
    #     async for num in async_count_generator(1, 5):
    #         print(num)
    # asyncio.run(test_gen())
    
    # 测试练习 7
    print("\n--- 练习 7：异步队列 ---")
    # asyncio.run(main())
    
    print("\n✅ Day 7 练习完成！")
    print("关键概念：async/await、asyncio.gather、异步生成器")