# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 01:44:22 2017

@author: Anirudh
"""


#1a. 2+5
print(2+5)
#results: 7; simple addition

#1b.2 + 5
print(2 + 5)
#results: 7; extra spaces are not recognized

#1c. 2*5
print(2*5)
#results: 10; multiplication

#1d. 2/5
print(2/5)
#results: 0.4; division

#1e. 2**5
print(2**5)
#results: 32; exponents


#2
x=7
x=x+3
print(x)
#results: 10; we set the new variable value to 7+3 = 10


#3
x=3
y=x
x=10
print(y)
#results: 3; x changed to 10 after we set y equal
# to the original value of 3, so the variable y
#did not recognize the new change


#4
x=3
x=x/2
y='abc'
z=y+y
print(x,z)
#results: 1.5 abcabc; you can add two strings together


#5
x=3
x=x/2
y='abc'
try:
    z=x+y
    print(x,z)
except:
        pass

#results: error; can't add a string and integer


#6
x=3
y=24
z=y/x
print(x,y,z,sep=' | ') 
#results: 3 | 24 | 8.0; you can do basic math with integers


#7
x=3
y='24'
try:
    z=y/x
    print(x,z)
except:
    pass
#results: error, because the quotations make the 24 a string, not a number


#8
x="I am a #string" #whoa, a string!
print(x)
#results: I am a #string, the block within the quotations was printed,
#but the comment wasn't


#9
x=[1,2,3]
y=[42,43] 
z=x+y
print(z)
#results: [1,2,3,42,43]; created a bigger list of 5 numbers by adding the
#two lists together


#10
x=[1,2,3]
y=42
try:
    z=x+y
except:
    pass
#results: error; can only concatenate list with list, not list with integer


#11
x1=12
#x1 is an integer
x2=12.0
#x2 is a float
x3='12.0'
#x3 is a string
x4=[12]
x5=[12,12.0,'12.0']
#x4 and x5 are lists


#12
print(type(42))
#its an integer
print(type(42.0))
#its a float
print(type('42.0'))
#its a string
print(type("42.0"))
#its a string
print(type("""42.0"""))
#its a string
print(type([1,2]))
#its a list
try:
    print(type[[1]+[2]])
except:
    pass
#its an error
print(type(1+2))
#its an integer
print(type(print))
#its a built-in function


#13
print(type(float(str(int('1234')))))
#its an float because that is the last change that happened



#14
print(type(int(float('12.34'))))
#its an integer because that is the last change that happened


#15
print(len([1234]))
#results: 1; only one item in list
print(len("1234"))
#results: 4; 4 characters in the string 1234
try:
    print(len(1234))
except:
    pass
#results: error, len can't be used on integers


#16
x=[]
print(len(x))
#results: 0, no items in list
print(type(x))
#results: class is list


#17
x='abcde'
x=list(x)
print(x)
#results: ['a','b','c','d','e']


#18
x=1234
#18a
print(float(x))
#results: 1234.0 is a float

#18b
print(str(x))
#results: 1234 as a string

#18c
try:
    print(list(x))
except:
    pass
#results: error, integer isn't iterable


#19
x="luke, i am your father"
print(x.title())
#results: Like, I Am Your Father

#20
x="How many characters and words are in this string"
#20a
print(len(x))
#results: 48
#20b
print(list(x))
#results a list of letters
#20c
print([x.split()])
#results: a list of words
print(len(x.split()))
#results: 9