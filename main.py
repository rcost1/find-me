from gather import *
import json
import requests
from bs4 import BeautifulSoup

def userLink():
    site = input("Give me a link: ")
    if "tech" not in site:
        print("Try: https://techncruncher.blogspot.com/")
        pass
    return site


def putTogether():
    parsedLink = parse(userLink())
    combined = combine(parsedLink)
    cleaned = clean(combined)
    return give(cleaned)

putTogether()