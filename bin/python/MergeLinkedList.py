# give n sorted linked list, merge and product a single increasing linked list.
from typing import List, Optional
from helper import Helper, ListNode
import heapq

# naive mer linked
# given:
# n is size of List[ListNode]
# m1, m2, ... mn is the length of each ListNode

# time complexity: O(m1*(n-1) + m2*(n-2) + m3*(n-3) + mn*1) = O(m*n)
# space complexity: O(1)


def merge_two_listNode(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode(-1)
    current = dummy
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next


def merge_linked_lists_naive(list: List[ListNode]) -> ListNode | None:
    if not list:
        return None
    merged_list = None
    for lst in list:
        merged_list = merge_two_listNode(merged_list, lst)

    return merged_list

# time complexity: O(m*log2n)
# space complexity: O(log2n)
# divide and conquer list


def divide_and_conquer_list(list: List[ListNode]) -> ListNode | None:
    if len(list) == 1:
        return list[0]

    mid = len(list) // 2
    left = divide_and_conquer_list(list[:mid])
    right = divide_and_conquer_list(list[mid:])

    return merge_two_listNode(left, right)


# time complexity: O(m*(logn)) - inserting/ extracting from the heap
# space complexity:O(n) - heap tree
def merge_k_list_priority_queue(list: List[ListNode]) -> ListNode | None:
    if not list:
        return None

    heap = []
    for ele in list:
        if ele:
            heapq.heappush(heap, (ele.value, ele))

    result = ListNode(-1)
    dummy = result
    while heap:
        value, node = heapq.heappop(heap)
        dummy.next = node
        dummy = dummy.next
        node = node.next
        if node:
            heapq.heappush(heap, (node.value, node))

    return result.next


l1 = ListNode(1, ListNode(5))
l3 = ListNode(2, ListNode(6))
l2 = ListNode(3, ListNode(4))
helper = Helper()
# helper.print_linked_list(merge_linked_lists_naive([l1, l2, l3]))
# helper.print_linked_list(divide_and_conquer_list([l1, l2, l3]))
helper.print_linked_list(merge_k_list_priority_queue([l1, l2, l3]))
