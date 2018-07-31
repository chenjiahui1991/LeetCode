# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge_sort(head, length):
            if length == 1:
                return head
            m = length // 2
            point = head
            for i in range(m - 1): point = point.next
            head2 = point.next
            point.next = None
            head1 = merge_sort(head, m)
            head2 = merge_sort(head2, length - m)
            if head1.val <= head2.val:
                result = head1
                point1 = head1.next
                point2 = head2
            else:
                result = head2
                point1 = head1
                point2 = head2.next
            last = result
            last.next = None
            while point1 is not None or point2 is not None:
                if point2 is None or (point1 is not None and point1.val < point2.val):
                    last.next = point1
                    last = point1
                    point1 = point1.next
                    last.next = None
                else:
                    last.next = point2
                    last = point2
                    point2 = point2.next
                    last.next = None
            return result

        if head is None: return None
        n = 0
        point = head
        while point is not None:
            n += 1
            point = point.next
        return merge_sort(head, n)


head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)

s = Solution()
head = s.sortList(head)
while head is not None:
    print(head.val)
    head = head.next
