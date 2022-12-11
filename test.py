class Solution:
    def DFS(self,adj,res,s,visited):
        visited[s] = True
        for c in adj[s]:
            if not visited[c]:
                self.DFS(adj,res,c,visited)
        res.append(s)
        
        
    def findOrder(self,dict, N, K):
        # if N==1:
        adj = [[] for _ in range(K)]
        
        res = []
        for i in range(1,N):
            prev = dict[i-1]
            curr = dict[i]
            minl = min(len(prev),len(curr))
            for j in range(minl):
                if prev[j] != curr[j]:
                    pi = ord(prev[j])-ord('a')
                    ci = ord(curr[j])-ord('a')
                    adj[pi].append(ci)
                    break
        visited = [False for _ in range(K)]
        for i in range(K):
            if not visited[i]:
                self.DFS(adj,res,i,visited)
        sRes = ''
        res.reverse()
        for r in res:
            sRes+= chr(ord('a')+r)
        return sRes
sol = Solution()

mylist =["bhhb", "blkbggfecalifjfcbkjdicehhgikkdhlachlgbhji" ,"cfjjhcifladadbgcleggjgbcieihabcglblflgajgkejccj",
 "dlgdhiha", "ehggedljjhfldcajeceaeehkalkfeidhigkifjl", "gdalgkblahcldahledfghjb",
  "geldbblaaflegjhlfjlgblfbdc", "ibjceciedbiilkjliijgklcgliaeeic", "jcebjkfgfibfckfiikklecihik",
  "jdkcabjjjckgdblkljf", "jijlbjbliigkffhkchkclkhafbiiiblcglhfjkflbjjkih", "kfd", "lhdgidialgabfklffahiihceflebfidl"]

sol = Solution()
response = sol.findOrder(mylist,len(mylist),12)
print('res: ',response)
