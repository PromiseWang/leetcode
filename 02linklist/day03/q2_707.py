from utils.linklist.linklist import print_linklist


class ListNode:
    def __init__(self, val=-1):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.length = 0
        self.strategies = {
            "addAtHead": self.addAtHead,
            "addAtTail": self.addAtTail,
            "addAtIndex": self.addAtIndex,
            "get": self.get,
            "deleteAtIndex": self.deleteAtIndex
        }

    def get(self, index: int) -> int:
        p = self.head
        if index >= self.length:
            return -1
        for i in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode()
        new_head.next = self.head
        new_head.val = val
        self.length += 1
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        p = self.head
        new_node = ListNode()
        new_node.val = val
        new_node.next = None
        for i in range(self.length - 1):
            p = p.next
        p.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index >= self.length:
            return
        new_node = ListNode()
        new_node.val = val
        p = self.head
        for i in range(index - 1):
            p = p.next
        new_node.next = p.next
        p.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        new_head = ListNode()
        new_head.next = self.head
        p = new_head

        if index >= self.length:
            return
        elif index == self.length - 1:
            for i in range(index - 1):
                p = p.next
            p.next = None
        elif index > 0:
            for i in range(index):
                p = p.next
            p.next = p.next.next
        else:
            self.head = None
        self.length -= 1

    def execute(self, action, *args):
        return self.strategies[action](*args)


actions = ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead",
           "addAtTail", "get", "addAtHead", "addAtIndex", "addAtHead"]
values = [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]
linklist = MyLinkedList()
for action, val in zip(actions[1:], values[1:]):
    result = linklist.execute(action, *val)
    print(result)
