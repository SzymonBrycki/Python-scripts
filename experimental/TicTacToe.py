import os

# default values of tiles, changed later into "x" or "o"

# tiles_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

one = "1"
two = "2"
three = "3"

four = "4"
five = "5"
six = "6"

seven = "7"
eight = "8"
nine = "9"

# players variables (if True player gets an x)

p_one = False 
P_two = False

# players tiles (later set to either x or o)

p_o_tile = " "
P_t_tile = " "

# who's turn? (basec on modulo 2: == 1 is player one, == 0 is player two)

turn = 1

# global variable that's checking if there's a line created

isline = False

# check is a given player wins or not

playerx_wins = False
playero_wins = False

#######################################################################

def clearscreen():
     os.system('cls' if os.name == 'nt' else 'clear')

#######################################################################

def whos_who_loop():
    global p_one, p_two, p_o_tile, p_t_tile
    
    who = input ("Press '1' or '2'. ")
    if who == "1":
        print ("Player 1 gonna be 'x', player two - 'o' ")
        p_one = True
        p_o_tile = "x"
        P_T_tile = "o"
    elif who == "2":
        print ("Player 1 gonna be 'o', player two - 'x' ")
        p_two = True
        p_o_tile = "o"
        p_t_tile = "x"
    else:
        print("You pressed a wrong number. Please, try again. ")
        whos_who_loop()
        
#######################################################################

def whos_who():
    print ("Who's gonna be player 'x'? Player one or player two? ")
    whos_who_loop()

#######################################################################
    
##    who = input ("Press '1' or '2'.")
##    if who == 1:
##        p_one = True
##    elif who == 2:
##        p_two = True
##    else:
##        print("You pressed a wrong number. Please, try again.")        

#######################################################################

def printboard():
    print (" ", one, "| ", two, " | ", three, " ")
    print (" ", four, "| ", five, " | ", six, " ")
    print (" ", seven, "| ", eight, " | ", nine, " ")

#######################################################################

def changetile(tile_nr, player_tile): # ??? to change later? ???
    global one, two, three, four, five, six, seven, eight, nine
    
    if one == "1" and tile_nr == "1":
        one = player_tile
    elif two == "2" and tile_nr == "2":
        two = player_tile
    elif three == "3" and tile_nr == "3":
        three = player_tile
    elif four == "4" and tile_nr == "4":
        four = player_tile
    elif five == "5" and tile_nr == "5":
        five = player_tile
    elif six == "6" and tile_nr == "6":
        six = player_tile
    elif seven == "7" and tile_nr == "7":
        seven = player_tile
    elif eight == "8" and tile_nr == "8":
        eight = player_tile
    elif nine == "9" and tile_nr == "9":
        nine = player_tile
    else:
        print("Something is not right. Please, try again. ")
        changetile(tile_nr, player_tile)

#######################################################################

def islineleftright():
    global one, two, three, four, five, six, seven, eight, nine
    global isline, playerx_wins, playero_wins
    
    if one == "x" and two =="x" and three == "x":
        isline = True
        playerx_wins = True
    elif one == "o" and two =="o" and three == "o":
        isline = True
        playero_wins = True
    elif four == "x" and five == "x" and six == "x":
        isline = True
        playerx_wins = True
    elif four == "o" and five == "o" and six == "o":
        isline = True
        playero_wins = True
    elif seven == "x" and eight == "x" and nine == "x":
        isline = True
        playerx_wins = True
    elif seven == "o" and eight == "o" and nine == "o":
        isline = True
        playero_wins = True
    else:
        pass

#######################################################################

def islineupdown():
    global one, two, three, four, five, six, seven, eight, nine
    global isline, playerx_wins, playero_wins

    if one == "x" and four == "x" and seven == "x":
        isline = True
        playerx_wins = True
    elif one == "o" and four == "o" and seven == "o":
        isline = True
        playero_wins = True
    elif two == "x" and five == "x" and eight == "x":
        isline = True
        playerx_wins == True
    elif two == "o" and five == "o" and eight == "o":
        isline = True
        playero_wins == True
    elif three == "x" and six == "x" and nine == "x":
        isline == True
        playerx_wins = True
    elif three == "o" and six == "o" and nine == "o":
        isline == True
        playeox_wins = True
    else:
        pass

#######################################################################

def islinediagonal():
    global one, two, three, four, five, six, seven, eight, nine
    global isline, playerx_wins, playero_wins
    
    if one == "x" and five == "x" and nine == "x":
        isline = True
        playerx_wins = True
    elif one == "o" and five == "o" and nine == "o":
        isline = True
        playero_wins = True
    elif seven == "x" and five == "x" and three == "x":
        isline = True
        playerx_wins = True
    elif seven == "o" and five == "o" and three == "o":
        isline = True
        playero_wins = True
    else:
        pass

#######################################################################

def isline():
    global one, two, three, four, five, six, seven, eight, nine
    global isline, playerx_wins, playero_wins

    islineleftright()
    islineupdown()
    islinediagonal()

#######################################################################

def changeboard():
    global turn
    
    if turn % 2 == 1:
        if p_one == True:
            t = input ("Where to put your 'x', player one? ")
        else:
            t = input ("Where to put your 'o', player one? ")

        changetile(t, p_o_tile)
        turn += 1
    else:
        if p_two == True:
            t = input ("Where to put your 'x', player two? ")
        else:
            t = input ("Wher to put your 'o', player two? ")

        changetile(t, p_t_tile)
        turn += 1

#######################################################################
        
def changeprint():
    first_time = 0
    if first_time == 0:
        clearscreen()
        printboard()
        changeboard()
        clearscreen()
        printboard()
        first_time = 1
    else:
#    clearscreen() # to change later? For now with no clearing?
        changeboard()
        printboard()        

#######################################################################    

# way to clear the screen ! ! !
#
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
    
##########################################
#
#                UP DEFS
#
#             DOWN EXECUTE
#
##########################################

whos_who()
# printboard()
changeprint()


    
