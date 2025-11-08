import cProfile

def process(number):
    for _ in range(1_000_000):
        x = 10 ** 1000


def main():
    inputs = [1, 2, 3]
    outputs = [process(number) for number in inputs]


if __name__ == '__main__':
    cProfile.run("main()", sort="cumtime")
