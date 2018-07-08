# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = None
        rest = 0
        while l1 != None or l2 != None:
            a = 0
            b = 0
            if l1 != None:
                a = l1.val
                l1 = l1.next
            if l2 != None:
                b = l2.val
                l2 = l2.next
            if l == None:
                l = ListNode((a + b + rest) % 10)
                rest = (a + b + rest) // 10
                last = l
            else:
                last.next = ListNode((a + b + rest) % 10)
                rest = (a + b + rest) // 10
                last = last.next
        if rest != 0:
            last.next = ListNode(rest)
        return l



s = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l = s.addTwoNumbers(l1, l2)
while l != None:
    print(l.val)
    l = l.next
