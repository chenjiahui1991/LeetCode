from utils import constructList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

l = constructList([4, 5, 1, 9])

s = Solution()
s.deleteNode(l.next)
while (l is not None):
    print(l.val)
    l = l.next
