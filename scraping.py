# needed libraries

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def getPlayer():
    player = ""

    while (player == ""):
         
        player = input("Give me a player: ")

        playerToSplit = player.split()
        if (len(playerToSplit) < 2):
            print("Need a first and last name!")
            player = ""
    print()
    print("Player chosen was {}".format(player))

    playerToSplit = player.split()
    firstName = playerToSplit[0]
    lastName = playerToSplit[1]

    urlSetter(firstName, lastName)

def urlSetter(firstName, lastName):
    #URL to scrape

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
    i = 0
    for elem in rows_data:
        strippedRows.extend(elem[0].strip().split(','))
        print(strippedRows[i])
        i += 1

    # now that I have list of players, parse name for player page url, then
    # do the rest

if __name__ == "__main__":
    getPlayer()
