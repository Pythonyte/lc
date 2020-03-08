# Thread Local Storage: Example Python Program


import threading, time


userName = threading.local()
# userName = None

def SessionThread(userName_in, timer):
    # Way 1
    # global userName
    # userName = userName_in
    # if timer:
    #     time.sleep(timer)
    # print(userName)

    # Way 2
    userName.val = userName_in
    if timer:
        time.sleep(timer)
    print(userName.val)


Session1 = threading.Thread(target=SessionThread, args=("User1",3))
Session2 = threading.Thread(target=SessionThread, args=("User2",0))

# start the session threads
Session1.start()
Session2.start()

# wait till the session threads are complete
Session1.join()
Session2.join()