"""
ThreadPoolExecutor
    An abstract class that provides methods to execute calls asynchronously. It should not be used directly, but through its concrete subclasses.

    - Submit
        Schedules the callable, fn, to be executed as fn(*args **kwargs) and returns a Future object representing the execution of the callable.
    - map
        Equivalent to map(func, *iterables) except func is executed asynchronously and several calls to func may be made concurrently.
    * Future Object
        Encapsulates the asynchronous execution of a callable. Future instances are created by Executor.submit() and should not be created directly except for testing.
        provides options to look around in threads like
        Done
        result
        cancel
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def test_method(x, secs):
    print("Method {} version {} starts in {} secs".format(test_method.__name__, x, secs))
    time.sleep(secs)
    print("Method {} version {} ends".format(test_method.__name__, x, secs))
    return "M-{}:Secs-{}".format(test_method.__name__, secs)

def test_method_2(secs):
    print("Start:-{}".format(secs))
    time.sleep(secs)
    print("Done Sleepin {}".format(secs))
    return "Done:-{}".format(secs)

def approach_1():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(test_method, 1,3)
        future2 = executor.submit(test_method, 2,3)
        future1.result()
        print("I will be print after future1 completion, result is waiting for it")
        future2.result()

def approach_2():
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(test_method, i,3) for i in range(10)]

def approach_3():
    with ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(test_method, i, sec) for i, sec in enumerate(secs)]

        # result should be printed as soon as thread is getting completed
        for f in as_completed(results):
            print(f.result())

def approach_4():
    with ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(test_method_2, secs)

        # result should be printed as soon as thread is getting completed
        for f in results:
            print(f)

if __name__ == '__main__':
    start = time.perf_counter()

    # approach_1()
    # approach_2()
    # approach_3()
    approach_4()

    end = time.perf_counter()
    print("Program ends in {} secs".format(end-start))