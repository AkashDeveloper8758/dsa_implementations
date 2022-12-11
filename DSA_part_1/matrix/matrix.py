from numpy import mat


def snakePattern(arr):
    isReverse = True
    n = len(arr)
    for i in range(n):
        isReverse = not isReverse
        m = len(arr[i])
        for j in range(m):
            if isReverse:
                print(arr[i][m-j-1],end=' ')
            else:
                print(arr[i][j],end=' ')

def boundaryTraversal(arr):
    n = len(arr)
    m = len(arr[0])
    if n == 1:
        for i in range(m):
            print(arr[0][i],end=' ')
        return
    if m == 1:
        for i in range(n):
            print(arr[i][0],end=' ')
        return

    # top
    for i in range(m):
        print(arr[0][i],end=' ')
    # right
    for i in range(1,n):
        print(arr[i][m-1],end=' ')
    # bottom
    for i in range(1,m):
        print(arr[n-1][m-i-1],end=' ')
    # left
    for i in range(1,n-1):
        print(arr[n-i-1][0],end=' ')

# transpose of a square matrix
def transposeOfMatrix(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    print(arr)


# efficient solution require no extra space
# idea is : find transpose then reverse row like 1 -> 4, 2 -> 3 
# ANTICLOCKWISE
def rotationOfMatrixAntiClock(mat):
    n = len(mat)
    # transpose
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    # reverse row for anti clockwise
    for i in range(n//2):
        mat[i],mat[n-i-1] = mat[n-i-1],mat[i]
    printmatrix(mat)

# CLOCKWISE, column swap after transpose
def rotationOfMatrixClockwise(mat):
    n = len(mat)
    # transpose
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    # reverse column for clockwise
    for i in range(n):
         for j in range(n//2):
             mat[i][j],mat[i][n-j-1] = mat[i][n-j-1],mat[i][j]
    printmatrix(mat)

def printmatrix(mat):
    n = len(mat)
    for i in range(n):
        print()
        for j in range(n):
            print(mat[i][j],end=' ')
    


# snakePattern([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# boundaryTraversal([
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16]])

# transposeOfMatrix([
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16]])


# rotationOfMatrixAntiClock([
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16]])

print()
print('--------------------------')

rotationOfMatrixClockwise([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]])

