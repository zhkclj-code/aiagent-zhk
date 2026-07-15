"""
Day 8: 异步编程练习题

学习目标：
- 掌握异步并发控制模式
- 理解任务依赖与编排
- 实现生产环境常见异步模式
- 提升异步编程实战能力

运行方式：python practice_day8.py
"""

import asyncio
import time
import random
from typing import List, Dict, Any, Callable
from collections import defaultdict


# ============================================================
# 练习 1：异步批量请求合并器
# ============================================================
"""
【问题描述】
在 LLM API 调用场景中，频繁的小批量请求会导致高延迟和高成本。
实现一个批量请求合并器，将多个小请求合并成一个批量请求，
减少 API 调用次数。

【要求】
1. 实现请求收集窗口（等待一定时间收集请求）
2. 达到批量上限或超时后触发批量处理
3. 每个请求能够获取到对应的响应结果

【预期行为】
- 连续发起多个请求时，自动合并为批量处理
- 不超过批量上限时等待窗口时间
- 每个请求返回正确对应的结果
"""

class BatchRequestMerger:
    """异步批量请求合并器"""
    
    def __init__(self, batch_size: int = 3, wait_time: float = 0.5):
        """
        初始化
        
        Args:
            batch_size: 批量大小上限
            wait_time: 等待时间窗口（秒）
        """
        self.batch_size = batch_size
        self.wait_time = wait_time
        self.pending_requests = []
        self.batch_id = 0
    
    async def add_request(self, request_data: Any) -> Any:
        """
        添加请求并等待结果
        
        TODO: 实现以下逻辑
        1. 创建一个 Future 用于接收结果
        2. 将请求添加到待处理列表
        3. 如果达到批量上限，立即触发批量处理
        4. 否则，等待一段时间后触发批量处理
        5. 等待 Future 完成并返回结果
        
        Args:
            request_data: 请求数据
            
        Returns:
            对应的响应结果
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        future = asyncio.Future()
        self.pending_requests.append((request_data, future))
        
        if len(self.pending_requests) >= self.batch_size:
            asyncio.create_task(self._process_batch())
        else:
            await asyncio.sleep(self.wait_time)
            if not future.done():
                asyncio.create_task(self._process_batch())
        
        return await future
    
    async def _process_batch(self):
        """
        处理当前批次
        
        TODO: 实现以下逻辑
        1. 获取并清空当前待处理列表
        2. 批量处理所有请求（模拟 LLM API 调用）
        3. 将结果设置到各个 Future
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        if not self.pending_requests:
            return
        
        batch = self.pending_requests[:]
        self.pending_requests = []
        
        requests = [req for req, _ in batch]
        futures = [f for _, f in batch]
        
        results = await self._mock_batch_api_call(requests)
        
        for future, result in zip(futures, results):
            if not future.done():
                future.set_result(result)
    
    async def _mock_batch_api_call(self, requests: List[Any]) -> List[Any]:
        """模拟批量 API 调用"""
        await asyncio.sleep(0.3)  # 模拟网络延迟
        return [f"响应_{i}_{req}" for i, req in enumerate(requests)]


async def test_batch_merger():
    """测试批量请求合并器"""
    print("\n" + "=" * 60)
    print("练习 1：异步批量请求合并器")
    print("=" * 60)
    
    merger = BatchRequestMerger(batch_size=3, wait_time=0.5)
    
    # 模拟并发发起 5 个请求
    async def make_request(request_id: int):
        print(f"  发起请求 {request_id}")
        result = await merger.add_request(f"prompt_{request_id}")
        print(f"  收到响应 {request_id}: {result}")
        return result
    
    start = time.time()
    results = await asyncio.gather(
        *[make_request(i) for i in range(1, 6)]
    )
    elapsed = time.time() - start
    
    print(f"\n总耗时: {elapsed:.2f} 秒")
    print(f"结果数量: {len(results)}")
    
    # 验证
    print("\n【验证点】")
    print(f"✓ 请求被合并处理（耗时应小于顺序执行的 1.5 秒）")
    print(f"✓ 每个请求都能获得正确响应")


# ============================================================
# 练习 2：异步限流器
# ============================================================
"""
【问题描述】
LLM API 通常有速率限制（如每分钟 60 次请求）。
实现一个异步限流器，控制单位时间内的请求数量，
避免触发 API 限流。

【要求】
1. 实现基于滑动窗口的限流
2. 超过限制时自动等待
3. 支持多个并发请求的公平调度

【预期行为】
- 请求数未超限时立即执行
- 超限时等待直到可以执行
- 多个等待请求按顺序执行
"""

class AsyncRateLimiter:
    """异步限流器"""
    
    def __init__(self, max_requests: int, time_window: float):
        """
        初始化
        
        Args:
            max_requests: 时间窗口内最大请求数
            time_window: 时间窗口（秒）
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []
        self.lock = asyncio.Lock()
    
    async def acquire(self):
        """
        获取执行许可
        
        TODO: 实现以下逻辑
        1. 加锁检查当前时间窗口内的请求数
        2. 如果未超限，记录请求时间并返回
        3. 如果超限，计算需要等待的时间
        4. 等待后重新检查
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        while True:
            async with self.lock:
                now = time.time()
                # 清理过期的请求记录
                self.requests = [t for t in self.requests if now - t < self.time_window]
                
                if len(self.requests) < self.max_requests:
                    self.requests.append(now)
                    return
                
                # 计算需要等待的时间
                wait_time = self.time_window - (now - self.requests[0])
            
            await asyncio.sleep(wait_time)


async def test_rate_limiter():
    """测试异步限流器"""
    print("\n" + "=" * 60)
    print("练习 2：异步限流器")
    print("=" * 60)
    
    limiter = AsyncRateLimiter(max_requests=2, time_window=1.0)
    
    async def make_request(request_id: int):
        await limiter.acquire()
        print(f"  [{time.time():.2f}] 执行请求 {request_id}")
        await asyncio.sleep(0.1)  # 模拟请求处理
    
    start = time.time()
    await asyncio.gather(
        *[make_request(i) for i in range(1, 6)]
    )
    elapsed = time.time() - start
    
    print(f"\n总耗时: {elapsed:.2f} 秒")
    
    print("\n【验证点】")
    print(f"✓ 限制为每秒 2 个请求，5 个请求应耗时约 2 秒")
    print(f"✓ 实际耗时: {elapsed:.2f} 秒")


# ============================================================
# 练习 3：异步事件广播器
# ============================================================
"""
【问题描述】
在 Agent 系统中，一个事件可能需要触发多个处理程序。
实现异步事件广播器，支持发布-订阅模式，
一个事件可以同时通知多个订阅者。

【要求】
1. 实现订阅/取消订阅功能
2. 发布事件时异步通知所有订阅者
3. 支持订阅者处理失败时的容错

【预期行为】
- 事件发布后所有订阅者都能收到
- 订阅者可以异步处理事件
- 一个订阅者失败不影响其他订阅者
"""

class AsyncEventBroadcaster:
    """异步事件广播器"""
    
    def __init__(self):
        self.subscribers = defaultdict(list)
    
    def subscribe(self, event_type: str, handler: Callable):
        """
        订阅事件
        
        TODO: 实现订阅逻辑
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        self.subscribers[event_type].append(handler)
    
    def unsubscribe(self, event_type: str, handler: Callable):
        """
        取消订阅
        
        TODO: 实现取消订阅逻辑
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        if handler in self.subscribers[event_type]:
            self.subscribers[event_type].remove(handler)
    
    async def publish(self, event_type: str, data: Any):
        """
        发布事件
        
        TODO: 实现以下逻辑
        1. 获取该事件类型的所有订阅者
        2. 并发调用所有订阅者的处理函数
        3. 捕获每个订阅者的异常，不影响其他订阅者
        4. 返回处理结果统计
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        handlers = self.subscribers.get(event_type, [])
        if not handlers:
            return {"total": 0, "successful": 0, "failed": 0}
        
        results = {"total": len(handlers), "successful": 0, "failed": 0}
        
        async def safe_call(handler):
            try:
                await handler(data)
                results["successful"] += 1
            except Exception as e:
                results["failed"] += 1
        
        await asyncio.gather(*[safe_call(h) for h in handlers])
        return results


async def test_event_broadcaster():
    """测试事件广播器"""
    print("\n" + "=" * 60)
    print("练习 3：异步事件广播器")
    print("=" * 60)
    
    broadcaster = AsyncEventBroadcaster()
    
    # 定义订阅者
    async def log_handler(data):
        await asyncio.sleep(0.1)
        print(f"  [日志] 收到事件: {data}")
        return "logged"
    
    async def notify_handler(data):
        await asyncio.sleep(0.15)
        print(f"  [通知] 发送通知: {data}")
        return "notified"
    
    async def analytics_handler(data):
        await asyncio.sleep(0.2)
        print(f"  [分析] 记录指标: {data}")
        return "recorded"
    
    # 订阅事件
    broadcaster.subscribe("user_login", log_handler)
    broadcaster.subscribe("user_login", notify_handler)
    broadcaster.subscribe("user_login", analytics_handler)
    
    # 发布事件
    print("发布事件: user_login")
    result = await broadcaster.publish("user_login", {"user_id": 123, "time": "10:00"})
    
    print(f"\n事件处理结果: {result}")
    
    print("\n【验证点】")
    print(f"✓ 三个订阅者都被触发")
    print(f"✓ 并发执行，总耗时约 0.2 秒（而非 0.45 秒）")


# ============================================================
# 练习 4：异步任务依赖图
# ============================================================
"""
【问题描述】
在复杂的工作流中，任务之间存在依赖关系。
例如：任务 B 必须等任务 A 完成后才能执行。
实现异步任务依赖图，支持定义任务依赖并自动调度执行。

【要求】
1. 支持添加任务和依赖关系
2. 自动检测循环依赖
3. 并行执行无依赖的任务
4. 按依赖顺序执行有依赖的任务

【预期行为】
- 无依赖的任务并发执行
- 有依赖的任务按正确顺序执行
- 检测到循环依赖时抛出异常
"""

class AsyncTaskGraph:
    """异步任务依赖图"""
    
    def __init__(self):
        self.tasks = {}
        self.dependencies = defaultdict(list)
        self.results = {}
    
    def add_task(self, task_id: str, task_func: Callable, depends_on: List[str] = None):
        """
        添加任务
        
        TODO: 实现添加任务逻辑
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        self.tasks[task_id] = task_func
        self.dependencies[task_id] = depends_on or []
    
    def _detect_cycle(self) -> bool:
        """
        检测循环依赖
        
        TODO: 使用 DFS 或拓扑排序检测
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        visited = set()
        rec_stack = set()
        
        def dfs(task_id):
            visited.add(task_id)
            rec_stack.add(task_id)
            
            for dep in self.dependencies.get(task_id, []):
                if dep not in visited:
                    if dfs(dep):
                        return True
                elif dep in rec_stack:
                    return True
            
            rec_stack.remove(task_id)
            return False
        
        for task_id in self.tasks:
            if task_id not in visited:
                if dfs(task_id):
                    return True
        
        return False
    
    async def execute(self) -> Dict[str, Any]:
        """
        执行所有任务
        
        TODO: 实现以下逻辑
        1. 检测循环依赖
        2. 找出无依赖的任务并发执行
        3. 任务完成后，找出新解锁的任务
        4. 重复直到所有任务完成
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        if self._detect_cycle():
            raise ValueError("检测到循环依赖！")
        
        completed = set()
        
        while len(completed) < len(self.tasks):
            ready_tasks = [
                task_id for task_id in self.tasks
                if task_id not in completed
                and all(dep in completed for dep in self.dependencies[task_id])
            ]
            
            if not ready_tasks:
                break
            
            async def run_task(task_id):
                deps_results = {dep: self.results[dep] for dep in self.dependencies[task_id]}
                if deps_results:
                    result = await self.tasks[task_id](**deps_results)
                else:
                    result = await self.tasks[task_id]()
                self.results[task_id] = result
                return task_id, result
            
            task_results = await asyncio.gather(*[run_task(t) for t in ready_tasks])
            for task_id, _ in task_results:
                completed.add(task_id)
        
        return self.results


async def test_task_graph():
    """测试任务依赖图"""
    print("\n" + "=" * 60)
    print("练习 4：异步任务依赖图")
    print("=" * 60)
    
    graph = AsyncTaskGraph()
    
    # 定义任务
    async def fetch_user():
        await asyncio.sleep(0.3)
        print("  完成: 获取用户信息")
        return {"user_id": 123, "name": "张三"}
    
    async def fetch_orders(user_data):
        await asyncio.sleep(0.4)
        print(f"  完成: 获取订单（用户: {user_data['name']}）")
        return ["order_1", "order_2"]
    
    async def fetch_products():
        await asyncio.sleep(0.2)
        print("  完成: 获取商品列表")
        return ["product_1", "product_2"]
    
    async def generate_report(orders, products):
        await asyncio.sleep(0.3)
        print("  完成: 生成报告")
        return {"report": "销售报告"}
    
    # 添加任务和依赖
    graph.add_task("fetch_user", fetch_user)
    graph.add_task("fetch_products", fetch_products)
    graph.add_task("fetch_orders", fetch_orders, depends_on=["fetch_user"])
    graph.add_task("generate_report", generate_report, depends_on=["fetch_orders", "fetch_products"])
    
    start = time.time()
    results = await graph.execute()
    elapsed = time.time() - start
    
    print(f"\n总耗时: {elapsed:.2f} 秒")
    print(f"任务结果: {results}")
    
    print("\n【验证点】")
    print(f"✓ fetch_user 和 fetch_products 并发执行")
    print(f"✓ fetch_orders 等待 fetch_user 完成后执行")
    print(f"✓ generate_report 等待所有依赖任务完成")


# ============================================================
# 练习 5：异步连接池
# ============================================================
"""
【问题描述】
数据库连接是昂贵资源，需要通过连接池管理。
实现一个异步连接池，限制并发连接数，支持连接复用。

【要求】
1. 实现连接的获取和释放
2. 连接数达到上限时等待
3. 连接用完后归还到池中
4. 支持连接健康检查（可选）

【预期行为】
- 并发请求数不超过连接池大小
- 连接被复用而非重复创建
- 所有等待的请求最终都能获得连接
"""

class AsyncConnectionPool:
    """异步连接池"""
    
    def __init__(self, max_connections: int = 3):
        """
        初始化
        
        Args:
            max_connections: 最大连接数
        """
        self.max_connections = max_connections
        self.available = asyncio.Queue()
        self.in_use = set()
        self.connection_count = 0
        self.lock = asyncio.Lock()
    
    async def _create_connection(self) -> Dict:
        """创建新连接"""
        async with self.lock:
            conn_id = self.connection_count
            self.connection_count += 1
        
        # 模拟连接创建
        await asyncio.sleep(0.1)
        print(f"  创建连接: conn_{conn_id}")
        return {"id": conn_id, "created_at": time.time()}
    
    async def acquire(self) -> Dict:
        """
        获取连接
        
        TODO: 实现以下逻辑
        1. 如果池中有可用连接，直接获取
        2. 如果池为空且未达上限，创建新连接
        3. 如果已达上限，等待连接释放
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        async with self.lock:
            if not self.available.empty():
                conn = await self.available.get()
                self.in_use.add(conn["id"])
                return conn
            
            if len(self.in_use) < self.max_connections:
                conn = await self._create_connection()
                self.in_use.add(conn["id"])
                return conn
        
        conn = await self.available.get()
        async with self.lock:
            self.in_use.add(conn["id"])
        return conn
    
    async def release(self, conn: Dict):
        """
        释放连接
        
        TODO: 实现连接归还逻辑
        """
        # TODO: 你的实现
        # 占位符实现 - 请替换为你的实际实现
        async with self.lock:
            if conn["id"] in self.in_use:
                self.in_use.remove(conn["id"])
        await self.available.put(conn)


async def test_connection_pool():
    """测试连接池"""
    print("\n" + "=" * 60)
    print("练习 5：异步连接池")
    print("=" * 60)
    
    pool = AsyncConnectionPool(max_connections=2)
    
    async def use_connection(request_id: int):
        print(f"  请求 {request_id} 等待连接...")
        conn = await pool.acquire()
        print(f"  请求 {request_id} 获得连接: conn_{conn['id']}")
        
        await asyncio.sleep(0.5)  # 模拟使用连接
        
        print(f"  请求 {request_id} 释放连接: conn_{conn['id']}")
        await pool.release(conn)
        return request_id
    
    start = time.time()
    results = await asyncio.gather(
        *[use_connection(i) for i in range(1, 5)]
    )
    elapsed = time.time() - start
    
    print(f"\n总耗时: {elapsed:.2f} 秒")
    print(f"处理请求数: {len(results)}")
    
    print("\n【验证点】")
    print(f"✓ 最大并发连接数为 2")
    print(f"✓ 4 个请求总耗时约 1 秒（2 批次 × 0.5 秒）")


# ============================================================
# 练习 6：异步熔断器
# ============================================================
"""
【问题描述】
在微服务架构中，当下游服务故障时，继续请求会浪费资源。
实现异步熔断器（Circuit Breaker），在错误率达到阈值时停止请求，
一段时间后尝试恢复。

【要求】
1. 实现三种状态：关闭、打开、半开
2. 错误率超阈值时熔断
3. 熔断后快速失败
4. 恢复时间后尝试半开状态

【预期行为】
- 正常状态（关闭）：请求正常执行
- 熔断状态（打开）：直接返回错误，不执行请求
- 半开状态：尝试少量请求，判断是否恢复
"""

class CircuitState:
    """熔断器状态"""
    CLOSED = "closed"      # 关闭（正常）
    OPEN = "open"          # 打开（熔断）
    HALF_OPEN = "half_open"  # 半开（尝试恢复）


class AsyncCircuitBreaker:
    """异步熔断器"""
    
    def __init__(self, failure_threshold: int = 3, recovery_time: float = 2.0):
        """
        初始化
        
        Args:
            failure_threshold: 失败次数阈值
            recovery_time: 恢复时间（秒）
        """
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None
        self.lock = asyncio.Lock()
    
    async def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        通过熔断器执行函数
        
        TODO: 实现以下逻辑
        1. 检查当前状态
        2. 如果是 OPEN 状态，检查是否到达恢复时间
        3. 如果是 OPEN 状态且未恢复，抛出异常
        4. 如果是 HALF_OPEN 或 CLOSED，尝试执行
        5. 执行成功/失败后更新状态
        """
        # TODO: 你的实现
        pass
    
    async def _on_success(self):
        """成功时更新状态"""
        async with self.lock:
            self.failure_count = 0
            self.state = CircuitState.CLOSED
    
    async def _on_failure(self):
        """失败时更新状态"""
        async with self.lock:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
                print(f"  熔断器打开！失败次数: {self.failure_count}")


async def test_circuit_breaker():
    """测试熔断器"""
    print("\n" + "=" * 60)
    print("练习 6：异步熔断器")
    print("=" * 60)
    
    breaker = AsyncCircuitBreaker(failure_threshold=3, recovery_time=2.0)
    
    # 模拟不稳定的服务
    call_count = 0
    
    async def unreliable_service():
        nonlocal call_count
        call_count += 1
        
        # 前 4 次失败，之后成功
        if call_count <= 4:
            raise Exception(f"服务故障 (调用 {call_count})")
        return f"成功 (调用 {call_count})"
    
    # 测试正常请求 -> 熔断 -> 恢复
    for i in range(1, 8):
        try:
            result = await breaker.call(unreliable_service)
            print(f"  请求 {i}: {result}")
        except Exception as e:
            print(f"  请求 {i}: {e}")
        
        await asyncio.sleep(0.3)
    
    print("\n【验证点】")
    print(f"✓ 前几次请求正常执行")
    print(f"✓ 失败达到阈值后熔断")
    print(f"✓ 熔断后快速失败（不执行实际请求）")


# ============================================================
# 运行所有练习
# ============================================================

async def main():
    """运行所有练习"""
    print("\n" + "=" * 60)
    print("Day 8: 异步编程练习题")
    print("=" * 60)
    print("\n说明：以下是练习框架，请完成 TODO 部分的实现")
    print("完成后运行验证预期行为")
    
    # 注意：以下是参考实现，实际练习时请先自己实现
    
    # 运行测试
    await test_batch_merger()
    await test_rate_limiter()
    await test_event_broadcaster()
    await test_task_graph()
    await test_connection_pool()
    await test_circuit_breaker()
    
    # 学习要点总结
    print("\n" + "=" * 60)
    print("学习要点总结")
    print("=" * 60)
    print("""
1. 批量请求合并器：减少 API 调用次数，降低延迟和成本
   - 应用场景：LLM API 批量调用、数据库批量写入

2. 异步限流器：控制请求速率，避免触发 API 限流
   - 关键：滑动窗口算法、等待队列

3. 事件广播器：实现发布-订阅模式，解耦系统组件
   - 应用场景：Agent 事件通知、日志收集

4. 任务依赖图：管理复杂工作流，自动调度执行
   - 关键：拓扑排序、并发执行、依赖解析

5. 连接池：管理昂贵资源，提高系统效率
   - 关键：资源限制、等待队列、连接复用

6. 熔断器：保护系统稳定性，快速失败
   - 三态：关闭、打开、半开
   - 应用场景：微服务调用、外部 API 集成

核心思想：
- 异步编程不仅是并发执行，更是设计模式的体现
- 生产环境需要考虑：限流、熔断、重试、超时
- 合理使用 asyncio 同步原语：Lock, Semaphore, Queue, Event
""")


if __name__ == "__main__":
    asyncio.run(main())