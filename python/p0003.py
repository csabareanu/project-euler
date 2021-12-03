import math
# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# By the fundamental theorem of arithmetic, every integer n > 1 has a unique factorization as a product of prime numbers.
# In other words, the theorem says that n = p_0 * p_1 * ... * p_{m-1}, where each p_i > 1 is prime but not necessarily unique.
# Now if we take the number n and repeatedly divide out its smallest factor (which must also be prime), then the last
# factor that we divide out must be the largest prime factor of n. For reference, 600851475143 = 71 * 839 * 1471 * 6857.


# I've implemented here, just for curiosity purposes, the erathostene sieve, a method to determine the prime numbers until a specific number
def erathostene_sieve(nr):
    max_divisor = math.ceil(math.sqrt(nr))
    sieve = [True] * max_divisor
    upper = math.ceil(math.sqrt(max_divisor))

    for x in range(2, upper):
        if sieve[x] == True:
            for y in range(x ** 2, max_divisor, x):
                sieve[y] = False

    return [ind for ind, value in enumerate(sieve) if value == True]


def compute(nr):
    assert nr >= 2
    prods = []
    for x in range(2, math.ceil(nr/2) + 1):
        # if all the divisors are computed break
        if nr == 1:
            break
        # in case it has same divisors - ex. 8 - 2*2*2
        while nr % x == 0:
            prods.append(x)
            nr = nr / x
    # if the number is prime it will return an empty array since it has no prime divisors
    return prods


if __name__ == "__main__":
    # The function returns all the prime divisors of the specified number. The last element from the array is the biggest prime divisor
    print(compute(600851475143))  # 6857
