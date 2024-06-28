from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self, nums: List):
        self.length = 0
        self.head = ListNode()
        n = len(nums)
        p = self.head
        for i in range(n - 1):
            p.val = nums[i]
            p.next = ListNode()
            p = p.next
            self.length += 1
        p.val = nums[-1]
        p.next = None
        self.length += 1

    def print(self):
        p = self.head
        print(f"链表长度 = {self.length}")
        while p is not None:
            print(p.val)
            p = p.next


def print_linklist(node):
    p = node
    while p:
        print(p.val, end=' -> ')
        p = p.next
    print('None')