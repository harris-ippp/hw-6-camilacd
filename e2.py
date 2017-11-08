#!/usr/bin/env python
#question 2
'''
   Loop over your list from Part 1, and use requests to download the CSV files from.
   You will format them like so:

   http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/


   Save your work in `e2.py` and commit your csv file for the 2016 election, naming it `president_general_2016.csv`.

   Don't run parts 1 and 2 every time you do this part -- once it's downloaded leave it be!
   We don't want to bother the Virginia Election site too much! &nbsp;<details><summary>Hints</summary>
   * Loop over a file using: `for line in open("ELECTION_ID"):`.
   * You can print the contents of the response using `resp.text`.
     Instead, write them to files (see slide 8 of [lecture 3B](https://github.com/harris-ippp/lectures/raw/master/03/files.pdf)) with a meaningful name structure:

     ```
     file_name = year +".csv"
     with open(file_name, "w") as out:
       out.write(resp.text)
     ```
   </details>
'''

from bs4 import BeautifulSoup as bs
import requests
import csv

from e1 import*

for line in ELECTION_ID:
    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
    replace_url = base.format(line)
    response = requests.get(replace_url).text
    file_name = "president_general_"+ line[0] +".csv"
    with open(file_name, 'w') as output:
        output.write(response.text)
