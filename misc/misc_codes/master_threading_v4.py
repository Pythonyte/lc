import concurrent.futures
import math
from time import sleep

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
]

def is_prime(n):
    if n % 2 == 0:
        return False
    sleep(4)
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        executors = executor.map(is_prime, [True,False])
        # for number, prime in zip(PRIMES, executors):
        #     print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    # print_number(is_even=True)
    main()