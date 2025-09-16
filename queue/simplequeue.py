class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        newnode = Node(val)
        if self.rear is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = self.rear.next

    def dequeue(self, pos):
        if self.front is None:  # Check if the queue is empty
            print("Queue is empty, nothing to delete.")
            return

        if pos == 1:  # Deleting the first element
            print("Deleted element is:", self.front.data)
            self.front = self.front.next
            if self.front is None:  # If the queue becomes empty
                self.rear = None
            return

        
        for i in range(1, pos - 1):
            if self.front is None or self.front.next is None:  # Check out-of-bounds
                print("Position out of bounds.")
                return
            self.front = self.front.next

        if self.front.next is None:  # Check if the position is out of bounds
            print("Position out of bounds.")
            return

        print("Deleted element is:", self.front.next.data)
        self.front   = self.front.next.next

        if self.front.next is None:  # If the deleted node was the last node
            self.rear = self.front

    def display(self):
        if self.front is None:  # Check if the queue is empty
            print("Queue is empty.")
            return

        temp = self.front
        while temp is not None:
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")

q = queue()
n = int(input("Enter the size of queue: "))
for i in range(n):
    num = int(input("Enter the number: "))
    q.enqueue(num)

print("Queue elements:")
q.display()

pos = int(input("Enter the position to be deleted: "))
q.dequeue(pos)

print("Queue after deletion:")
q.display()