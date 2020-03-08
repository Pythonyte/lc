from datetime import timedelta, datetime
import threading
import logging
from time import sleep
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-1s) %(message)s',
                    )

class RateLimiter:
    mapping = {}
    def __init__(self, thottling_period, rate_limit):
        """
        :param thottling: int time In seconds
        :param rate_limit: int count
        """
        self.thottling_period = thottling_period
        self.rate_limit = rate_limit
        self.sem = threading.Semaphore(1)

    def calculate_end_time(self, current_time):
        return current_time + timedelta(seconds=self.thottling_period)

    def __check_limit(self, unique_id, current_time, end_time):
        if unique_id not in self.mapping:
            self.mapping[unique_id] = {
                'count': 1,
                'end_time': end_time
            }
        elif current_time > self.mapping[unique_id]['end_time']:
            self.mapping[unique_id] = {
                'count': 1,
                'end_time': end_time
            }
        elif self.mapping[unique_id]['count'] < self.rate_limit:
            self.mapping[unique_id]['count'] += 1
        else:
            logging.info("Next request for UID=>{} has been throttled".format(unique_id))
            return False
        logging.info("UID=>{} Count=>{} EndTime=>{} RequestTime=>{}".format(
            unique_id,
            self.mapping[unique_id]['count'],
            str(self.mapping[unique_id]['end_time']),
            str(current_time)
        ))
        return True

    def check_limit(self, unique_id, current_time):
        end_time = self.calculate_end_time(current_time)
        # Critical Section Starts
        self.sem.acquire()
        self.__check_limit(unique_id, current_time, end_time)
        self.sem.release()
        # Critical Section Ends

# 5 req per 10 seconds by each userid
rl1 = RateLimiter(thottling_period=10, rate_limit=5)
rl2 = RateLimiter(thottling_period=10, rate_limit=5)
rl3 = RateLimiter(thottling_period=10, rate_limit=5)
for i in range(100):
    sleep(.2)
    objects = [rl1.check_limit, rl2.check_limit, rl3.check_limit]

    threading.Thread(
        target=objects[i%2],
        name="t{}".format(i),
        args=(i%5, datetime.now())
    ).start()
