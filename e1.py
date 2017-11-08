#!/usr/bin/env python
#question 1 Using BeautifulSoup (docs), print, then save as ELECTION_ID,
#a list containing the years and election IDs in exactly this format.
'''
2016 80871
2012 44930
2008 39050
2004 41055
2000 39517
'''

from bs4 import BeautifulSoup as bs
import requests

#Set up the `soup`: make the `requests.get()`
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(addr)
#Scraping the data from the webpage
html = resp.content
#save the soup, and parse it.
soup = bs(html, "html.parser")
#Grab all of the instances where the class is `election_item`
instances = soup.find_all("tr","election_item")

ELECTION_ID = []

#extract the IDs with a loop; split them on dashes to extract the numbers
for y in instances:
    year = y.td.text
    year_id = y["id"][-5:]
    i = [year, year_id]
    ELECTION_ID.append(i)

with open("ELECTION_ID","w") as ELECTION_ID_file:
    for line in ELECTION_ID:
        ELECTION_ID_file.write(line[0] + "" + line[1])
        print(line[0],line[1])
