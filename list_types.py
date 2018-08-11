#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 20:30:27 2018

@author: novoforce
"""

#list starts with [] brackets

l1 = []
print(l1)

l1 = [10,20,30.5,5]
print(l1)
#we can perform indexing, slicing and repetition on the list

print(l1[3])#indexing
print(l1[1:4])#slicing
print(l1*4)# repetition

#for appending
l1.append(40)
print(l1)

#for removing
l1.remove(30.5)
print(l1)

#to remove elements using index value
#del(l1[1])
#print(l1)

#to remove alll the elements from the list
#l1.clear()
print(max(l1))
print(min(l1))

#to insert an element
l1.insert(2,99)
print(l1)

#to sort element in a list

l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)
















