#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FileAndFolderMapper.py
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

print("")
print("Printing folders nicely!")
print("")
BaseFolder = input("Enter the PATH towards the base file: ")

FilesSUM = 0
DirectoriesSUM = 0

main_list = list()
main_string = None

double_space = "  "
new_line = "\n"

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

def determineFinalSlashes(base):
	'''
	Function that determines how many double spaces should be entered.

	Argument: base (str)

	Returns: slashes_final (int)
	'''
	slashes = countSlashes(base) # number of slashes in current folder
	slashes_minus = countSlashes(BaseFolder) # number of slashes in the Base Folder 
	slashes_final = slashes - slashes_minus # number of slashes that's a difference between BaseFolder and current folder

	return slashes_final

def sliceToLastElement(base):
	'''
	A function which strips the string of all adress of a file/folder into it's last element (the file/folder itself).

	Arguments: base (str) [the adress of a file/folder]

	Returns: my_new_string
	'''
	beginning_of_string = findLastSlash(base) # the number of last slash in given folder, counted from the back

	my_new_string = base[beginning_of_string:] # string from the last slash till beginning of folder name

	return my_new_string

def addNicelyFolders(base):
	'''
	A function which add folders in this program to main_list in a nice fashion. 
	
	Arguments: base (str)
	
	Returns: appends main_string with my_new_string_2
	'''
	
	new_string = sliceToLastElement(base)
	slashes_final = determineFinalSlashes(base)

	if base == BaseFolder:
		my_new_string_2 = new_string + new_line # ... at the beginning of new print
	else:
		my_new_string_2 = (double_space * slashes_final) + new_string + new_line # add additional double space in case of non-BaseFolder folders
	
	slashes_of_main = countSlashes(BaseFolder)
	slashes_compare = countSlashes(base)

	main_list.append(my_new_string_2)

def printTheMainList():
	'''
	Function that prints the main_list, so we can see what's in there.
	'''
	global main_string

	main_string = " ".join([str(item) for item in main_list])

	print(main_string)

def finding_slash(my_list): # it needs to be list[1], list[-1] etc !!!
	'''
	Function that checks if there is a slash in a given list

	Arguments: my_list (list[nr])

	Returns: False if no slash or position of slash (if contains one)
	'''

	# searched_thing = my_list.join()

	searched_thing = " ".join(map(str, my_list))

	boolean = searched_thing.find("\\")

	if boolean == -1:
		return False 
	else:
		return boolean

def spaces_previous(my_list):
	'''
	Function that finds number of spaces in the previous list member.

	Argument: my_list (list)

	Returns: The number of spaces (being formatted - it should work no matter id double_space is 1, 2 or 4 spaces)
	'''
	previous_list = my_list[-1]
	searched_thing = " ".join(map(str, previous_list))
	# searched_thing = previous_list.join() WRONG???

	space_counter = 0

	for char in searched_thing:
		if char == " ":
			space_counter = space_counter + 1
		else:
			break

	number_of_formatted_spaces = int(space_counter / 4)

	return number_of_formatted_spaces

def finalStringOfFiles(file):
	'''
	A function to determine the final string that a file adress should have been.

	Argument: file (str)

	Returns: string_with_file (str)
	'''
	previous_entry = main_list[-1]

	if finding_slash(previous_entry) is False:
		spaces = spaces_previous(main_list)
	else:
		spaces = spaces_previous(main_list) + 1

	string_with_file = (double_space * spaces) + sliceToLastElement(file)
	return string_with_file

def addNicelyFiles(file):
	'''
	A function that add files to main_list in a nice fashion.

	Argument: file (str)

	Returns: appends main_list (with my_string)
	'''
	my_string = finalStringOfFiles(file) + new_line

	main_list.append(my_string)
		
'''
print("Printing folders nicely!")	
printNicelyFolders("E:\Personal Data\My Folders\ExampleDir")
'''	

print("") # just a nice space
for base, dirs, files in os.walk(BaseFolder):
	addNicelyFolders(base) # put here function "printNicelyFolders
	# for name in files:
		# printNicelyFiles(name)
	for directories in dirs:
		DirectoriesSUM +=1
	for Files in files:
		addNicelyFiles(Files)
		FilesSUM += 1

printTheMainList()
		
print("")
print("Total number of files:", FilesSUM)
print("Total number of directories:", DirectoriesSUM)
print("Total items:", FilesSUM + DirectoriesSUM)
print("")

while True:
	Yes_no = input("Do you wish to save the result of the program? Y/N ")

	print("")

	if Yes_no.upper() == "Y":
		name = input("Enter the name of file you wish to save OR leave blank for default name ")

		print("")
		
		if len(name) == 0:
			name = "FileAndFolderMapper.txt"

		else:
			name = name + ".txt"

		f = open(name, "w")
		opening = "Snapshot of a folder created in FileAndFolderMapper.py "

		from datetime import date, datetime

		today = date.today()

		today_formatted = today.strftime("%d-%b-%Y")

		now = datetime.now()

		now_formatted = now.strftime("%H:%M:%S") 

		date_of_creation = "File created on: " + today_formatted + " " + now_formatted

		file_buffer = [opening, new_line, date_of_creation, new_line, new_line, BaseFolder, new_line, main_string]
		file_buffer2 = str(file_buffer)

		size = len(file_buffer)
		offset = 0
		chunk = 100

		while True:
			if offset > size:
				break
			f.write(file_buffer2[offset:offset+chunk])
			offset = offset + chunk

		# f.writelines("%s\n" % line for line in file_buffer)
		# f.writelines(file_buffer)

		f.close()

		cwd = os.getcwd()
		cwd_2 = cwd + "\\" + name 

		print("File saved under the following destination: ")

		print("")
		print(cwd_2)

		break
	
	elif Yes_no.upper() == "N":
		print("Finishing the program without saving. ")

		break

	else:
		print("Unknown command (must be Y/N). Try again. ")


print("")
iks = input("Enter any character to finish... ")
exit() 
