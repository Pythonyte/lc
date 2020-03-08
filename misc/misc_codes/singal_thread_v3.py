import threading, logging
# represents the addition of an item to a resource
import time

condition = threading.Condition()
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-1s) %(message)s',
                    )
state = False

class Producer(threading.Thread):
    def __init__(self, target=None, name=None, args=()):
        threading.Thread.__init__(self, target=target, name=name, args=args)

    def run(self):
        global state
        with condition:
            logging.debug("Doing work")
            state = True

            logging.debug("work done. notifying all other waiting threads")
            time.sleep(2)
            condition.notifyAll()  # signal that a new item is available


class Consumer(threading.Thread):
    def __init__(self, target=None, name=None, args=()):
        threading.Thread.__init__(self, target=target, name=name, args=args)
    def run(self):
        with condition:
            logging.debug("got condition")
            while True:
                time.sleep(1)
                if state:
                    logging.debug("state is {}".format(state))
                    break
                logging.debug("waiting for condition")
                condition.wait()  # sleep until item becomes available


p = Producer()
for _ in range(5):
    c = Consumer()
    c.start()
p.start()
