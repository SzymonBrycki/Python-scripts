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

def generate_safe_password(size = 20):
    random_list = list()

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

###############################
# PROGRAM
###############################

a = generate_safe_password()
b = string_from_list(a)
print(b)
