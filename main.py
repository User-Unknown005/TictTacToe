#Created by Shourya Deep Bera
#All Rights Reserved
from colorama import Fore, Back, Style
import os
file=open("banner.txt",'r')
ban=file.read()
file.close()
print(Fore.CYAN+ban)
print(Style.RESET_ALL)
main_board={'1':' ','2':' ','3':' '
,'4':' ','5':' ','6':' ',
'7':' ','8':' ','9':' '}
x=0
value='X'
check=0
num_input=0
player1=input("Enter name of 1st player")
player2=input("Enter name of 2nd player")
def printboard(board):
    os.system("clear")
    print(" " + board['1'] + "|" + board['2'] + "|" + board['3'])
    print("-- - --")
    print(" " + board['4'] + "|" + board['5'] + "|" + board['6'])
    print("-- - --")
    print(" " + board['7'] + "|" + board['8'] + "|" + board['9'])

def userInput(board):
    global x
    global num_input
    num_input=num_input+1
    x=x+1
    if x%2==0:
        print("Its "+player2+"'s turn")
        print("Enter the position to put 'X' ")
        value='X'                                                       
    else:
        print("Its "+player1+"'s turn")
        print("Enter the position to put 'O' ")
        value = 'O'
    v=input()
    if int(v)>9:
        print(Fore.RED+"Wrong input, the board contains only 9 spaces, enter correct position")
        print(Style.RESET_ALL)
        input()
    else:
        if board[v]=='X' or board[v]=='O':
            print(Fore.RED+"The position is already occupied, enter another position")
            print(Style.RESET_ALL)
            v=input()
    board[v]=value
def calculate(board):
    global check
    if (board['1']=='X' and board['2']=='X' and board['3']=='X') or (board['4']=='X' and board['5']=='X' and board['6']=='X') or (board['7']=='X' and board['8']=='X' and board['9']=='X') or (board['1']=='X' and board['4']=='X' and board['7']=='X') or (board['2']=='X' and board['5']=='X' and board['8']=='X') or (board['3']=='X' and board['6']=='X' and board['9']=='X') or (board['1']=='X' and board['5']=='X' and board['9']=='X') or (board['3']=='X' and board['5']=='X' and board['7']=='X'):
        check=2
        return False
    elif (board['1']=='O' and board['2']=='O' and board['3']=='O') or (board['4']=='O' and board['5']=='O' and board['6']=='O') or (board['7']=='O' and board['8']=='O' and board['9']=='O') or (board['1']=='O' and board['4']=='O' and board['7']=='O') or (board['2']=='O' and board['5']=='O' and board['8']=='O') or (board['3']=='O' and board['6']=='O' and board['9']=='O') or (board['1']=='O' and board['5']=='O' and board['9']=='O') or (board['3']=='O' and board['5']=='O' and board['7']=='O'):
        check=1
        return False
    else:
        return True
user_choice='y'
while(user_choice=='y' or user_choice=='Y'):
 num_input=0
 main_board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ','7': ' ', '8': ' ', '9': ' '}
 while(calculate(main_board)):
     printboard(main_board)
     userInput(main_board)
     if num_input==9:
         print("..........Game Over..........")
         print("The Match is a draw")
         break
     calculate(main_board)
     if check==2:
         printboard(main_board)
         print(Fore.GREEN+"..........Game Over..........")
         print(Fore.GREEN+"Congatultions..... " + player2 + ", YOU WON...")
         print(Style.RESET_ALL)
     elif check==1:
         printboard(main_board)
         print(Fore.GREEN+"..........Game Over..........")
         print(Fore.GREEN+"Congatultions..... " + player1 + ", YOU WON...")
         print(Style.RESET_ALL)
 user_choice=input("Do you want top play again? (y/n)")
