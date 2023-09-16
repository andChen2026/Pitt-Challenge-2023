# Linked List class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
# Create a LinkedList class
 
 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(data)
        old_node = self.head
        self.head = node
        node.next = old_node

    
