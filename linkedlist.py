# This is a comment.

class Node:
    
    def __init__(self, data):
        self.val = data
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        node = Node(val)
        if not self.head:
            self.head = node
        elif index <= 0:
            node.next = self.head
            self.head = node
        else:    
            currentNode = self.head
            previousNode = None
            for i in range(index):
                if currentNode is None:
                    return
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = node
            node.next = currentNode
        self.size += 1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        return

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        return

    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1
        
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.next
        return currentNode.val

    def deleteAtIndex(self, index: int):
        if index < 0 or index > self.size - 1:
            return
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
            
        currentNode = self.head
        previousNode = None
        for i in range(index):
            previousNode = currentNode
            currentNode = currentNode.next
        previousNode.next = currentNode.next
        self.size -= 1
        
