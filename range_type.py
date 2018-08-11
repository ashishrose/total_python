#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:44:12 2018

@author: novoforce
"""
#range datatype

r = range(5) # values will be iterated till <5

for i in r:
	print(i)
	
print("********")
r = range(3,9)

for i in r:
	print(i)
	
print("********")
# by passing a step value

r = range(3,9,2) # here 2 is the step value

for i in r:
	print(i)s