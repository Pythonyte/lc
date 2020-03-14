import threading
import logging
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-1s) %(message)s',
                    )

sem = threading.Semaphore(1)
counter = 0

def helper():
    sem.acquire()
    # Critical Section Starts
    global counter
    logging.debug("Critical section starts - counter {}".format(counter))
    logging.debug("Semaphore counter {}:".format(sem._value))
    counter += 1
    sleep(4)
    # Critical Section Ends
    sem.release()
    logging.debug("Critical section ends - counter {}".format(counter))

n = 4
for i in range(n):
    threading.Thread(target=helper, name="t{}".format(i)).start()
