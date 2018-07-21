# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        nodeList = [[root]]
        curLevel = 1
        while len(nodeList[-1]) > 0:
            nodeList.append([])
            result.append([])
            for i in range(len(nodeList[curLevel - 1])):
                result[curLevel - 1].append(nodeList[curLevel - 1][i].val)
                if nodeList[curLevel - 1][i].left != None:
                    nodeList[curLevel].append(nodeList[curLevel - 1][i].left)
                if nodeList[curLevel - 1][i].right != None:
                    nodeList[curLevel].append(nodeList[curLevel - 1][i].right)
            curLevel += 1
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.levelOrder(root))
