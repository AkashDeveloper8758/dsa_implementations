class Solution:
    def findTopologicalOrder(self,adjs,visited,stack,s):
        visited[s] = True
        for v in adjs[s]:
            if not visited[v]:
                self.findTopologicalOrder(adjs,visited,stack,v)
        stack.append(s)


    def findOrder(self,dict, N, K):
        graph = [[] for _ in range(K)]

        for i in range(1,N):
            item= dict[i-1]
            sec = dict[i]
            m = min(len(item),len(sec))
            l = 0
            while l < m and item[l] == sec[l]:
                l+=1
            if l < m and item[l] != sec[l]:
                p = ord(item[l]) - ord('a')
                c = ord(sec[l]) - ord('a')
                graph[p].append(c)

        res = []
        visited = [False]*K
        for item in graph:
            print(item)
            print('')
        for item in range(K):
            if not visited[item]:
                self.findTopologicalOrder(graph,visited,res,item)
        res.reverse()
        strv = ''
        for r in res:
            strv += chr(ord("a") +r) 
        return strv

        

# mylist =["baa","abcd","abca","cab","cad"]
# mylist =["caa","aaa","aab"]
mylist =["bhhb", "blkbggfecalifjfcbkjdicehhgikkdhlachlgbhji" ,"cfjjhcifladadbgcleggjgbcieihabcglblflgajgkejccj",
 "dlgdhiha", "ehggedljjhfldcajeceaeehkalkfeidhigkifjl", "gdalgkblahcldahledfghjb",
  "geldbblaaflegjhlfjlgblfbdc", "ibjceciedbiilkjliijgklcgliaeeic", "jcebjkfgfibfckfiikklecihik",
  "jdkcabjjjckgdblkljf", "jijlbjbliigkffhkchkclkhafbiiiblcglhfjkflbjjkih", "kfd", "lhdgidialgabfklffahiihceflebfidl"]


sol = Solution()
response = sol.findOrder(mylist,len(mylist),12)
print('res: ',response)