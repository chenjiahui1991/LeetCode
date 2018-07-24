# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructTree(valueList):
    if len(valueList) == 0:
        return None
    nodeList = [None for _ in range(len(valueList))]
    nodeList[0] = TreeNode(valueList[0])
    for i in range(1, len(valueList)):
        if valueList[i] is None:
            continue
        nodeList[i] = TreeNode(valueList[i])
        if (i - 1) % 2 == 0:
            nodeList[(i - 1) // 2].left = nodeList[i]
        else:
            nodeList[(i - 1) // 2].right = nodeList[i]
    return nodeList[0]


