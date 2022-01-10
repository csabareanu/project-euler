# Special Pythagorean triplet

# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def compute(sum):
    a = 2
    b = 2
    c = 2


# with brute force, generate a list of pythagorean triplets with c <= nr, optional in the problem


def pythagorean_triplets(nr):
    # a < b < c
    a = 1
    b = 2
    c = 3
    list = []
    while c <= nr:
        # if b will become bigger than c in the next iteration we will restart the process with an increment of c
        if b + 1 == c:
            c += 1
            a = 1
            b = 2
            continue
        b += 1
        # will increment a until a has the same value than b
        while a < b:
            if is_pythagorean_triplet(a, b, c):
                list.append([a, b, c])
            a += 1
        a = 1
    return list


def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


# function to generate a list of numbers [a,b,c] s.a. a < b < c with the property that a + b + c = nr
def generate_numbers(sum):
    nr = sum // 3
    if sum % 3 == 0:
        return [nr - 1, nr, nr + 1]
    elif sum % 3 == 1:
        return [nr - 2, nr + 1, nr + 2]
    elif sum % 3 == 2:
        return [nr - 1, nr + 1, nr + 2]


def compute(triplets_sum):
    a, b, c = generate_numbers(triplets_sum)


if __name__ == "__main__":
    print(compute(1000))
