https://www.geeksforgeeks.org/number-of-ways-to-calculate-a-target-number-using-only-array-elements/

def findTotalWays(arr, i, k, comb):
    if (i >= len(arr) and k != 0):
        return 0

    # If target is reached, return 1
    if (k == 0):
        print(comb)
        return 1

    return (findTotalWays(arr, i + 1, k, comb) +
            findTotalWays(arr, i + 1, k - arr[i], comb + [arr[i]]))

arr = [-3, 1, 3, 5]
k = 6
print(findTotalWays(arr, 0, k, []))
