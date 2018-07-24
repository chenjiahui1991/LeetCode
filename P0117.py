# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def dfs(self, node, deep):
        if deep in self.mem:
            self.mem[deep].next = node
        self.mem[deep] = node
        if node.left is not None:
            self.dfs(node.left, deep + 1)
        if node.right is not None:
            self.dfs(node.right, deep + 1)

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        self.mem = dict()
        self.dfs(root, 0)

root = TreeLinkNode(1)
s = Solution()
print(s.connect(root))
