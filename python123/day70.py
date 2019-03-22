""" 我设计的程序是这样运作的：

1. N个子程序反复占用并释放共有的内存资源

2. 主线程在等死锁出现

3. 一旦死锁出现，主线程就会释放所有会导致各个线程出现RuntimeError错误的锁定。

注：任何线程都可以释放先前出现的锁定，因为这里的锁定是无法再次进入的。但是尝试释放一个不在占用状态的锁定，就会导致RuntimeError。

测试时间到 ！ 现在我问你们 ， 如果你们不去运行这个程序 ， 你们能发现哪里会有bug吗 ？ 此处bug指程序运行中一切偏离上述三条要求的行为 。
 """
class SharedState:
    def __init__(self, n):
        self._lock = Lock()
        self._state = defaultdict(int)
        self._resources = [Lock() for _ in range(n)]

    def atomic(self, key, value=0):
        with self._lock:
            self._state[key] += value
            return self._state[key]

    def resource(self, i):
        return self._resources[i]

    def kill(self):
        resources = self._resources
        self._resources = None
        for i in resources:
            i.release()


def worker(pid, state):
    try:
        while True:
            state.atomic('waiting', 1)
            with state.resource(pid):
                state.atomic('waiting', 1)
                with state.resource(pid - 1):
                    state.atomic('waiting', -2)
                    state.atomic('tasks', 1)
    except RuntimeError:
        pass


def deadlock(n):
    state = SharedState(n)
    for i in range(n):
        Thread(target=worker, args=(i, state)).start()
    while state.atomic('waiting') < 2 * n:
        sleep(1)
    print(n, 'workers; deadlock after',
          state.atomic('tasks'), 'tasks')
    state.kill()


for i in range(1, 10):
    deadlock(10 * i)
