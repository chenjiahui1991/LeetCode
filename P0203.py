from utils import constructList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None: return None
        result = head
        while result is not None and result.val == val:
            result = result.next
        if result is None: return None
        last = result
        while True:
            while last is not None and last.next is not None and last.next.val != val:
                last = last.next
            if last is None or last.next is None: return result
            last.next = last.next.next


l = constructList([])
s = Solution()
l = s.removeElements(l, 6)
while l is not None:
    print(l.val)
    l = l.next

