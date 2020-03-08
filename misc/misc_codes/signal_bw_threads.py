import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def task(event, timeout):
    logging.debug("Started thread but waiting for event...")
    # make the thread wait for event with timeout set
    event_set = event.wait(timeout)
    if event_set:
        logging.debug("Event received, releasing thread...")
    else:
        logging.debug("Time out, moving ahead without event...")

def even(e1,e2):
    for i in range(0,10,2):
        print(i)
        e1.wait()
        time.sleep(1)
        e2.set()


def odd(e1,e2):
    for i in range(1,10,2):
        print(i)
        e1.set()
        time.sleep(1)
        e2.wait()

if __name__ == '__main__':
    e1 = threading.Event()
    e2 = threading.Event()
    t1 = threading.Thread(name='t1',
                          target=even,
                          args=(e1,e2))
    t1.start()

    t2 = threading.Thread(name='t2',
                          target=odd,
                          args=(e1,e2,))
    t2.start()