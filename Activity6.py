import math


def read():
    nums = input("Enter a few numbers").split()
    ints = [int(n) for n in nums]
    return ints


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


def get_sum(numbers):
    total = 0
    for i in numbers:
        if is_prime(i):
            total += i
    return total


def output(total_value):
    print(f"Sum of all prime numbers = {total_value}")


def main():
    nums = read()
    sump = get_sum(nums)
    output(sump)


main()