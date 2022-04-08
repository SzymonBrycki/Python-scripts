#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Print_epoch.py
#  
#  Copyright 2021 Szymon "Kaworu" Brycki <szymon.brycki@gmail.com>
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

import time

def epoch_beginning():
	'''
	This function returns the beginning of an epoch on a given computer. 
	To use, just print the function.
	'''
	
	time_string = "The epoch on this computers begins with %A, %d %b %Y"
	epoch = time.gmtime(0)
	epoch2 = time.strftime(time_string, epoch)
	return epoch2
	
print(epoch_beginning())
