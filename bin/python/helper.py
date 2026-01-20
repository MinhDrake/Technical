from typing import Optional


class ListNode:
    def __init__(self, value=0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next


class Helper:
    def print_linked_list(self, list: ListNode | None):
        current = list
        while current:
            print(current.value, end="->")
            current = current.next
        print('End')
