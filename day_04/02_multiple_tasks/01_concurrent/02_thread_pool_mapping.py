import cProfile
from concurrent.futures import ThreadPoolExecutor

import requests


def fetch_url(url):
    return requests.get(url).status_code


def main():
    inputs = [f'https://httpbin.org/delay/{wait}' for wait in range(1, 5)]

    with ThreadPoolExecutor() as pool:
        outputs = pool.map(fetch_url, inputs)


if __name__ == '__main__':
    cProfile.run("main()", sort="cumtime")
