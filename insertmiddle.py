class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:  
    def __init__(self):
        self.head = None

    def insert(self, val):
        """Insert a new node at the end of the list."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_middle(self, pos, val):
        """Insert a new node at a specific position in the list."""
        if pos < 1:
            raise ValueError("Position must be greater than or equal to 1.")
        
        new_node = Node(val)
        
        # Insert at the head if position is 1
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        count = 1
        
        # Traverse to the node just before the desired position
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
        
        if not temp:
            raise ValueError("Position out of bounds.")
        
        # Insert the new node
        new_node.next = temp.next
        temp.next = new_node
    def display(self):
        """Display the linked list."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
list1=LinkedList()
n=int(input("Enter number of nodes:"))
for i in range(n):
    val=int(input("Enter value:"))
    list1.insert(val)   
list1.display()
pos=int(input("Enter position to insert:"))
val=int(input("Enter value to insert:"))    
list1.insert_middle(pos,val)
list1.display()