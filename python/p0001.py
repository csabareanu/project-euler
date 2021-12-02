# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def compute(nr):
    return sum(x for x in range(nr) if (x % 3 == 0 or x % 5 == 0))

# better
# Sum of first n numbers = n(n+1)/2
# 3+6+9+12+15+...+996+999 = 3*(1+2+3+...+333) = 3*333*(333+1)/2


def sum_divisible_by(nr, target):
    p = target // nr
    return int(nr * p * (p + 1) / 2)


if __name__ == "__main__":
    print(compute(1000))
    # must subtract numbers divisible with 15 because those numbers are added twice
    print(sum_divisible_by(5, 1000) +
          sum_divisible_by(3, 1000) - sum_divisible_by(15, 1000))
