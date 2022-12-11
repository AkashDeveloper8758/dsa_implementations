from bisect import bisect_right as upper_bound
def spiralTraversal(mat):
    # we maintain 4 variables
    n = len(mat)
    m = len(mat[0])

    top = 0
    bottom = n-1
    left = 0
    right = m-1
    count = 0
    
    while top <= bottom and left <= right:
        count+=1
        # top traversal from :  left to right
        for i in range(left,right+1):
            print(mat[top][i],end=' ')
        top+=1

        # right traversal from : top to bottom
        for i in range(top,bottom+1):
            print(mat[i][right],end=' ')
        right -=1
        if top<=bottom:
            # bottom traversal from :  right to left (reversed)
            for i in range(right,left-1,-1):
                print(mat[bottom][i],end=' ')
            bottom-=1
        if left<=right:
            # left traversal from : bottom to top
            for i in range(bottom,top-1,-1):
                print(mat[i][left],end=' ')
            left +=1
    print('')
    print('top,bottom,right,left: ',[top,bottom,right,left,count])

def binarySearch(arr,ele):
    n = len(arr)
    high = n-1
    low = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid
        if arr[mid] > ele:
            high = mid-1
        else:
            low = mid+1
    return -1

# time : O(nlog(n))
def searchInRowSortedMatrix(mat,ele):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        index = binarySearch(mat[i],ele)
        if index != -1:
            return [i,index]
    return -1

# if both row and column is sorted, time: O(R+C)
def searchInRowColumnSortedMatrix(mat,ele):
    n = len(mat)
    m = len(mat[0])
    i,j = 0,m-1
    while i<n and j>0:
        if mat[i][j] == ele:
            return [i,j]
        elif mat[i][j] > ele:
            # if element is smaller then mat[i][j] : move left
            j-=1
        else:
            # else move down
            i+=1
    return -1

def customBinarySearch(arr,ele):
    n = len(arr)
    high = n-1
    low = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid+1
        if arr[mid] > ele:
            high = mid-1
        else:
            low = mid+1
    return mid+1

def medianOfRowSoretedMat(mat):
    n = len(mat)
    m = len(mat[0])
    minV = mat[0][0]
    maxV = mat[0][m-1]

    # find min and max from first column and last column resp. 
    for i in range(n):
        minV = min(minV,mat[i][0])
        maxV = max(maxV,mat[i][m-1])
    median = (n*m+1)//2
    while minV < maxV:
        mid = (minV+maxV)//2
        midPos = 0
        for i in range(n):
            # midPos += customBinarySearch(mat[i],mid)
            midPos += upper_bound(mat[i],mid)
        if midPos < median:
            minV = mid+1
        else:
            maxV = mid
    return maxV

# print('custom bin search : ',customBinarySearch([1,3,4,6,7,8,12,13],9))


    
# spiralTraversal([
# [6,6,2,28,2],
# [12,26,2,28,7],
# [22,25,3,4,23]])

# print('search mat : ',searchInRowSortedMatrix([
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16]],8))
         
# print('search mat in row/column soreted mat : ',searchInRowColumnSortedMatrix([
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16]],14))

print('median of row soretd mat : ',medianOfRowSoretedMat([
    [1, 3, 5], 
    [2, 6, 9], 
    [3, 6, 9]]))
         
