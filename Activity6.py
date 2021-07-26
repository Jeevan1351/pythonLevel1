import math


def read():
    nums = input("Enter a few numbers").split()
    ints = [int(n) for n in nums]
    return ints


def is_prime(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return 0
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return 0
        return n


def get_sum(numbers):
    total = [is_prime(i) for i in numbers]
    return sum(total)


def output(total_value):
    print(f"Sum of all prime numbers = {total_value}")


def main():
    nums = read()
    sump = get_sum(nums)
    output(sump)


main()
