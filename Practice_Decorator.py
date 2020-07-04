import time


class MyTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, args):
        time.perf_counter()
        result = self.func(args)
        e = time.perf_counter()
        print(f'{e}')
        return result


class MyCache:
    def __init__(self, func):
        self.func = func
        self.cache = dict()

    def __call__(self, args):
        if args not in self.cache:
            self.cache[args] = self.func(args)               

        return self.cache[args]


@MyCache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


@MyTime
def run_fib(n):
    return fib(n)


if __name__ == "__main__":
    print(run_fib(33))
