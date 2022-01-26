#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Proportion.py
#  
#  Copyright 2022 Szymon "Kaworu" Brycki <szymon.brycki@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def Proportion():
	
	n = input("Which number you wish to calculate? [A/B/C/D] ")
	
	if n == "A":
		
		B = input("Enter B(%) ")
		C = input("Enter C ")
		D = input("Enter D(%) ")
		
		B = int(B)
		C = int(C)
		D = int(D)
		
		result = (B*C)/D
		
		print("")
		print("A is equal to: ", result)
		
	elif n == "B":
		
		A = input("Enter A ")
		C = input("Enter C ")
		D = input("Enter D(%) ")
		
		A = int(A)
		C = int(C)
		D = int(D)
		
		result = (A*D)/C
		
		print("")
		print("B is equal to: ", result, "%")
	
	elif n == "C":
		
		A = input("Enter A ")
		B = input("Enter B(%) ")
		D = input("Enter D(%) ")
		
		A = int(A)
		B = int(B)
		D = int(D)
		
		result = (A*D)/B
		
		print("")
		print("C is equal to: ", result)
		
	elif n == "D":
		
		A = input("Enter A ")
		B = input("Enter B(%) ")
		C = input("Enter C ")
		
		A = int(A)
		B = int(B)
		C = int(C)
		
		result = (B*C)/A
		
		print("")
		print("D is equal to: ", result, "%")
		
	else:
		print("")
		print("Wrong input. Try again.")
		Proportion()
		
#####################################		

print("Welcome to my proportions calculator!")
print("Below is the proportion equation.")
print("Enter the number you are looking for and then all other data.")
print("The program will calculate the unknown.")
print("")
print("A = B%")
print("C = D%")
print("")
print("A*D% = C*B%")
print("")
		
Proportion()		
	
