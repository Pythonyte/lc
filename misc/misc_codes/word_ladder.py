def find_min_max(arr):
    emin, emax = float("inf"), float("-inf")
    for item in arr:
        emin = min(emin, item)
        emax = max(emax, item)
    return emin, emax

def find_max_smax(arr):
    if not arr: return -1, -1
    if len(arr) == 1: return arr[0], arr[0]
    fmax = max(arr[0], arr[1])
    smax = min(arr[0], arr[1])
    for i in range(2,len(arr)):
        item = arr[i]
        if item > smax and item > fmax:
            smax = fmax
            fmax = item
        elif fmax > item > smax:
            smax = item
    return fmax, smax


def maxLen(arr, target):
    hash_map = {}
    max_len = 0
    curr_sum = 0

    # Traverse through the given array
    for i in range(len(arr)):
        curr_sum += arr[i]

        # Case print(maxLen([0,0]))
        if arr[i] is target and max_len is 0:
            max_len = 1

        # Case print(maxLen([1,-1,0]))
        if curr_sum is target:
            max_len = i + 1

        # Normal Case
        if curr_sum - target in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum - target])
        else:
            hash_map[curr_sum] = i
    return max_len

print(maxLen([9,8,-8,9,-9,5], 9))
print(maxLen([1,-1,0], 0))
print(maxLen([9,9,-9], 9))