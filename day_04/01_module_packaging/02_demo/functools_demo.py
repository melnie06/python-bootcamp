import cProfile
from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    print(fib(38))


if __name__ == '__main__':
    cProfile.run("main()")
