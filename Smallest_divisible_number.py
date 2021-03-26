# Recursive function to return hcf of a and b
def hcf(a, b):
    # When b is zero, a would be hcf
    if (b == 0):
        return a
    return hcf(b, a % b)

def lcm(a, b):
    """
    As per math formula
    lcm(a,b) = (a * b)/ gcd(a,b)
    :param a:
    :param b:
    :return:
    """
    return a*b // hcf(a,b)

def smallest_divisible_no(n):
    """
    Smallest divisible of numbers 1 to n will be lcm of 1 to n
    """
    ans = 1
    for i in range(1, n + 1):
        ans = lcm(ans, i)
    return ans

for i in range(15):
    print("Smallest divisible for numbers till {} : {}".format(i, smallest_divisible_no(i)))

"""
Output:

Smallest divisible for numbers till 0 : 1
Smallest divisible for numbers till 1 : 1
Smallest divisible for numbers till 2 : 2
Smallest divisible for numbers till 3 : 6
Smallest divisible for numbers till 4 : 12
Smallest divisible for numbers till 5 : 60
Smallest divisible for numbers till 6 : 60
Smallest divisible for numbers till 7 : 420
Smallest divisible for numbers till 8 : 840
Smallest divisible for numbers till 9 : 2520
Smallest divisible for numbers till 10 : 2520
Smallest divisible for numbers till 11 : 27720
Smallest divisible for numbers till 12 : 27720
Smallest divisible for numbers till 13 : 360360
Smallest divisible for numbers till 14 : 360360
"""