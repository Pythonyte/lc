# import random
# import threading
# import time
# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )
#
#
# class CustomThread(threading.Thread):
#     def __init__(self, group=None, target=None, name=None,
#                  args=(), kwargs=None, *, daemon=None):
#         super().__init__(
#             group=group,
#             target=target,
#             name=name,
#             args=args,
#             kwargs=kwargs,
#             daemon=daemon
#         )
#         self.args = args
#         self.kwargs = kwargs
#         return
#
#     def run(self):
#         logging.debug("Starting run {}".format(self.__dict__))
#         super().run()
#         logging.debug("Ending run {}".format(self.__dict__))
#
#
# def worker():
#     """thread worker function"""
#     pause = random.randint(1,5)
#     logging.debug('sleeping %s target', pause)
#     time.sleep(pause)
#     logging.debug('ending target')
#     return
#
# for i in range(3):
#     t = CustomThread(target=worker, name="t{}".format(i))
#     t.setDaemon(True)
#     t.start()
#
# # # main_thread = threading.currentThread()
# # for t in threading.enumerate():
# #     # if t is main_thread:
# #     #     continue
# #     logging.debug('joining %s', t.getName())
# #     # t.join()
#
# # deadlock
# # main_thread = threading.currentThread()
# # logging.debug(main_thread.getName())
# # main_thread.join()











import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def delayed():
    logging.debug('worker running')
    return

t1 = threading.Timer(3, delayed)
t1.setName('t1')
t2 = threading.Timer(3, delayed)
t2.setName('t2')

logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('canceling %s', t2.getName())
t2.cancel()
logging.debug('done')
logging.debug("GO TO SLEEP")
time.sleep(6)
logging.debug("END SLEEP")
logging.debug(t1.is_alive())
t1.cancel()
logging.debug("END")