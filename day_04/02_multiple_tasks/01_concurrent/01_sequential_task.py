import cProfile

import requests


def fetch_url(url):
    return requests.get(url).status_code


def main():
    inputs = [f'https://httpbin.org/delay/{wait}' for wait in range(1, 5)]
    outputs = [fetch_url(url) for url in inputs]


if __name__ == '__main__':
    cProfile.run("main()", sort="cumtime")
