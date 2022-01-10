# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def compute(n):
    largest_number = 3 * int(n * '3')
    smallest_number = 10 ** (n-1)
    the_largest_palindrome = 0
    the_largest_product = []
    for a in range(largest_number, smallest_number - 1, -1):
        # if the maximum value that b can take multiplied by the current value of a is smaller than the largest_palindrome, there is no need to check further
        if a*largest_number < the_largest_palindrome:
            break
        for b in range(largest_number, smallest_number - 1, -1):
            # if a*b is smaller than the largest_palindrom_found all other values in this loop will also be smaller
            if(a*b < the_largest_palindrome):
                break
            if is_palindrome(a*b):
                if the_largest_palindrome < a * b:
                    the_largest_palindrome = a * b
                    the_largest_product = [a, b]
                    # all other pottential palindroms will be smaller
                    break
    return (the_largest_product, the_largest_palindrome)


def is_palindrome(n):
    digits = str(n)

    for index, digit in enumerate(digits):
        # if the len of the number is odd, the digit in the middle of the number it's not important. (len(digits) - 1) is the maximum index.
        if index >= (len(digits) - 1) / 2:
            return True
        if digit != digits[-(index+1)]:
            return False


if __name__ == "__main__":

    # ([993, 913], 906609) - the first element is the numbers that forms the product
    print(compute(6))
