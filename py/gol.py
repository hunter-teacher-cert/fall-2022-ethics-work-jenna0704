# Game of Life
# Jenna Lin
# CSCI 77800 Fall 2022
# collaborators: 
# consulted:

dead = '-'
alive = 'X'

# print the board to the terminal
def printBoard(board):
    for row in board:
        for col in row:
            print(col, end = " ")
        print()


# create, initialize, and return  empty board (all cells dead)
def createNewBoard(rows, cols):
    board = [[dead for i in range(cols)] for j in range(rows)]    
    return board
  
  
# set cell (r,c) to val
def setCell(board, r, c, val):
    board[r][c] = val
    

# return number of living neigbours of board[r][c]
def countNeighbours(board, r, c):
    numOfNeighbours = 0
    i = max(0, r - 1)
    while i <= min(r + 1, len(board) - 1):
        j = max(0, c - 1)
        while j <= min(c + 1, len(board[0]) - 1):
            if not(i == r and j == c) and board[i][j] == alive:
                numOfNeighbours += 1
            j += 1
        i += 1
        
    return numOfNeighbours
                
           
# precond: given a board and a cell
# postcond: return next generation cell state based on CGOL rules
def getNextGenCell(board, r, c):
    counts = countNeighbours(board, r, c)
    
    if board[r][c] == alive:
        if counts == 2 or counts == 3:
            return alive
        else:
            return dead
    else:
        if counts == 3:
            return alive
        else:
            return dead
    
    

# generate and return a new board representing next generation
def generateNextBoard(board):
    nextBoard = createNewBoard(len(board), len(board[0]))
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[0]):
            nextBoard[i][j] = getNextGenCell(board, i, j)
            j += 1
        i += 1
           
    return nextBoard



# Testing
board = createNewBoard(5, 5)

setCell(board, 0, 0, alive)
setCell(board, 0, 1, alive)
setCell(board, 1, 0, alive)


print('Gen X: ')        
printBoard(board)
print('---------------------------------------')

board = generateNextBoard(board)

print('Gen X + 1: ')        
printBoard(board)
print('---------------------------------------')
