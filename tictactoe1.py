from random import sample
#board is a list that will contain all the filled and left boxes
sign=[]
lst1=[]
Free=[]
lst=[0,1,2,3,4,5,6,7,8]
lst1=sample(lst,9)
board=[1,2,3,4,5,6,7,8,9]
count2=0
def DisplayBoard(board):
   print("+-------+-------+-------+")
   print("|       |       |       |")
   print("|  ",board[0],"  |  ",board[1],"  |  ",board[2],"  |")
   print("|       |       |       |")
   print("+-------+-------+-------+")
   print("|       |       |       |")
   print("|  ",board[3],"  |  ",board[4],"  |  ",board[5],"  |")
   print("|       |       |       |")
   print("+-------+-------+-------+")
   print("|       |       |       |")
   print("|  ",board[6],"  |  ",board[7],"  |  ",board[8],"  |")
   print("|       |       |       |")
   print("+-------+-------+-------+")
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision

def EnterMove(board):
    n=int(input("Enter your move: "))
    if n>9:
        print("Invalid Input")
        EnterMove(board)
    elif board[n-1]=="X" or board[n-1]=="O":
        print("Place Already occupied")
        EnterMove(board)
    else:
        board[n-1]="O"
        
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers

def MakeListOfFreeFields(board):
    for i in board:
        if type(i)==int:
            Free.apprnd(i)

# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game

def VictoryFor(board, sign):
    count=0
    for k in range(9):
            if type(board[k])==int:
                count+=1
    if board[0]==board[1]==board[2]=="O" or board[3]==board[4]==board[5]=="O" or \
    board[6]==board[7]==board[8]=="O" or board[0]==board[4]==board[8]=="O" or \
    board[2]==board[4]==board[6]=="O" or board[0]==board[3]==board[6]=="O" or board[1]==board[4]==board[7]=="O" or board[2]==board[5]==board[8]=="O":
        print("Congratulations! You Won")
        a=input("Enter 'exit' to escape the game: ")
        if a=="exit":
            exit()
    elif board[0]==board[1]==board[2]=="X" or board[3]==board[4]==board[5]=="X" or \
    board[6]==board[7]==board[8]=="X" or board[0]==board[4]==board[8]=="X" or \
    board[2]==board[4]==board[6]=="X" or board[0]==board[3]==board[6]=="X" or board[1]==board[4]==board[7]=="X" or board[2]==board[5]==board[8]=="X":
        print("Computer Wins!")
        a=input("Enter 'exit' to escape the game or 'y' to restart: ")
        if a=="exit":
            exit()
        elif a=="y":
            board=[1,2,3,4,5,6,7,8,9]
            DrawMove(board,count2)
            for i in range(2,10):
                if i%2==0:
                    EnterMove(board)
                    VictoryFor(board, sign)
                else:
                    DrawMove(board,count2)
                    VictoryFor(board, sign)
    elif count==0:
        print("Game ends with a Tie.....")
        a=input("Enter 'exit' to escape the game: ")
        if a=="exit":
            exit()
# the function draws the computer's move and updates the board

def DrawMove(board,count2):
    if type(board[4])==int:
        board[4]="X"
        count2=0
        print(DisplayBoard(board))
    elif type(board[lst1[count2]])==int:
        board[lst1[count2]]="X"
        count2+=1
        print(DisplayBoard(board))
    else:
        count2=((count2+1)%8)
        DrawMove(board,count2)
#Main function starts below

DrawMove(board,count2)
for i in range(2,10):
    if i%2==0:
        EnterMove(board)
        VictoryFor(board, sign)
    else:
        DrawMove(board,count2)
        VictoryFor(board, sign)