def mergeTwoSortedArray(arr1,arr2):
    i,j = 0,0
    l1,l2 = len(arr1),len(arr2)
    while i< l1 or j < l2:
        if i==l1 or j==l2:
            if i==l1:
                print(arr2[j],end=' ')
                j+=1
            elif j == l2:
                print(arr1[i],end=' ')
                i+=1
        else:
            if arr1[i] <= arr2[j]:
                print(arr1[i],end=' ')
                i+=1
            else:
                print(arr2[j],end=' ')
                j+=1

def intersectionOfTwoSortedArray(a,b):
    i,j = 0,0
    m,n = len(a),len(b)
    while i<m and j<n:
        if i>0 and a[i] == a[i-1]:
            i+=1
            continue
        if a[i] > b[j]:
            j+=1
        elif a[i] < b[j]:
            i+=1
        elif a[i] == b[j]:
            print(a[i],end=' ')
            i+=1
            j+=1

def unionOfSortedArray(arr1,arr2):
    i,j = 0,0
    l1,l2 = len(arr1),len(arr2)
    while i< l1 and j < l2:

        if i > 0 and arr1[i] == arr1[i-1]:
            i+=1
            continue
        if j > 0 and arr2[j] == arr2[j-1]:
            j+=1
            continue

        if arr1[i] < arr2[j]:
            print(arr1[i],end=' ')
            i+=1
        elif arr1[i] > arr2[j]:
            print(arr2[j],end=' ')
            j+=1
        else:
            print(arr1[i],end=' ')
            i+=1
            j+=1
    while i<l1:
        if i > 0 and arr1[i] == arr1[i-1]:
            i+=1
            continue
        print(arr1[i],end=' ')
        i+=1
    while j<l2:
        if j > 0 and arr2[j] == arr2[j-1]:
            j+=1
            continue
        print(arr2[j],end=' ')
        j+=1
    
def countOfInversions(arr):
    n = len(arr)
    count =0
    for i in range(n):
        for j in range(i,n):
            if arr[j] < arr[i]:
                count +=1
    return count        
    

# intersectionOfTwoSortedArray([2,3,4,5,6],[1,3,4,6,7,8,9])
# mergeTwoSortedArray([1,2,3,4,5],[3,4,5,6,7,8,9,10])
# unionOfSortedArray([3,3,4,5,6],[1,2,3,4,4,4,6,7,8,9,9])
print('inversion count : ',countOfInversions([6,5,4,3,2]))


