def test_function():
    print("Hello")


def better_calc(num1, num2, operation):
    result = 0
    if operation == 'plus':
        result = num1 + num2
    if operation == 'minus':
        result = num1 - num2

    print(f"The result of {num1} + {num2} is {result}")


better_calc(1, 2, "minus")


def print_all(*arguments):
    for arg in arguments:
        print(arg)


def print_even_more(*args, **kwargs):
    print(args)
    print(kwargs)


def calc_sum(*args):
    print(sum(args))


calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print_all(1, 2, 3, 4)
print_even_more(1, 2, 3, 54, 21, 3412, 31, 'hello', test=1, test2=5)
