from linked_list_implementation import LinkedQueue

# recursive implementation
def reverseAQueue(queue:LinkedQueue):
    if queue.isEmpty():
        return
    # get the front
    x = queue.getFront()
    # then remove it
    queue.dequeue()
    reverseAQueue(queue)
    # add the removed element
    queue.enqueue(x)

def generateNoWithGivenDigits(n):
    queue = LinkedQueue()
    queue.enqueue('5')
    queue.enqueue('6')
    for i in range(n):
        value = queue.getFront()
        print(value,end=' ')
        queue.dequeue()
        queue.enqueue(value+'5')
        queue.enqueue(value+'6')
    

generateNoWithGivenDigits(40)

# queue = LinkedQueue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)

# queue.printQueue()
# reverseAQueue(queue)
# queue.printQueue()