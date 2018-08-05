from utils import constructList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        def dfs(node):
            if node.next is None:
                return node, node
            last, head = dfs(node.next)
            last.next = node
            node.next = None
            return node, head
        return dfs(head)[1]


l = constructList([1, 2, 3, 4, 5])
s = Solution()
l = s.reverseList(l)
while l is not None:
    print(l.val)
    l = l.next

