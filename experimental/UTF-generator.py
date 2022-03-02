#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  UTF-generator.py
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

import unicodedata

def unicode_printer(number):
	
	character = chr(number)
	
	name = unicodedata.name(character)
	
	print(number, "-", character, name)
	
#################################


#################################	

unicode_printer(10)
unicode_printer(11)
unicode_printer(12)
unicode_printer(13)
unicode_printer(14)
unicode_printer(15)
unicode_printer(16)
unicode_printer(17)
unicode_printer(18)

unicode_printer(1000)
