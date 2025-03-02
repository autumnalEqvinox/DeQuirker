import os
import requests
from bs4 import BeautifulSoup

DIRECTORY_NAME = "pages"


def download(n):
    if (os.path.isdir(DIRECTORY_NAME) == False):
        os.mkdir(DIRECTORY_NAME)
        print(f"Directory '{DIRECTORY_NAME}' created successfully.")
    for i in range(1, n+1):
        if os.path.isfile(f"pages\\{i}.html"):
            print(f"page {i} exists")
        else:
            print(f"downloading page {i}")
            with open(f"pages\\{i}.html", "w") as pagefile:
                pagefile.write(str(requests.get(f"https://www.deconreconstruction.com/vasterror/{i}").content))