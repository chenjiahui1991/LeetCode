# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        length = 1
        point = head
        while point.next is not None:
            length += 1
            point = point.next
        if length == 1: return True
        point = head
        next = head.next
        head.next = None
        for i in range(length // 2 - 1):
            tmp = next.next
            next.next = point
            point = next
            next = tmp
        if length % 2 == 1: next = next.next
        while point is not None:
            if point.val != next.val: return False
            point = point.next
            next = next.next
        return True


link = ListNode(1)
link.next = ListNode(2)
link.next.next = ListNode(2)
link.next.next.next = ListNode(1)
s = Solution()
print(s.isPalindrome(link))
