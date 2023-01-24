class Solution:
    def checkMaxPossible(self,arr,m,maxVal):
        sumv =0 
        n= len(arr)
        x = 0
        for i in range(n):
            if arr[i] > maxVal:
                return False
            if arr[i]  + sumv > maxVal:
                sumv = arr[i]
                x+=1
                if x > m:
                    return False
            else:
                sumv += arr[i]
        return True
        
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        sumv = 0
        res =0 
        for item in A:
            sumv += item
        low = 0
        high = sumv
        while low <= high:
            mid= low + (high - low)//2
            if self.checkMaxPossible(A,M,mid):
                res = mid
                high= mid-1
            else:
                low= mid+1
        return res
        

sol = Solution()

arr1 = [12,34,67,90]
arr2 = [13,31,37,45,46,54,55,63,73,84,85]
print('kth element : ',sol.findPages(arr2,len(arr2),9))
# print('kth element : ',sol.checkMaxPossible(arr2,9,72))
# print('----------')
# print('shell sort : ',shellSort(arr,len(arr)))