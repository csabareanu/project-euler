# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1 ^ 2 + 2 ^ 2 + ... + 10 ^ 2 = 385

# The square of the sum of the first ten natural numbers is,
# (1+2+...+10) ^ 2 = 55 ^ 2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025-385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math


def compute(nr):
    return square_sum(nr) - sum_squares(nr)


def sum_squares(nr):
    return sum([x ** 2 for x in range(1, nr + 1)])


def square_sum(nr):
    return (nr * (nr + 1) / 2) ** 2


if __name__ == "__main__":

    print(compute(100))
