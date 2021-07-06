def input_two_numbers():
    print("Enter two numbers: ")
    l = input().split()
    a, b = int(l[0]), int(l[1])
    return a, b


def add(a, b):
    return a+b


def output(l, m, sum):
    print(f'{l} + {m} = {sum}')


def main():
    a, b = input_two_numbers()
    sum=add(a,b)
    output(a,b,sum)


main()