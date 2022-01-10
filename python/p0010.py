# Summation of primes

# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import p0003 as p


def compute(nr):
    return sum(p.erathostene_sieve(nr))


if __name__ == "__main__":
    print(compute(2000000))
