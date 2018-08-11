#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 18:20:34 2018

@author: novoforce
"""
#first program
print("hii python is easy")

#commments in pyython #-for single line """for multiline comment"""

#python uses intendation to recognise the block of codes

print("datatypes")

a=10
b=55
c=-66

print(a,b,c)

x=-6.66
y=78
z=5.9

print(x,y,z)
#for finding the type of data
print(type(z))

print("complex datatypes")

d= 3+2j
print(d)
print(type(d))

print("binary datatypes")
#binary always starts with "0B" followed by the binary values

a= 0B1010
print(a)
print(type(a))

print("hexadecimal datatypes")

b= 0XFF
print(b)
print(type(b))

print("boolean datatypes")

c= True
print(c)
print(type(c))

print(9>8) #bool is used for conditional statements 

print("type conversion in python")

h = int(x) #to convert float to int
print(h)

i= float("22")# to convert int to float
print(i)

#to convert to binary value
print("to convert to binary value")
print(bin(100))

# to convert to hexadecimal value
print("to convert to hexadecimal value")
print(hex(55))




