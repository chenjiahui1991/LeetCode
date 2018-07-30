# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        point = head
        while point != None:
            if point.next == point:
                return True
            tmp = point.next
            point.next = point
            point = tmp
        return False





root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = root
s = Solution()
print(s.hasCycle(root))
