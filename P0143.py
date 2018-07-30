# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        point = head
        line = []
        while point != None:
            line.append(point)
            point = point.next
        line.pop(0)
        point = head
        head.next = None
        now = -1
        while len(line) > 0:
            tmp = line.pop(now)
            point.next = tmp
            tmp.next = None
            now = -1 - now
            point = tmp


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
s = Solution()
s.reorderList(root)
while root != None:
    print(root.val)
    root = root.next
