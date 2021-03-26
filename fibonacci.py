def fib(n):
    print('call', n)
    if n<=1:return n
    return fib(n-1) + fib(n-2)

fibonacci_cache = {}
def fibonacci_memo(input_value):
    if input_value in fibonacci_cache:
        return fibonacci_cache[input_value]
    print('call', input_value)
    if input_value == 1:
            value = 1
    elif input_value == 2:
            value = 1
    elif input_value > 2:
            value =  fibonacci_memo(input_value -1) + fibonacci_memo(input_value -2)
    fibonacci_cache[input_value] = value
    return value


# 0 1 1 2 3 5 8 13

def fib_iteration(n):
    if n<=1: return n
    prev_prev, prev = 0, 1
    curr = None
    for i in range(2, n+1):

        curr = prev + prev_prev
        print(i,curr)
        prev_prev = prev
        prev = curr
    return curr

print(fib_iteration(7))



def maxsubarraysum(array, size):
    max_so_far = array[0]
    curr_sum = array[0]
    for i in range(1, size):
        curr_sum = max(array[i], curr_sum+array[i])
        max_so_far = max(max_so_far, curr_sum)
    return max_so_far


