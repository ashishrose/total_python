#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:27:40 2018

@author: novoforce
"""

s={10,20,30,"xyz"}
print(s)

print(type(s))

#to add elements to the set we use "update"
s.update([88,99])
print(s)

#we can never perform indexing,slicing,repetition on set

#to remove element
s.remove(30)
print(s)

#frozen set in python
f = frozenset(s)#now f cannot be indexed, sliced,repetited

