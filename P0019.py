# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return
        last = head
        for i in range(n):
            last = last.next
        if last == None:
            return head.next
        point = head
        while last.next != None:
            last = last.next
            point = point.next
        point.next = point.next.next
        return head


s = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)
list = s.removeNthFromEnd(list, 2)
while list != None:
    print(list.val)
    list = list.next

