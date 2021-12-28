import requests
from bs4 import BeautifulSoup
# import beautifulsoup4

r = requests.get('https://techncruncher.blogspot.com/')

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

## TechCrunch

listofLinks = []

def write():
    with open("results.txt", "w") as text_file:
        text_file.write(soup.prettify())

# Get all posts with their titles

def combine():
    allFrontPage = soup.find_all("h2", {"class": "post-title"})

    for x in allFrontPage:
        listofLinks.append(str(x))

# Adjust the whole string so that it takes only the title and link

def clean():
    # make it so its just links and titles
    for x in listofLinks:
        current = listofLinks[listofLinks.index(x)]
        current = current[33:]
        size = len(current)
        current = current[:size-10]
        current = current.replace('">', ' ') 
        #print("X: " + current)
        # Save It:
        listofLinks[listofLinks.index(x)] = current
    # Give me back the list

    return listofLinks

def give():
    print(listofLinks)

combine()
print("-----------------------------------------------")
clean()
print("-----------------------------------------------")
give()

    
#print(*listofLinks, sep = "\n")





