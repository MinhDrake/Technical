# the secret key is: always maintain the root node as the new one and pop that root
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.data = None

    def is_empty(self):
        return self.data == None

    def push(self, data):
        new_node = Node(data)
        if self.data is None:
            self.data = new_node
        else:
            new_node.next = self.data
            self.data = new_node

    def pop(self):
        if self.data is None:
            return None
        popped_node = self.data
        self.data = self.data.next
        return popped_node.data

    def peek(self):
        if self.data is None:
            return None
        return self.data.data


solution = Solution()
solution.push(10)  # set root is 10
solution.push(20)  # set new root is 20
solution.push(30)  # set new root is 30

print(solution.pop())  # Output: 30 - Last in first out
print(solution.peek())  # Output: 20
print(solution.is_empty())  # Output: False
