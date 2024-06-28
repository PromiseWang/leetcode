from typing import Optional

from utils.linklist.linklist import ListNode, LinkList, print_linklist


class Solution(object):
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode()
        new_head.next = head
        p = new_head
        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return new_head.next


s = Solution()
# nums = [1, 2, 3, 4, 5]
# nums = [1, 2, 6, 3, 4, 5, 6]
nums = [7, 7, 7, 7, 7]
linklist = LinkList(nums)
# linklist.print()
head = s.removeElements(linklist.head, 7)
print_linklist(head)
