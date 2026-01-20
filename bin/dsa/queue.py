class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# front -> node -> rear
# enqueue: add new node at rear
# dequeue: remove node from front
class Solution:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        if self.rear is None:
            new_node = Node(data)
            self.rear = new_node
            self.front = new_node
        else:
            new_node = Node(data)
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def pop(self):
        if self.front is None:
            return None
        return self.front.data
