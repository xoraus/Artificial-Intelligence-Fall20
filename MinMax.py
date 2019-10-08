import numpy as np

def row_win(board, player): 
    for x in range(len(board)): 
        win = True
          
        for y in range(len(board)): 
            if board[x, y] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win)

# Checks whether the player has three 
# of their marks in a vertical row 
def col_win(board, player): 
    for x in range(len(board)): 
        win = True
          
        for y in range(len(board)): 
            if board[y][x] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 
  
# Checks whether the player has three 
# of their marks in a diagonal row 
def diag_win(board, player): 
    win = True
      
    for x in range(len(board)): 
        if board[x][x] != player : 
            win = False
    if board[1][1]==player and board[0][2]==player and board[2][0]==player:
         return True
    return(win) 
  
# Evaluates whether there is 
# a winner or a tie  
def evaluate(board): 
    winner = 0
      
    for player in [1, 2]: 
        if (row_win(board, player) or
            col_win(board,player) or 
            diag_win(board,player)): 
                 
            winner = player 
              
    if np.all(board != 0) and winner == 0: 
        winner = -1
    return winner
MAX, MIN = 1000, -1000 
N,M=0,0
def possibilities(board): 
    l = [] 
      
    for i in range(len(board)): 
        for j in range(len(board)): 
              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l)

def getScore(b, depth):
    if b == 2:
        return 10 - depth
    elif b == 1:
        return depth - 10
    else:
        return 0
u=0
def minimax(board,maximizingPlayer,  
            depth, alpha, beta):  
   
    global u
    x=evaluate(board)
    if x!=0 :
        u=u+1
        return (getScore(x,depth),0,0)  
  
    if maximizingPlayer:  
       
        best = MIN

        poss=possibilities(board)
        nboard=board.copy()
        # Recur for each possible position of board
        for i,j in poss:  
            nboard[i][j]=2
            val,a,b= minimax(nboard,False, depth + 1, alpha, beta)     
            
            if best<val:
                N=j
                M=i
            best = max(best, val)
            alpha = max(alpha, best)  
            nboard[i][j]=0
            # Alpha Beta Pruning  
            if beta <= alpha:  
               break 
            
        return (best,M,N)  
       
    else: 
        best = MAX
        poss=possibilities(board)
        nboard=board.copy()
        #Recur for each possible position of board
        for i,j in poss:  
            nboard[i][j]=1
            val,a,b= minimax(nboard,True, depth + 1, alpha, beta)  
            if best>val:
                N=j
                M=i
            best = min(best, val)  
            beta = min(beta, best)  
            nboard[i][j]=0
            # Alpha Beta Pruning  
            if beta <= alpha:  
               break 
            
        return (best,M,N) 
#b=np.array([[2, 1, 2], [1, 1, 2], [0, 2, 1]])
#print(diag_win(b,1))
#print(minimax(b,True,0,MIN,MAX))
#print(b)


import math
def create():
  board=np.array([[0,0,0],[0,0,0],[0,0,0]])
  return board
def main():
  board=create()
  while evaluate(board)==0:
    pos=int(input("enter your position[0-8]...."))
    xpoint=math.floor(pos/3)
    ypoint=pos%3
    board[xpoint][ypoint]=1
    val,x,y=minimax(board,True,0,MIN,MAX)
    board[x][y]=2
    print(board)
    print("************next move*********\n\n")
  print("RESULT:")
  if evaluate(board)==-1:
    print("MATCH DRAW")
  elif evaluate(board)==1:
    print("YOU WIN")
  elif evaluate(board)==2:
    print("YOU LOSE")
main()
