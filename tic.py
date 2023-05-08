#lets create a tictac toe game 

# first lets define our board 

# This is first part of board as  in list 
# it gives the output as ==>> ['-', '-', '-', '-', '-', '-', '-', '-', '-']\
print (''' Welcome to tic-tactoe
       procedd by being X or O
       
       ''')
import random
board =["-","-","-",
        "-","-","-",
        "-","-","-"
]


# print(board)
def print_board():
    print(board[0] + " | "+ board[1] + " | " +board[2])
    print("+++++++++++")
    print(board[3]+ " | " +board[4] + " | " + board[5])
    print("+++++++++++")
    print(board[6] + " | "+ board[7]+ " | "+ board[8])
        
print_board()

# we can definre the whole board as tic tactes format as above 
# and it loks alike
''' 
- | - | -
+++++++++++
- | - | -
+++++++++++
- | - | 
'''

def choose_letter():
    
    letter = " "
    # this (while not) loops written below execute until the user input the variable  x  or o 
    # suppose if the user  mistakely give input of z then it will ask again 
    # while works as loop keyword not puts the condition 
    # that until and unless x or o are inputed by users 
    #repeadetly print do you want to be x or O?
    
    # If letter has the value 'X' or 'O', then the loop’s condition is False and 
    # lets the program execution continue past the while block. 
    while not (letter == "X" or letter =="O"): # not gives the condition to repeat until  {X and O} ajd print 
      print('Do you want to be X or O? ') # do you want to be X or O #
      letter = input().upper()
    if letter == "X":
         return ["X","O"]  # here 
    else:
        return["O","X"]   
choose_letter()
# Now to chose who make the first move 

def first_move():
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "Players choice"
    
# first_move()

# to make the  mark on the board d
def make_move(board,letter,move):
    board[move]=letter
# to make the 
    
        
    








