# -*- coding: utf-8 -*-
"""Day 6 Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gpLOGbkhIhsYC3Gv0dZwleF5BfbImqGA
"""

# Day 6 Assignment
# Decorator

def mod_div (fun):
	def inner (a,b):
		if a < b :
			a, b = b, a 
		return fun(a, b)
	return inner
	
@mod_div
def div(a, b):
	return  a // b

a= int(input ('Enter first number:'))
b= int(input ('Enter second number:'))

print(a,b)

print(div(a, b))