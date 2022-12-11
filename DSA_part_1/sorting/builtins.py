from functools import cmp_to_key

# -------------------------------------- PRIMITIVE SORTING WITH CUSTOM COMPARATOR
def comparator(a,b):
    return a%2 - b%2

def evenOddSort(arr):
    # reversed
    return sorted(arr,key=cmp_to_key(lambda a,b: 0 if b == a else 1 if a < b else -1 ))

# -------------------------------------- ( NON ) PRIMITIVE SORTING WITH CUSTOM COMPARATOR
class Point:
    def __init__(self,x,y) -> None:
        self.x =  x
        self.y = y
    def __str__(self) -> str:
        return '( '+ str(self.x) + ' , ' + str(self.y) + ')'
        
listOfPoints = []
listOfPoints.append(Point(5,2))
listOfPoints.append(Point(3,8))
listOfPoints.append(Point(1,2))
listOfPoints.append(Point(8,7))

def sortPoints(points):
    return [ str(item) for item in  sorted(points,key= cmp_to_key(lambda point1,point2: 1 if point1.x > point2.x else 0 if point1.x == point2.x else -1 ))]

myArr = [1,2,3,4,5,6,7,8]
print('reverse is : ',evenOddSort(myArr))
# print('sorted points : ',sortPoints(listOfPoints))