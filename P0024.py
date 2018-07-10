# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        result = head.next
        cur = head.next.next
        head.next.next = head
        head.next = None
        last = head
        while cur != None:
            sec = cur.next
            if sec == None:
                last.next = cur
                return result
            tmp = sec.next
            sec.next = cur
            cur.next = None
            last.next = sec
            last = cur
            cur = tmp
        return result



s = Solution()
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)
list = s.swapPairs(list)
while list != None:
    print(list.val)
    list = list.next

