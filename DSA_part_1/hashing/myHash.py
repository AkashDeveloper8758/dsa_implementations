def hashKey(key,size):
    return key%size

class MyHash:
    arr = []
    size = 0
    def __init__(self,cap) -> None:
        self.capacity = cap
        self.arr = [-1 for _ in range(cap)]
    
#  open addressing with linear probing
    def searchKey(self,key):
        h = hashKey(key,self.capacity)
        i = h
        while self.arr[h] != -1:
            if self.arr[i] == key:
                return True
            i = (i+1)%self.capacity 

            # loop is completed, element doesn't exist
            if i == h:
                return False
        return False

    def insertKey(self,key):
        if self.capacity == self.size:
            return False

        i = hashKey(key,self.capacity)
        while self.arr[i] != -1 and self.arr[i] != -2 and self.arr[i] != key:
            i = (i+1)%self.capacity
        
        if self.arr[i] == key:
            # key is already present
            return False
        self.arr[i] = key
        self.size+=1
        return True
        
    def deleteKey(self,key):
        h = hashKey(key,self.capacity)
        i = h
        while self.arr[h] != -1:
            if self.arr[i] == key:
                self.arr[i] = -2
                return True
            i = (i+1)%self.capacity 

            # loop is completed, element doesn't exist
            if i == h:
                return False
        return False
