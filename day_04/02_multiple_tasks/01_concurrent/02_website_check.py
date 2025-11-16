from concurrent.futures import ThreadPoolExecutor #added
import requests
import cProfile
import cProfile

import requests


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up!")
        else:
            print(f"{url} status {response.status_code}")
    except:
        print(f"{url} failed to reach.")

base_url = "https://raw.githubusercontent.com/"
file_name = "bensooter/URLchecker/master/top-1000-websites.txt"
response = requests.get(base_url + file_name)

websites = response.text.splitlines()
websites = ["https://" + site.strip() for site in websites if site.strip()]
websites = websites[:100]


def main():
    for website in websites:
        check_website(website)
        
    # with ThreadPoolExecutor() as pool:
    #     outputs = pool.map(check_website, websites)


if __name__ == '__main__':
    cProfile.run("main()", sort="cumtime")
