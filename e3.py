#!/usr/bin/env python
#question 3 Import your CSV files into a single `pandas.DataFrame()`
#and plot the Republican vote share in Accomack County, Albermarle County, Alexandria City,
#and Alleghany County as a fraction of Total Votes Cast.
#Save your work as `e3.py` and commit your plots as:
#`accomack_county.pdf`, `albemarle_county.pdf`, `alexandria_city.pdf`, and `alleghany_county.pdf`.

import pandas as pd
import csv
import glob
from e1 import *

# get data file names
path =r'/Users/camilacarrasco/Dropbox/MSESP/5.Fall2017/Programming/GitHub/hw-6-camilacd'
filenames = glob.glob(path + "/*.csv")

all_years = []
for filename in filenames:
    all_years.append(filename)

'''
*Hint: there are empty columns, and the 'relevant' column names (party names) are in the second row.
Steps: import that single row as a dictionary, to change the column names.
'''
for line in ELECTION_ID:
     header = pd.read_csv(file_name, nrows = 1).dropna(axis = 1)
     d = header.iloc[0].to_dict()
     df = pd.read_csv(file_name, index_col = 0, thousands = ",", skiprows = [1])
     df.rename(inplace = True, columns = d) # rename to democrat/republican
     df.dropna(inplace = True, axis = 1)    # drop empty columns
     df["Year"] = line[0]

'''
Hint: Write a for loop, placing up all of your dataframes (elections) in a list.
Then `concat` them together.  You'll probably want just these columns:
     ["Democratic", "Republican", "Total Votes Cast", "Year"]
'''
republican_share=[]
df['republican share']=df['Republican'/df['Total Votes Cast']]

'''
   * Then you just need to define a new column, Republican Share.
   * You can either "select off" the column and plot the year, or you can [pivot](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pivot.html) all of the city/county names up as columns, keeping the
     * If you do this, you may want to deal with the counties that were occasionally split between congressional districts, "(CD X)".  You could do this by fixing the labels with a regular expression.  Then group by County/City, take the sum, and reset the index.
'''

county = {'Accomack County':'accomack_county.pdf', 'Albemarle County':'albemarle_county.pdf', \
          'Alexandria City':'alexandria_city.pdf', 'Alleghany County':'alleghany_county.pdf'}

for x,y in county.items():
    df=filenames[filenames.index==x]
    plt.plot(df['Year'],df['republican share'], label=Republican Share of Votes)
    plt.xlabel('Year')
    plt.ylabel('Share of total Votes')
    plt.legend()
    plt.savefig(y)

republican_share=pd.read_csv("president_general_2016.csv", index_col = 'Date', parse_dates = ['Date'])
