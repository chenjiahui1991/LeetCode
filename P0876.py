# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        point = head
        count = 1
        while point.next != None:
            point = point.next
            count += 1
        n = count // 2
        result = head
        for i in range(n):
            result = result.next
        return result


s = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
# list.next.next.next.next = ListNode(5)
# list.next.next.next.next.next = ListNode(6)
list = s.middleNode(list)
while list != None:
    print(list.val)
    list = list.next

