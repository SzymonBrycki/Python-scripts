ENG_list = list()
ENG_list_2 = list()
POL_list = list()

beginning = "("
ending = ")" 

sampleString = "English (Polski)"

def findingPOLbeginning(string):
    index = string.rfind(beginning)
    return index

def findingPOLending(string):
    index = string.rfind(ending)
    return index

def findingPOLword(string):
    beginning = findingPOLbeginning(string) + 1 # +1 to exclude the "("
    ending = findingPOLending(string)

    POLcontent = string[beginning:ending]
    return POLcontent

def findingENGword(string):
    ending = findingPOLbeginning(string) #Polish beginning is an English ending

    ENcontent = string[:ending]
    return ENcontent

with open("Zdolności ANG to POL.txt", encoding="utf8") as read_file:
    ENG_list = read_file.readlines()

# print(ENG_list) # OK!!!

ENG_list_2 = [item[6:] for item in ENG_list]

# print(ENG_list_2)

# print(findingPOLbeginning(sampleString))
# print(findingPOLending(sampleString))
    
# print("PL word: ", findingPOLword(sampleString))
# print("EN word: ", findingENGword(sampleString))

for item in ENG_list_2:
    PL_word = findingPOLword(item)
    EN_word = findingENGword(item)

    return_string = PL_word + " (" + EN_word + ")\n"

    POL_list.append(return_string)

POL_list.sort()

print(POL_list)

with open("Zdolności POL to ANG.txt", "w", encoding="utf8") as save_file:
    save_file.writelines(POL_list)


