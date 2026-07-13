"""
Day 9: 异步编程进阶 - 真实场景

学习目标：掌握异步编程在实际项目中的应用
"""


# ================================
# 练习 1：异步 Web 爬虫
# ================================
"""
任务：实现异步爬虫：

功能：
1. async_fetch(url, session)：
   - 使用 aiohttp 异步获取网页
   - 返回 HTML 内容

2. async_crawler(urls)：
   - 并发爬取多个 URL
   - 返回 {url: content} 字典

测试代码：
urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3"
]

start = time.time()
results = await async_crawler(urls)
print(f"爬取 {len(urls)} 个页面，总时间: {time.time() - start:.2f}秒")
"""

# TODO: 在这里实现异步爬虫（需要安装 aiohttp）




# ================================
# 练习 2：异步数据库操作
# ================================
"""
任务：实现异步数据库操作：

功能：
1. AsyncDatabase 类：
   - async connect()：连接数据库
   - async execute(query, params)：执行查询
   - async fetch_one(query)：查询单条
   - async fetch_all(query)：查询多条
   - async close()：关闭连接

测试代码：
db = AsyncDatabase("sqlite:///test.db")
await db.connect()

# 创建表
await db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# 插入数据
await db.execute("INSERT INTO users (name) VALUES (?)", ("张三",))

# 查询数据
users = await db.fetch_all("SELECT * FROM users")
print(users)

await db.close()
"""

# TODO: 在这里实现异步数据库（使用 aiosqlite）




# ================================
# 练习 3：异步 HTTP 服务器
# ================================
"""
任务：实现异步 HTTP 服务器：

功能：
1. 使用 aiohttp 创建 Web 服务器
2. 路由：
   - GET /：返回欢迎信息
   - GET /users：返回用户列表
   - POST /users：创建用户
3. 返回 JSON 格式数据

测试代码：
# 启动服务器
python server.py

# 测试请求
curl http://localhost:8080/
curl http://localhost:8080/users
curl -X POST http://localhost:8080/users -d '{"name":"张三"}'
"""

# TODO: 创建 server.py 实现异步 Web 服务器




# ================================
# 练习 4：异步 WebSocket 通信
# ================================
"""
任务：实现 WebSocket 聊天室：

功能：
1. 服务端：
   - 接收客户端连接
   - 广播消息给所有客户端

2. 客户端：
   - 连接服务器
   - 发送消息
   - 接收广播消息

测试代码：
# 服务端
async def chat_server():
    # 实现 WebSocket 服务器
    pass

# 客户端
async def chat_client(name):
    # 实现 WebSocket 客户端
    pass
"""

# TODO: 在这里实现 WebSocket 聊天室




# ================================
# 练习 5：异步任务队列
# ================================
"""
任务：实现异步任务队列系统：

功能：
1. TaskQueue 类：
   - enqueue(task)：添加任务
   - worker()：工作协程
   - start(n_workers)：启动 n 个工作协程
   - stop()：停止所有工作协程

2. 任务状态：
   - pending：待处理
   - running：运行中
   - completed：已完成
   - failed：失败

测试代码：
queue = TaskQueue()

# 添加任务
for i in range(10):
    await queue.enqueue({"id": i, "data": f"任务{i}"})

# 启动 3 个工作协程
await queue.start(n_workers=3)

# 等待所有任务完成
await queue.wait_all()

await queue.stop()
"""

# TODO: 在这里实现异步任务队列




# ================================
# 练习 6：异步定时任务
# ================================
"""
任务：实现异步定时任务调度器：

功能：
1. AsyncScheduler 类：
   - schedule(coro, interval)：定时执行协程
   - schedule_once(coro, delay)：延迟执行一次
   - cancel(task_id)：取消任务
   - start()：启动调度器
   - stop()：停止调度器

测试代码：
scheduler = AsyncScheduler()

# 每隔 2 秒执行
async def periodic_task():
    print(f"[{time.time():.2f}] 定时任务执行")

await scheduler.schedule(periodic_task, interval=2)

# 5 秒后执行一次
await scheduler.schedule_once(lambda: print("一次性任务"), delay=5)

# 启动调度器
await scheduler.start()

# 10 秒后停止
await asyncio.sleep(10)
await scheduler.stop()
"""

# TODO: 在这里实现异步定时任务调度器




# ================================
# 练习 7：异步日志系统
# ================================
"""
任务：实现异步日志系统：

功能：
1. AsyncLogger 类：
   - async log(level, message)：异步写日志
   - 支持不同级别：DEBUG、INFO、WARNING、ERROR
   - 支持写入文件和控制台
   - 支持日志轮转（按日期或大小）

2. 使用异步队列缓存日志：
   - log() 将日志放入队列
   - 后台协程异步写入文件
   - 避免阻塞主线程

测试代码：
logger = AsyncLogger("app.log")

await logger.info("系统启动")
await logger.debug("调试信息")
await logger.error("错误信息")

await logger.close()
"""

# TODO: 在这里实现异步日志系统




# ================================
# 验证你的实现
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("Day 9 练习验证 - 异步进阶场景")
    print("=" * 60)
    
    # 测试练习 1
    print("\n--- 练习 1：异步爬虫 ---")
    # urls = ["https://httpbin.org/delay/1"]
    # results = asyncio.run(async_crawler(urls))
    # print(results)
    
    # 测试练习 5
    print("\n--- 练习 5：任务队列 ---")
    # queue = TaskQueue()
    # await queue.start(n_workers=3)
    # for i in range(5):
    #     await queue.enqueue({"id": i})
    # await queue.wait_all()
    # await queue.stop()
    
    print("\n✅ Day 9 练习完成！")
    print("重点：Web服务器、数据库、WebSocket、任务队列")