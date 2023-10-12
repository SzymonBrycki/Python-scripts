import string
import random

# structured_list = list()

lc = string.ascii_lowercase
uc = lc.upper()
nr = string.digits
special = string.punctuation

def random_lowercase():
    random_lc = random.choice(lc)
    return random_lc

def random_uppercase():
    random_uc = random.choice(uc)
    return random_uc

def random_nr():
    random_nr = random.choice(nr)
    return random_nr

def random_special():
    random_special = random.choice(special)
    return random_special

# print(structured_list)

def generate_safe_password(size):
    random_list = list()
    if size < 5:
        print("Too little size of safe passowrd! Make it at least 5!")
    else:
        while size != 0:
            random_step = random.randint(1,4)
            if random_step == 1:
                x = random_lowercase()
                random_list.append(x)
            elif random_step == 2:
                x = random_uppercase()
                random_list.append(x)
            elif random_step == 3:
                x = random_nr()
                random_list.append(x)
            elif random_step == 4:
                x = random_special()
                random_list.append(x)
            size = size - 1
    return random_list

def string_from_list(my_list):
    my_string = "".join(my_list)
    # print(my_string)
    return my_string

def split(word):
    return list(word)

def checker(my_string):
    for char in split(lc):
        if char in my_string:
            break
        else:
            x = random_lowercase()
            my_string + x
        break 

    for char in split(uc):
        if char in my_string:
            break
        else:
            x = random_uppercase()
            my_string + x
        break

    for char in split(special):
        if char in my_string:
            break
        else:
            x = random_special()
            my_string + x
        break 

    for char in split(nr):
        if char in my_string:
            break
        else:
            x = random_nr()
            my_string + x
        break
    
    return my_string

    if special not in my_string:
        x = random_special()
        my_string + x
    if nr not in my_string:
        x = random_nr()
        my_string + x
    return my_string

# a = string_from_list(generate_safe_password(6))
#b = checker(a)
# print(b)

c = checker("111111") #should add more things at the end
print(c)

'''
size_of_st_list = len(structured_list)
place = 0

while place <= size_of_st_list:
    random_element = random.choice(structured_list)
    # print(random_element)
    random_list.append(random_element)
    structured_list.remove(random_element)
    place = place + 1

print(random_list)
'''

