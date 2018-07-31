# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getSize(node):
            result = 0
            while node is not None:
                result += 1
                node = node.next
            return result
        sizeA = getSize(headA)
        sizeB = getSize(headB)
        point1 = headA
        point2 = headB
        if sizeA > sizeB:
            for i in range(sizeA - sizeB):
                point1 = point1.next
        else:
            for i in range(sizeB - sizeA):
                point2 = point2.next
        while point1 is not None and point2 is not None and point1 != point2:
            point1 = point1.next
            point2 = point2.next
        if point1 is None: return None
        return point1




headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headB = ListNode(4)
headB.next = headA.next
s = Solution()
print(s.getIntersectionNode(headA, headB).val)
