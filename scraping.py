# needed libraries

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import string

def getPlayer():
    player = ""

    while (player == ""):
         
        player = input("Give me a player: ").strip()

        playerToSplit = player.split()
        if (len(playerToSplit) < 2):
            print("Need a first and last name!")
            player = ""
    
    print()

    playerToSplit = player.split()
    firstName = playerToSplit[0]
    lastName = playerToSplit[1]

    urlSetter(firstName, lastName)

def urlSetter(firstName, lastName):
    #URL to scrape
    playerFullName = "{} {}".format(firstName, lastName)
    lastInitial = lastName.lower()[0]

    url = "https://www.basketball-reference.com/players/{}/".format(lastInitial)

    # collect HTML data 
    html = urlopen(url)

    #create beautiful soup object from HTML
    soup = BeautifulSoup(html, features="lxml")
    
    # use getText() to extract the headers into a list

    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

    #print(headers)

    # get rows from table
    rows = soup.findAll('tr')[1:]
    #print(rows)
    rows_data = [[td.getText() for td in rows[i].findAll('th')]
                 for i in range(len(rows))]

    #rows_data.pop(20)
    print()

    strippedRows = []

    foundPlayer = False

    for elem in rows_data:
        strippedRows.extend(elem[0].strip().split(','))

    playerFullName = playerFullName.translate(str.maketrans('','', string.punctuation))

    for i in range(len(strippedRows)):
        if (strippedRows[i].translate(str.maketrans('', '', string.punctuation)).casefold() == playerFullName.casefold()):
            foundPlayer = True

    if (foundPlayer):
        print("Found the player we wanted")
        print()
        if (len(lastName) >= 5):
            lastNameFirstFive = lastName[:5]
        else:
            lastNameFirstFive = lastName
        if (len(firstName) >= 2):
            firstNameFirstTwo = firstName[:2]
        else:
            firstNameFirstTwo = firstName
        playerNameUrl = "{}{}01".format(lastNameFirstFive.lower(), firstNameFirstTwo.lower())
        playerPage(playerNameUrl, url)

    else:
        print("Player wasn't found")
        getPlayer()

def playerPage(playerNameUrl, url):
    # do something
    url = url + "{}.html".format(playerNameUrl)

    html = urlopen(url)

    soup = BeautifulSoup(html, features="lxml")


if __name__ == "__main__":
    getPlayer()
