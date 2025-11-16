import cProfile


def main():
    for _ in range(1_000_000):
        x = 10 ** 1000


if __name__ == '__main__':
    cProfile.run("main()")
