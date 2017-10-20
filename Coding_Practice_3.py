# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:10:18 2017

@author: Anirudh
"""
"""
Question 1
"""
import pandas as pd
data = {'BRA': [13.37, 13.30, 14.34, 15.07, 15.46, 15.98, 16.10],
        'JPN': [33.43, 31.83, 33.71, 34.29, 35.60, 36.79, 37.39],
        'USA': [48.30, 46.91, 48.31, 49.72, 51.41, 52.94, 54.60],
        'Year': [2008, 2009, 2010, 2011, 2012, 2013, 2014]}
weo  = pd.DataFrame(data)
#Question 1a
'''
it is to make sure that there is no overlap between the built in library
and imported library
'''

#Question 1b
print(type(data))
'''
data is a dictionary
'''

#Question 1c
'''
it has pd in front of it to indicate that the DataFrame method is coming from
the pandas library
'''

#Question 1d
print(type(weo))
'''
it is a pandas.core.frame.DataFrame
'''

#Question 1e
weo.shape
'''
there are 4 columns and 7 rows
'''

#Question 1f
weo.dtypes
'''
The countries are float64, the year is an integer64. 
'''

#Question 1g
print(type(weo['Year']))
'''
This is a series, gives back a table with the list of years
'''
print(type(weo[['Year']]))
'''
This is a dataframe, gives back a table with the list of years
'''
try:
    print(type(weo[[3]]))
except:
    pass
'''
This is giving an error
'''

#Question 1h
weo['Year'] = weo['Year'].astype('float64') 

#Question 1i
t = weo.tail(3)
print(t)
'''
t is a dataframe type and it is the last 3 years of the data
'''

#Question 1j
df  = weo[:3]

#Question 1k
'''
It is a Series
'''

#Question 1l
weo['GDP_ratio'] = weo['BRA'] / weo['JPN']

#Question 1m
weo = weo.drop('GDP_ratio', 1)
 
 #Question 1n
weo.columns.tolist()
#'['BRA', 'JPN', 'USA', 'Year']'

weo.index.tolist()
[0, 1, 2, 3, 4, 5, 6]

#Question 1o
weo = weo.set_index('Year')

#Question 1p
weo.columns = ['Brazil', 'Japan', 'United States']

#Question 1q
excel = pd.ExcelWriter('test.xlsx')
weo.to_excel(excel)

#Question 1r
weo['Brazil'].mean()
14.802857142857144

weo['Japan'].mean()
34.71999999999999

weo['United States'].mean()
50.31285714285714

#Question 1s
weo['mean'] = weo.mean(axis=1)

#Question 1t
weo.plot()

#Question 1u
weo.plot(color = ['g', 'r', 'b'])

#Question 1v
weo.plot(logy=True)

#Question 1w
weo['Brazil'].plot()



#---------------------------------------------
"""
Question 2
"""

import pandas as pd
url1 = 'https://raw.githubusercontent.com/NYUDataBootcamp/Materials/master/'
url2 = 'Data/entry_poll_fall16.csv'
url = url1 + url2
#Question 2a
ep = pd.read_csv(url)

#Question 2b
list(ep)
['TimeStamp',
 'Why have you enrolled in this course?  ',
 'What program are you enrolled in?',
 'How much programming experience have you had?',
 'How much experience with probability and statistics have you had?',
 'What is your expected major or concentration? ',
 'What career path most interests you? ',
 'Do you use social media for information purposes?  Check all that apply.',
 'What kinds of data most interest you?  List any that cross your mind.  ',
 'If we have time -- and we may not -- what special topics would interest you? 
 'Check all that apply.']
#variables

#Question 2c
ep.dtypes
'all objects'

#Question 2d
ep.columns['TimeStamp', 'Enrolled', 'Program', 'Programming Experience', 
           'Statistics Experience', 'Expected Major', 'Career Path', 
           'Social Media', 'Interesting Data', 'Interesting Topics']
# i dont know why it is isn't working

#Question 2e
ep[list(ep)[1]].value_counts()
#it is listing and counting how many times the answers came up for that 
#question



#------------------------------------------------------------------
"""
Question 3
"""
import pandas as pd
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/'
url2 = 'master/college-majors/recent-grads.csv'
url = url1 + url2

#Question 3a
df538 = pd.read_csv(url)
ep.shape
'''
10 columns, 85 rows
'''

#Question 3b
df = df538[:11]
print(df)

#Question 3c
df538.ix[2]
df538.ix[4]
df538.ix[15]
df538.ix[16]
df538.ix[17]
'''
extracts the values from specific rows (3,5,16,17,18) within the data frame 
'''

#Question 3d
df538.set_index('Major')

#Question 3e
df538['Total'].sort_values(ascending = False)

#Question 3f
df538.sort_values('Total',ascending=False).head(10)

#Question 3g
df538['Median'].sort_values(ascending=False).head(10).plot('barh')
df538['P25th'].sort_values(ascending=False).head(10).plot('barh')