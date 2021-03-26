arr = [['a', 2, 3],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 4, 25],
       ['e', 3, 15]]
# Following is maximum profit sequence of jobs
# c a e
# We have total 3 hours and each job take 1 hr to complete.
from pprint import pprint
def max_profit_sequence_of_jobs(arr):
    arr = sorted(arr, key=lambda x:x[2], reverse=True)
    max_time = max([x[1] for x in arr])
    seq_array = [None]*max_time
    for job_detail in arr:
        job, waiting_time, profit = job_detail
        while waiting_time:
            if not seq_array[waiting_time-1]:
                seq_array[waiting_time - 1] = job
                waiting_time = False
            else:
                waiting_time -= 1

    pprint(seq_array)

max_profit_sequence_of_jobs(arr)