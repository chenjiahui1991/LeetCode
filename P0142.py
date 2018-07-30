# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return None
        fast = head
        slow = head
        first = True
        while fast is not None and fast.next is not None and (first or fast != slow):
            first = False
            fast = fast.next.next
            slow = slow.next
        if fast is None or fast.next is None:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = root.next.next
s = Solution()
print(s.detectCycle(root).val)
