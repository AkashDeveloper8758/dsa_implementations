class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return -1
            
        hashmap = {}
        for i in range(len(p)):
            if p[i] in hashmap:
                hashmap[p[i]] +=1
            else:
                hashmap[p[i]] =1
        resmap = {i: 0 for i in s}
        dist= len(hashmap)
        count,start = 0,0
        res = -1
        for i in range(len(s)):
            resmap[s[i]] +=1
            if s[i] in hashmap and hashmap[s[i]] == resmap[s[i]]:
                count +=1
            if count == dist:
                while s[start] not in hashmap or resmap[s[start]] > hashmap[s[start]]:
                    resmap[s[start]] -=1 
                    start+=1
                if res == -1 or len(res) > i-start + 1:
                    res = s[start:i+1]
        return res



sol = Solution()
s = 'zoomlazapzo'
p = 'ozza'
print('res : ',sol.smallestWindow(s,p))