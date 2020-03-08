import threading, time


def test_method(x):
    print("Method {} version {} starts".format(test_method.__name__, x))
    time.sleep(4)
    print("Method {} version {} ends".format(test_method.__name__, x))

def approach_1():
    t1 = threading.Thread(target=test_method, args=(1,))
    t2 = threading.Thread(target=test_method, args=(2,))

    # to start the threads
    t1.start()
    t2.start()

    # if you want program to wait for complition of all threads before exiting
    t1.join()
    t2.join()

def approach_2(n):
    threads = []
    for i in range(n):
        t = threading.Thread(target=test_method, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == '__main__':
    start = time.perf_counter()

    # approach_1()
    # approach_2(5)

    end = time.perf_counter()
    print("Program ends in {} secs".format(end-start))