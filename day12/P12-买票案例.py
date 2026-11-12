import threading
import time


def sale_ticket():
    global ticket_num
    while True:
        lock.acquire()
        if ticket_num <= 0:
            lock.release()
            break
        ticket_num -= 1
        print(f"当前{threading.current_thread().name}卖了一张票，还剩{ticket_num}张")
        lock.release()
        time.sleep(0.01)

if __name__ == '__main__':
    ticket_num = 30
    # 创建线程对象
    lock = threading.Lock()
    threads = [threading.Thread(target=sale_ticket,name="窗口" + str(i)) for i in range(1,4)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    print(f"当前线程{threading.current_thread().name}",ticket_num)