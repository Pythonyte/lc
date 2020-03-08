import threading, time, random
sem = threading.Semaphore

from threading import local
# Python create mutex
my_mutex = threading.Lock()
class thread_one(threading.Thread):
	def run(self):
		# Python mutex global
		global my_mutex
		print ("The first thread is now sleeping")
		time.sleep(random.randint(1, 5))
		print("First thread is finished")
		# Python release mutex: once the first thread
		# is done, we release the lock
		my_mutex.release()

class thread_two(threading.Thread):
	def run(self):
		# Python mutex global
		global my_mutex
		print ("The second thread is now sleeping")
		time.sleep(random.randint(1, 5))
		# Python mutex acquire: second thread has to
		# to keep waiting until the lock is released
		my_mutex.acquire()
		print("Second thread is finished")

# Python mutex acquire: main thread is acquiring the lock 
my_mutex.acquire()
t1 = thread_one()
t2 = thread_two()
t1.start()
t2.start()