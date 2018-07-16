# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return
        n = 1
        point = head
        while (point.next != None):
            n += 1
            point = point.next
        k = k % n
        if k == 0:
            return head
        point.next = head
        k = n - k
        point = head
        for i in range(k - 1):
            point = point.next
        result = point.next
        point.next = None
        return result


s = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)
result = s.rotateRight(list, 1)
while result != None:
    print(result.val)
    result = result.next
