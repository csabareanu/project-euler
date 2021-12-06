# 10001st prime

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# A first aproach is to apply the sieve of erathostene (implemented in p0003) with a number big enough to generate at least 10001 prime numbers

import p0003 as p


def with_erathostene():
    primes = p.erathostene_sieve(10000009990005)
    prime = primes[10000]
    return prime

# Another aproach is to use the compute function in p0003 for each number in a sequence to see if a specific number is prime or not - seems much slower


def with_divisors(nr=10001):
    primes = [2]
    number = 3
    while True:
        divisors = p.compute(number)
        if(divisors == []):
            primes.append(number)
            if len(primes) == 10001:
                return number
        number += 2


if __name__ == "__main__":
    print(with_erathostene())  # 104743
    # print(with_divisors())  # 104743
