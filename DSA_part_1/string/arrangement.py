def printAllSubsequence(string,curr,i,arr):
	if i == len(string):
		arr.append(curr)
		return
	# we will not include the character
	printAllSubsequence(string,curr,i+1,arr)
	# we will include the character
	printAllSubsequence(string,curr+string[i],i+1,arr)
	return arr
class Solution:
    def swapFunc(self,s,i,j):
        strlist = list(s)
        strlist[i],strlist[j] = strlist[j],strlist[i]
        return ''.join(strlist)
        
    def find_permu_func(self,S,i,res):
        if i ==len(S)-1:
            # print(S,end=' ')
            res.append(S)
            return
        for j in range(i,len(S)):
            S = self.swapFunc(S,i,j)
            self.find_permu_func(S,i+1,res)
            S = self.swapFunc(S,i,j)
            
    def find_permutation(self, S):
        # Code here
        res = []
        self.find_permu_func(S,0,res)
        res = sorted(res,key=str.lower)
        print('res : ',res)

sol = Solution()
sol.find_permutation('ljr')