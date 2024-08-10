import time


def decorat(func):
    def wrapper():
        print("decoration begins")
        func()
        print("decoration ends")

    return wrapper


def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start")
        func()
        duration = time.time() - start_time
        print(f'duration: {duration}')

    return wrapper


def double_decorator(func):
    def wrapper():
        func()
        func()

    return wrapper


@double_decorator
@decorat
@duration_decorator
def func():
    print("Hello")
    time.sleep(1)


func()
