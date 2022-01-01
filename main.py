from gather import *
import json
import requests
import mysql.connector
from bs4 import BeautifulSoup
def userLink():
    site = input("Give me a link (or ESC): ")
    if "tech" not in site:
        print("Try: https://techncruncher.blogspot.com/")
        userLink()
    return site


def putTogether():
    # Parse the link
    parsedLink = parse(userLink())
    # get all the neccessary content
    combined = combine(parsedLink)
    # scrub off the excess text
    cleaned = clean(combined)
    #return it all together
    return give(cleaned)

def putTogetherDict():
    # Parse the link
    parsedLink = parse(userLink())
    # get all the neccessary content
    combined = combine(parsedLink)
    # scrub off the excess text
    cleaned = clean(combined)
    #return it all together
    print(type(cleaned))
    return cleaned

def write():
    results = putTogether()
    #print(results)
    with open("results.txt", "w") as text_file:
        text_file.write(results)

def store():
    passW = input("password")

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=passW,
    database="findmeproject"
    )

    mycursor = mydb.cursor()

    listofLinks = putTogetherDict()

    for key,value in listofLinks.items():
        sql = "INSERT INTO sites (LINK, headline) VALUES (%s, %s)"
        val = (key, value)
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")        
    mydb.commit()
    

#write()        
store()
putTogether()