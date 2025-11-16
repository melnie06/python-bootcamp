import cProfile
from multiprocessing import Pool


def process(number):
    for _ in range(1_000_000):
        x = 10 ** 1000


def main():
    inputs = [1, 2, 3]
    with Pool() as pool:
        pool.map(process, inputs)
        outputs = pool.map(process, inputs)#


if __name__ == '__main__':
    cProfile.run("main()", sort="cumtime")
