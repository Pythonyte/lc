import threading
import logging
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-1s) %(message)s',
                    )

def myfunc2(t):
    logging.debug("Completing my task")
    logging.debug("Now, setting event for {}, to start its task".format(t.getName()))
    sleep(5)
    t.event.set()

def myfunc1():
    logging.debug("Completing my task")

class TimerClass(threading.Thread):
    def __init__(self, target=None, name=None, args=()):
        threading.Thread.__init__(self, target=target, name=name, args=args)
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
            logging.debug("Started but waiting for event to set !!")
            self.event.wait(10)
        else:
            logging.debug("Event is set Now !!")
            super().run()

thread1 = TimerClass(name="thread1", target=myfunc1)
thread1.start()

thread2 = TimerClass(target=myfunc2, name="thread2", args=(thread1,))
thread2.start()
thread2.event.set()