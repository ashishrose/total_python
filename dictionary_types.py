#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 23:00:14 2018

@author: novoforce
"""

dict1 = {
		1:"tom",
		2:"dick",
		3:"harry",
		}

print(dict1)

# to result out the items
print(dict1.items())

print(dict1.keys())

k = dict1.keys()# here the keys are returned as a list so we can iterate through it

for i in k:
	print(i)

v = dict1.values()

for i in v:
	print(i)# here the values are returned as a list so we can iterate through it
	
# to delete a key value pair 


del dict1[2]

print(dict1)
	

l1 = ["india","germany","canada"]
print(l1)

l1.append("paris")
print(l1)

l1.remove("india")
print(l1)

l1.insert(1,"brazil")
print(l1)	

print("******************")
	
s1 = {"india","germany","canada"}
print(s1)

s1.update("paris")
print(s1)

s1.remove("india")
print(s1)

s1.update("brazil")

print(s1)
  
	
	
	
	
	
	
	
	