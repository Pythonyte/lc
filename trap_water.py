

def find_trapped_water_nsqr(arr):
    res = 0
    n = len(arr)
    for i in range(1, n-1):
        # max left before i
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # max right after i
        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])

        print("Index {}, Value {} ==Water {}".format(i, arr[i],min(left,right) - arr[i]))
        res = res + min(left,right) - arr[i]
    print("==>",res)
    return res

def find_trapped_water_n(arr):
    res = 0
    n = len(arr)
    left, right = [0]*n, [0]*n

    left[0] = arr[0]
    for i in range(1,n):
        left[i] = max(left[i-1], arr[i])

    right[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    print("LEFT MAX=> {}".format(left))
    print("RIGHT MAX=> {}".format(right))

    for i in range(n):
        res = res + min(left[i], right[i]) - arr[i]
    print("++",res)
    return res

find_trapped_water_n([3, 0, 2, 0, 4])
find_trapped_water_nsqr([3, 0, 2, 0, 4])
# find_trapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
find_trapped_water_n([6,5,4,3,2,1])
find_trapped_water_nsqr([6,5,4,3,2,1])