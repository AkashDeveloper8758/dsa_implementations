from numpy import sort


def activitySelectionProblem(arr:list[list]):
    n = len(arr)
    arr.sort(key=lambda a : a[1])
    prev = 0
    res = 1
    for i in range(1,n):
        if arr[i][0] >= arr[prev][1]:
            prev = i
            res+=1
    return res 

class Item:
    def __init__(self,weight,value):
        self.value = value
        self.weight = weight
    
def fractionalKnapsack(i:list[Item],w):
    i.sort(key=lambda I: -(I.value/I.weight))
    for k in i:
        print(k.value/k.weight)
    res = 0
    for v in i:
        if v.weight <= w:
            res+=v.value
            w-=v.weight
        else:
            res+= (w/v.weight)*v.value
            return res

# --------------- job sequencing ------------- n^2
class Job:
    def __init__(self,deadline,profit):
        self.deadline = deadline
        self.profit = profit

def jobsequencingProblem(jobs:list[Job]):
    maxdeadline = 0
    for i in jobs:
        maxdeadline = max(maxdeadline,i.deadline)
    jobs.sort(key=lambda item: -item.profit)
    arr = [None for _ in range(maxdeadline)]
    for j in jobs:
        if arr[j.deadline-1] == None:
            arr[j.deadline-1] = j.profit
        else:
            i = j.deadline-1
            while i> 0:
                if arr[i] == None:
                    arr[i] = j.profit
                i-=1
    print(arr)
    

jobs = [Job(4,50),Job(1,5),Job(1,20),Job(5,10),Job(5,80)]




items = [Item(10,400),
Item(15,600),Item(30,450),Item(25,200),Item(20,400)]

arr = [[1,3],[4,6],[9,10],[4,8],[7,12]]
# print('activities : ',activitySelectionProblem(arr))
# print('fractional knapsack : ',fractionalKnapsack(items,12))

jobsequencingProblem(jobs)