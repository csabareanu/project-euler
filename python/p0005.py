# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import p0003 as p
import math

# brute force - very slow for large numbers


def compute(n):
    assert n > 2
    current_number = n
    while True:
        for nr in range(2, n + 1):
            if current_number % nr != 0:
                # step must be multiple of n
                current_number += n
                break
            if nr == n:
                return current_number

# 4 - 2*2*3=12
# 5 - 2*2*3*5 = 60
# 6 - 2*2*3*5 = 60
# 7 - 2*2*3*5*7 = 60*7 = 420
# 8 - 420 * 2 = 840
# 9 - 840*3 = 2520
# 10 - 2520

# Must iterate the first n numbers and determine the minimum list of divisors so each number in the list can be composed


def compute_better(n):  # and faster
    divisors = {}
    # will populate a dictionary with key being the current number and value beeing a list of divisors
    for nr in range(2, n+1):
        divisors[nr] = p.compute(nr)

    # this part will generate the minimum list of divisors such as every number from 1 to n can be composed
    min_divs = []
    for key, values in divisors.items():
        # this means that the number is prime and if not in the min_divs list it should be appended
        if values == []:
            if key not in min_divs:
                min_divs.append(key)
        else:
            for value in values:
                times_in_values = values.count(value)
                times_in_divs = min_divs.count(value)
                if times_in_values > times_in_divs:
                    min_divs.extend([value] * (times_in_values-times_in_divs))

    return math.prod(min_divs)


if __name__ == "__main__":

    print(compute_better(20))  # 232792560
