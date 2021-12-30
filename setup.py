import requests
from bs4 import BeautifulSoup
# import beautifulsoup4

def parse(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def write():
    with open("results.txt", "w") as text_file:
        text_file.write(soup.prettify())