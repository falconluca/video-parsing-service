import gevent
from gevent import monkey
import time

# 使用 monkey patch 使标准库的 I/O 操作变为非阻塞
monkey.patch_all()


# 线程是协程的容器：一个线程中可以运行多个协程，但这些协程之间不会并行，而是并发。
#
# 协程的执行权是显式让出的：协程通过 yield 或类似操作（如 gevent.sleep()）让出执行权。
# 让出执行权意味着当前协程暂停执行，允许同一个线程内的其他协程运行。
if __name__ == "__main__":

    def task(name, delay):
        print(f"Task {name} starts")
        time.sleep(delay)  # 实际上是非阻塞的 gevent.sleep
        print(f"Task {name} ends")

    # 启动两个协程
    g1 = gevent.spawn(task, "1", 3)
    g2 = gevent.spawn(task, "2", 1)

    gevent.joinall([g1, g2])
