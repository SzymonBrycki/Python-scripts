#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FileCounter.py
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

import os

BaseFolder = input("Enter the PATH towards the base file: ")

FilesSUM = 0
DirectoriesSUM = 0

text_file = "FileMapper.txt"

def findLastSlash(my_string):
	'''
	Finds last slash in a given string. 
	
	Arguments: my_string (str).
	
	Returns: x <which is minus number being the index of lash found slash> (int)
	'''
	
	slash = "\\"
	x = -1
	for char in my_string:
		if my_string[x] == slash:
			return x
		else:
			x = x-1
			
		# WEEEEEE! It's working! :3

def countSlashes(base):
	'''
	Counts all slashes in a given argument.
	
	Arguments: base (str).
	
	Returns: numberOfSlashes (int)
	'''
	
	numberOfSlashes = base.count("\\")
	return numberOfSlashes	

def printNicelyFolders(base):
	'''
	A function which prints folders in this program in a nice fashion. 
	
	Arguments: base (str)
	
	Returns: append main_string
	'''
	
	slashes = countSlashes(base)
	slashes_minus = countSlashes(BaseFolder)
	slashes_final = slashes - slashes_minus
	
	beginning_of_string = findLastSlash(base)
	my_new_string = base[beginning_of_string:]
	
	double_space = "  "
	spacechars = double_space * (slashes_final -1)
	my_new_string_2 = spacechars + my_new_string
	
	slashes_of_main = countSlashes(BaseFolder)
	slashes_compare = countSlashes(base)
	
	if base == BaseFolder:
		main_string.append(my_new_string)
	else:
		main_string.append(my_new_string_2)
		
		'''
		if slashes_of_main - slashes_compare == -1:
			print("┖ " + my_new_string)
		else:				
			print(spacechars + " ┖ " + my_new_string)
		'''
	
def printNicelyFiles(file):
	pass
		
		
'''
print("Printing folders nicely!")	
printNicelyFolders("E:\Personal Data\My Folders\ExampleDir")
'''	

print("") #just a nice space
for base, dirs, files in os.walk(BaseFolder):
	printNicelyFolders(base) #put here function "printNicelyFolders
	# for name in files:
		# printNicelyFiles(name)
	for directories in dirs:
		DirectoriesSUM +=1
	for Files in files:
		FilesSUM += 1
		
print("")
print("Total number of files:", FilesSUM)
print("Total number of directories:", DirectoriesSUM)
print("Total items:", FilesSUM + DirectoriesSUM)

