from setup import *
import json
import requests
from bs4 import BeautifulSoup

# Get all posts with their titles
def combine(soup):

    listofLinks = []
    allFrontPage = soup.find_all("h2", {"class": "post-title"})

    for x in allFrontPage:
        listofLinks.append(str(x))
    return listofLinks

# Adjust the whole string so that it takes only the title and link
def clean(listofLinks):
    linkDict = {}
    # make it so its just links and titles
    for x in listofLinks:
        current = listofLinks[listofLinks.index(x)]
        current = current[33:]
        size = len(current)
        current = current[:size-10]
        current = current.replace('">', '^') 
        # print("X: " + current)
        current = current.split('^')
        # Save It:
        linkDict[current[1]] = current[0]
    # Remove Duplicates by making a new list for only
    # entries with unique
    tmp = {value : keyVal for keyVal, value in linkDict.items()}
    # next check if its already added
    new = {value : keyVal for keyVal, value in tmp.items()}
    return new

# using the json library it outputs nicely for viewing
def give(dictionary):
    return json.dumps(dictionary, indent=1)