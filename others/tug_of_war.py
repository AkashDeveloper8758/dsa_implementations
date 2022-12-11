'''
print "Practice makes Perfect!"   
Given a set of n integers, divide the set in two subsets of n/2 sizes each such that the
difference of the sum of two subsets is as minimum as possible. If n is even, then sizes 
of two subsets must be strictly n/2 and if n is odd, then size of one subset must be (n-1)/2 
and size of other subset must be (n+1)/2.


 input : {3, 4, 5, -3, 100, 1, 89, 54, 23, 20}
 output : {4, 100, 1, 23, 20} and {3, 5, -3, 89, 54}
 
 m = len(arr)//2 -1
 sumv = totalSum/2
 
 if m==0:
  if minv > sumv:
    minv = sumv
    return True
  return False
 v1 = resc(sumv,n-1,m) 
 v2 = resc(sumv-arr[n-1],n-1,m-1)
 
 
'''


class Solution:
  minv = float('inf')
  res = []
  
  def recSol(self,arr,sumv,res,n,m):
    if n < 0:
      return
    if m == 0:
      if sumv < self.minv:
        self.minv = sumv
        self.res = res[::]
        #print(res)
      return
    
    if sumv < arr[n-1]:
      self.recSol(arr,sumv,res,n-1,m)
      return
    #print([n,m])
    # take current value
    res.append(arr[n-1])
    check = self.recSol(arr,sumv-arr[n-1],res,n-1,m-1)
    res.pop()
    # do not take current value
    self.recSol(arr,sumv,res,n-1,m)
    return False
  
  def solve(self,arr):
    n = len(arr)
    sumv = 0
    for i in range(n):
      sumv += arr[i]
      
    sumv = sumv//2
    print('sum to make : ',sumv)
    m = 0
    if n %2 == 0:
      m = n //2
    else:
      m = n//2 -1
    self.recSol(arr,sumv,[],n,m)
    print(self.res)
    print('minv : ',self.minv)
  
arr = [3, 4, 5, 3, 10,7]
s = Solution()
s.solve(arr)