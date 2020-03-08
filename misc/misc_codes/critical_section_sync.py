import threading
import logging
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-1s) %(message)s',
                    )
n = 6
sem = threading.Semaphore(2)
counter = 0
def helper():
    sem.acquire()
    # Critical Section Starts
    global counter
    counter += 1
    sleep(1)
    logging.info("{}".format(counter))
    # Critical Section Ends
    sem.release()

for i in range(n):
    threading.Thread(target=helper, name="t{}".format(i)).start()
