# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:21:26 2017

@author: Anirudh
"""

#Question 1
x=[1,2,3]
y= 'bootcamp'
try:
    z=x+y
except:
    pass
#Results: error, can't concat a list to a string


#Question 2
print(type(x))
print(type(y))
print(len(x))
print(len(y))


#Question 3
#a
2
#is a int
#b
'2'
#is a string, qoutations
#c
2.0
#is a float, decimal
#d
"2.0"
#is a string, quotations
#e
2>1
#is a boolean, true/false
#f
'Itamar'>'Chase'
#is a boolean, greater than
#g
[1,2]
#is a list, brackets
#h
(1,2)
#is a tuple, parantheses
#i
{1: 'one',2: 'two'}
#is a dictionary, curly brackets


#Question 4
1>=0
#true
1>=1
#true
1>1
#false
1==1
#true
1==1.0
#true
'Spencer' == "Spencer"
#true
2**3>3**2
#false
1>=0 or 1<=2
#true
1>=0 and 1<=2
#true


#Question 5
if 2>1:
    print('Yes, 2 is still greater than 1')
#results: Yes, 2 is still greater than 1


#Question 6
if not True:
    print('on the one hand')
else:
    print('but on the other hand')
#results: on the one hand because with True, the if is automatically correct
#results: if we replace with False, then the else function will activate
#results: if not after if, then the else function will activate


#Question 7
cond=True
if cond:
    x="Chase"
else:
    x='Dave'
print(x)
#results: x=Chase, but cond is True so if is also true


#Question 8
x=[1,2,3,4]
y=['x','y','z']

if len(x)>len(y):
    print('x has more')
else:
    print('y has at least as many')

#Question 9
#slicing is extracting characters within strings using brackets


#Question 10
x=[1,2,3,4,5]
print(x[0])
print(x[4])
print(x[:4])

#Question 11
sentence = 'This is a sentence; please slice it.'
print(sentence[0:4])
print(sentence[5:8])
print(sentence[8:10])
print(sentence[10:18])
print(sentence[20:27])
print(sentence[27:33])
print(sentence[33:35])

#Question 12
x=[1,2,"a",'b',"fast",'slow',3,"raghu",'liuren',10]
print(x[0])
print(x[len(x)-1])
print(x[3:7])

#Question 13
for i in x:
    print(i)
    

#Question 14
for i in x:
    if type(i)==str:
        print(i)
    else:
        pass


#Question 15
#range (3,12,2) displays the integers between 3 and 12, starting at 3 and 
#accending by 2 each time
print(list(range(3,12,2)))


#Question 16
x=list(range(0,30,3))
j=0
for i in x:
    j=i+j
print(j)

#Question 17
def pocket_change(pennies,nickels,dimes,quarters):
    x=0
    for i in range(quarters):
        x=x+.25
    for i in range(dimes):
        x=x+.1
    for i in range(nickels):
        x=x+.05
    for i in range(pennies):
        x=x+.01
    print("$",round(x,2))

pocket_change(11,52,38,144)

#Question 18
def notsix():
    x=[]
    y=int(input("How many integers? "))
    for i in range(y):
        z=str(input("Integer? "))
        x.append(list(z))
    print(x)
    
    for j in x:
        if j[0]=='6':
            x.remove(j)
        else:
            pass
    print(x)
    t=[]
    for z in x:
        q=[int(b) for b in z]
        p=0
        for i in range(0,len(q)):
            p=p+q[i]*10**(len(q)-1-i)
        print(p)
        t.append(p)
    print(t)

#Question 19    
old_list = [1234,6783,6,4321,9876]
new_list = [x for x in old_list if str(x)[0] != "6"]
print(new_list)
#results: it gets rid of any list item that starts with the number 6

#Question 20
z={1: 'one', 2: 'two', 3: 'three'}
#a.
#it is a dictionary with length 3
#b
#the integers are the keys and the strings are the values
#c
print(z.get(2))
#d
#z.keys makes a list of all the keys and z.values makes a list of all the values
#e/f
print(list(z.keys()))
print(list(z.values()))
#z.keys makes a list of all the keys and z.values makes a list of all the values
#g
print(list(z))
#prints the keys


#Question 21
# it took 2 hours

    