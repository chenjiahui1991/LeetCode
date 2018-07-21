# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, head, len):
        if len <= 0: return None
        current = len // 2
        point = head
        for i in range(current):
            point = point.next
        result = TreeNode(point.val)
        result.left = self.buildTree(head, current)
        result.right = self.buildTree(point.next, len - current - 1)
        return result

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None: return None
        count = 1
        point = head
        while point.next != None:
            count += 1
            point = point.next
        return self.buildTree(head, count)


list = ListNode(-10)
list.next = ListNode(-3)
list.next.next = ListNode(0)
list.next.next.next = ListNode(5)
list.next.next.next.next = ListNode(9)
s = Solution()
print(s.sortedListToBST(list))
