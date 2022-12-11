def isSafe():
    pass
def swapString(string,s,e):
    lst = list(string)
    lst[s],lst[e] = lst[e],lst[s]
    return ''.join(lst)

def isSafe(string,l,r,i):
    if l!=0 and string[l-1] == 'A' and  string[i] == 'B':
        return False
    if r==l+1 and string[i] == 'A' and string[l] == 'B':
        return False
    return True


def permutationExceptAb(string,l,r):

    if l==r:
        print(string)
        return
    
    for i in range(l,r+1):
        if isSafe(string,l,r,i):
            string = swapString(string,l,i)
            permutationExceptAb(string,l+1,r)
            string = swapString(string,l,i) 

#  ------------------- rat mage problem ---------------
def printMatrix(mat):
    for i in mat:
        print()
        for j in i:
            print(j,end=' ')
def ratInMage(mat:list[list]):
    n = len(mat)
    sol = [[0 for _ in range(n)] for _ in range(n)]
    if ratInMageRec(0,0,n,sol,mat):
        printMatrix(sol)
        return True
    return False

def ratInMageRec(i,j,n,sol,mat):
    if i == n-1 and j == n-1:
        # destination is reached
        sol[i][j] = 1
        return True
    # backtracking safe condition
    if i < n and j < n and mat[i][j] == 1:
        sol[i][j] = 1
        if ratInMageRec(i+1,j,n,sol,mat):
            return True
        if ratInMageRec(i,j+1,n,sol,mat):
            return True
        # if code reached here means no path is possible
        sol[i][j] = 0
    return False


# -------------- n queens ------------
# place n queens so they do not attack each other
def nQueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solveNqueens(board,0):
        printMatrix(board)
        return True
    print('not possible to place n queens')
    return False

def isSafeForQueen(mat,row,col):
    n = len(mat)
    # row check 
    for i in range(col):
        if mat[row][i]==1:
            return False
    # first upper diagonal, because there is nothing on right side
    i,j = row,col
    while i>= 0 and j >= 0:
        if mat[i][j] == 1:
            return False
        i-=1
        j-=1
    i,j = row,col
    while i <n and j >=0:
        if mat[i][j] ==1 : 
            return False
        i+=1
        j-=1
    return True


def solveNqueens(board,col):
    n = len(board)
    if col == n:
        # printMatrix(board)
        # print('------------------------')
        return True
    # try for all rows in current column
    for i in range(n):
        if isSafeForQueen(board,i,col):
            board[i][col] = 1
            if solveNqueens(board,col+1):
                return True
            board[i][col] = 0
    return False
            

mat = [[1,0,1],[1,1,0],[0,1,1]]
string = 'ABC'
# permutationExceptAb(string,0,len(string)-1)
# ratInMage(mat)
nQueens(8)

