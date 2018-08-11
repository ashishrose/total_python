#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 19:25:57 2018

@author: novoforce
"""

s = "you are awesome"
print(s)

#for assigning strings to multiple lines

s1 = """hey this is ashish and 
im awesome"""

print(s1)

# to reachout to individual characters in the string 

print(s[0])
print(s[8])
# now * operator is used to repeat the string multiple times
print(s*5)

# to find the length of the string
print(len(s))
print(len(s1))


print("now here we see SLICING in action")

print(s[0:5])# here 0 is the starting index and 5 is the ending index
print(s[:5])
print(s[5:15])

print(s[-3:-1]) #here the indexing is startng from back of the list

print(s[0:9:2])# here 2 means the STEP value ie. how many steps to be taken while printing

print("to reverse a string")
print(s[15::-1])
print(s[::-1])

#s1 = "   you are awesome     hii   "
print("to strip spaces in the strig")

print(s1)# initial 
print(s1.strip())#final

#to remove left white spaces
print(s1.lstrip())

#to remove right white spaces
print(s1.rstrip())


print("to find the sub string in the string")

print(s1.find("awe"),0,len(s1))# it means that the awe starts from 11 position..... here 0 is the starting and len(s1) ending where we want to search for the string

print(s1.find("awe",0,len(s1)))

print(s1.count("a"))#to find the frequency

print(s1.replace("ashish","rose"))

print(s1.upper())# for uppercase
print(s1.lower())# for lowercase
print(s1.title()) # for titlecase ie. the words starting after the space 









