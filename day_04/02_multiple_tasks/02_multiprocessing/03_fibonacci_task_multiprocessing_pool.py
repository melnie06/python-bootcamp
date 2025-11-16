from multiprocessing import Pool
import cProfile

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    inputs = [35, 36, 37, 38]
    # outputs = [fib(number) for number in inputs]
    with Pool() as pool:
        outputs = (pool.fib(number) for number in inputs)


if __name__ == '__main__':
    cProfile.run("main()", sort="cumtime")
