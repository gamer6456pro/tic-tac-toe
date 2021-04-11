import random
import sys
boardtop=[' ',' ',' ']
boardmiddle=[' ',' ',' ']
boardbottom=[' ',' ',' ']
XorO=''
TurnForAI=''
board=[boardtop,boardmiddle,boardbottom]
#turn =X or 0
class AImove():
    def __init__(self,turn):
        self.turn=turn
    def CheckForTwoInARow(self):
        TwoInARowChecker=[]
        Row=''
        column=''
        #check for 2 in a row horizontal
        for x in [boardtop,boardmiddle,boardbottom]:
            TwoInARowChecker.clear()
            for y in range(3):
                if x[y]!=' ':
                    TwoInARowChecker.append(x[y])
                    if len(TwoInARowChecker)==2 and len(set(TwoInARowChecker))==1:
                        Row=x
        if Row not in [boardtop,boardmiddle,boardbottom]:
            #check verticle
            TwoInARowChecker.clear()
            for x in range(3):
                for y in [boardtop,boardmiddle,boardbottom]:
                    if y[x]!=' ':
                        TwoInARowChecker.append(y[x])
                        if len(TwoInARowChecker)==2 and len(set(TwoInARowChecker))==1:
                            
                            column=x
        elif Row in [boardtop,boardmiddle,boardbottom]:
            for x in range(3):
                if Row[x]==' ':
                    Row[x]=self.turn
                    return 'played'
        if not isinstance(column,int):
            #diagonal check
            i=4
            for x in [0,2]:
                TwoInARowChecker.clear()
                i-=2
                if boardtop[x]!=' ':
                    TwoInARowChecker.append(boardtop[x])
                if boardmiddle[1]!=' ':
                    TwoInARowChecker.append(boardmiddle[1])
                if boardbottom[i]!=' ':
                    TwoInARowChecker.append(boardbottom[i])
                #left diagonal=0  right diagonal=2
                if len(TwoInARowChecker)==2 and len(set(TwoInARowChecker))==1:
                    if boardtop[x]==' ':
                        boardtop[x]=self.turn
                    elif boardmiddle[1]==' ':
                        boardmiddle[1]==self.turn
                    elif boardbottom[i]==' ':
                        boardbottom[i]=self.turn
                    return 'played'
        elif isinstance(column,int):
            for x in [boardtop,boardmiddle,boardbottom]:
                if x[column]==' ':
                    x[column]=self.turn
                    return 'played'
        else:
            return
    def AIhardmode(self):
        global boardtop
        global boardmiddle
        global boardbottom
        global board
        corners=['00','02','20','22']
        edges=['01','10','12','21']
        if self.CheckForTwoInARow()=='played':
            return
        if boardmiddle[1]==' ':
            boardmiddle[1]=self.turn
            return
        for i,x in enumerate(corners):
            ycoord=x[0]
            xcoord=x[1]
            ycoord=int(ycoord)
            xcoord=int(xcoord)
            if board[ycoord][xcoord]!=' ':
                del corners[i]
            # -----> this doesn't work for some reason 
        if len(corners)!=0:
            while True:
                for x in corners:
                    ycoord=x[0]
                    xcoord=x[1]
                    ycoord=int(ycoord)
                    xcoord=int(xcoord)
                    choice=random.randint(0,1)
                    if choice==1:
                        board[ycoord][xcoord]=self.turn
                        return
        else:
            while True:
                for x in edges:
                    if x!=' ':
                        continue
                    else:
                        ycoord=x[0]
                        xcoord=x[1]
                        ycoord=int(ycoord)
                        xcoord=int(xcoord)
                        choice=random.randint(0,1)
                        if choice==1:
                            board[ycoord][xcoord]=self.turn
                            return
    # -----> recode hardmode ai corners and edges without using board indexes in the corner and edge lists cuz they 
    # ----->   aren\'t references 


    def AInormalmode(self):
        global boardtop
        global boardmiddle
        global boardbottom
        global board
        if self.CheckForTwoInARow()=='played':
            return
        else:
            for I,x in enumerate(board):
                for J,y in enumerate(x):
                    if y==' ':
                        ChanceToPlay=random.randint(0,1)
                        if ChanceToPlay==0:
                            continue
                        else:
                            board[I][J]=self.turn
                            return 
                    elif I*J==9:
                        board[I][J]=self.turn
                        return 
                    else:
                        continue





#prints the board so that it looks good
def printboard():   
    global boardtop
    global boardmiddle
    global boardbottom
    printboard=[]
    printboard.append('|'.join(boardtop))
    printboard.append('|'.join(boardmiddle))
    printboard.append('|'.join(boardbottom))
    return'\n-+-+-\n'.join(printboard)+'\n'
    
    

#checks if there is 3 in a row on the board
# -----> Diagonal check kinda sucks idk why but fix it 
def winboard():
    ThreeInARowChecker=[]
    for x in [boardtop,boardmiddle,boardbottom]:
        ThreeInARowChecker.clear()
        for y in range(3):
            if x[y]!=' ':
                ThreeInARowChecker.append(x[y])
                if len(ThreeInARowChecker)==3 and len(set(ThreeInARowChecker))==1:
                    Type=ThreeInARowChecker[0]
                    #return True,Type
                    return True,'horizontal'
                
            
    for x in range(3):
        ThreeInARowChecker.clear()
        for y in [boardtop,boardmiddle,boardbottom]:
            if y[x]!=' ':
                ThreeInARowChecker.append(y[x])
                if len(ThreeInARowChecker)==3 and len(set(ThreeInARowChecker))==1:
                    Type=ThreeInARowChecker[0]
                    #return True,Type
                    return True,'verticle'
           
    #check diagonal
    i=4
    for x in [0,2]:
        ThreeInARowChecker.clear()
        i-=2
        if boardtop[x]!=' ':
            ThreeInARowChecker.append(boardtop[x])
        if boardmiddle[1]!=' ':
            ThreeInARowChecker.append(boardmiddle[1])
        if boardbottom[i]!=' ':
            ThreeInARowChecker.append(boardbottom[i])
        
        if len(ThreeInARowChecker)==3 and len(set(ThreeInARowChecker))==1:
            Type=ThreeInARowChecker[0]
            return True,Type

    
    #check draw
    drawCheck=[]
    for x in [boardtop,boardmiddle,boardbottom]:
        for y in x:
            if y!=' ':
                drawCheck.append(y)
            if len(drawCheck)==9:
                return 'draw',None
    return False,None

                

    

class user():
    def __init__(self,XorO):
        self.XorO=XorO
    def userinput(self):
        global boardtop
        global boardmiddle
        global boardbottom
        while True:
            board=[boardtop,boardmiddle,boardbottom]
            
            usermove=input('''Your turn! The moves are abbreviated so that only the first letter of each word act as x and y.\nEx. You want to play the top left corner. You would input TL. Ex.2 You want to play the middle square. You would input MM\n''')
            usermove=usermove.lower()
            if len(usermove)>2:
                usermove=input('Please input a valid move!\n')
                continue
            try:
                boardy='tmb'.index(usermove[0])
                boardx='lmr'.index(usermove[1])
                if board[boardy][boardx]!=' ':
                    print('That square is already taken!\n')
                    continue
                elif board[boardy][boardx]==' ':
                    board[boardy][boardx]=XorO
                    return
            except:
                print('The input is not valid!')
                continue

def turnsystem(typeOfTurn):
    global TurnForAI
    global XorO
    turns=['X','O']
    if typeOfTurn=='F':
        XorO=turns[0]
        TurnForAI=turns[1]
    elif typeOfTurn=='S':
        XorO=turns[1]
        TurnForAI=turns[0]
    elif typeOfTurn=='R':
       TurnForAI=random.choice(turns)
       index=turns.index(TurnForAI)-1
       XorO=turns[index]

    





mode=input('Welcome to tic-tac-toe!\nChoose the difficulty for the computer:\n[N]ormal  [H]ard')
while True:
    if mode=='N':
        while True:
            turn=input('Great! Would you like to play going first (X) or second (O).\nOr do you want it to be random?\n[F]irst  [S]econd  [R]andom\n')
            if turn!='F'and turn!='S'and turn!='R':
                print('Please input a valid input!\n')
                continue
            turnsystem(turn)
            order=[AImove(TurnForAI),user(XorO)]
            if TurnForAI=='O':
                order.reverse()
            while True:
                for x in order: 
                    print(printboard())
                    boardwin,WhoWon=winboard()
                    if boardwin==True:
                        print(WhoWon,'has won!')
                        sys.exit()
                    elif boardwin=='draw':
                        print('A draw has been reached!')
                        sys.exit()
                    
                    if type(x) is AImove:
                        x.AInormalmode()
                    else:
                        x.userinput()
    elif mode=='H':
        while True:
            turn=input('Great! Would you like to play going first (X) or second (O).\nOr do you want it to be random?\n[F]irst  [S]econd  [R]andom')
            if turn!='F' and turn!='S' and turn!='R':
                print('Please input a valid input!\n')
                continue
            turnsystem(turn)
            order=[AImove(TurnForAI),user(XorO)]
            if TurnForAI=='O':
                order.reverse()
            while True:
                
                for x in order: 
                    print(printboard())
                    boardwin,WhoWon=winboard()
                    if boardwin==True:
                        print(WhoWon,'has won!')
                        sys.exit()
                    elif boardwin=='draw':
                        print('A draw has been reached!')
                        sys.exit()
                    
                    if type(x) is AImove:
                        x.AIhardmode()
                    else:
                        x.userinput()


                
    
            
    else:
        print('You must select either Normal or Hard mode.\ntype N for normal or H for hard')
        mode=input('Choose a difficulty for the computer:\n[N]ormal [H]ard')
        continue
