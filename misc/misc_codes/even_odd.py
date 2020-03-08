import threading, logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-1s) %(message)s',
                    )

thread_list = []

state = True

def numbers(start, end, jump):
    for i in range(start, end, jump):
        yield i

def create_threads(n):
    for i in range(n):
        t = Consumer(target=numbers, name="t_{}".format(i), args=(i,10,3))
        thread_list.append(t)

def start_threads():
    for t in thread_list:
        t.start()
    thread_list[0].event.set()

class Consumer(threading.Thread):
    def __init__(self, target=None, name=None, args=()):
        self.target = target
        self.args=args
        self.event = threading.Event()
        threading.Thread.__init__(self, target=target, name=name, args=args)

    def run(self):
        global state
        nums_gen = self.target(*self.args)
        index = (self.args[0] + 1) % 3
        next_thread = thread_list[index]
        while True:

            try:
                if not state: break
                if self.event.is_set() and state:
                    logging.debug(next(nums_gen))
                    self.event.clear()
                    next_thread.event.set()
            except StopIteration as e:
                state = False
                break
        self.event.clear()

if __name__ == '__main__':
    create_threads(3)
    start_threads()