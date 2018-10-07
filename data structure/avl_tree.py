import random


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.bf = 0


class AVLTree:
    def __init__(self):
        self.T = None

    def search(self, node, value, pre):
        if node.val == value:
            return True, node, pre
        if (value < node.val and node.left is None) or (value > node.val and node.right is None):
            return False, node, pre
        if value < node.val: return self.search(node.left, value, node)
        else: return self.search(node.right, value, node)

    def r_rotate(self, root):
        p = root.left
        root.left = p.right
        p.right = root
        root = p

    def l_rotate(self, root):
        p = root.right
        root.right = p.left
        p.left = root
        root = p

    def RightBalance(self, root):
        rchild = root.right
        if rchild.bf == 1:
            root.bf = 0
            rchild.bf = 0
            self.l_rotate(root)
            root = root.right
        elif rchild.bf == 0:
            root.bf = 1
            rchild.bf = -1
            self.l_rotate(root)
            root = root.right
        else:
            rlchild = root.right.left
            if rlchild.bf == 0:
                root.bf = 0
                rchild.bf = 0
            elif rlchild.bf == 1:
                root.bf = -1
                rchild.bf = 0
            else:
                root.bf = 0
                rchild.bf = 1
            rlchild.bf = 0
            self.r_rotate(root.right)
            self.l_rotate(root)
            root = root.right




    def insert(self, value):
        if self.T is None:
            self.T = TreeNode(value)
            return True
        is_exist, node, pre = self.search(self.T, value, None)
        if is_exist: return False
        if value < node.val:
            node.left = TreeNode(value)
        else:
            node.right = TreeNode(value)

    def delete(self, value):
        if self.T == None:
            return False
        is_exist, node, pre = self.search(self.T, value, None)
        if is_exist == False: return False
        if pre is not None:
            if node.left is None and node.right is None: # leaf node
                if value < pre.val: pre.left = None
                else: pre.right = None
            if node.left is not None and node.right is None: # only left child
                if value < pre.val: pre.left = node.left
                else: pre.right = node.left
            if node.left is None and node.right is not None: # only right child
                if value < pre.val: pre.left = node.right
                else: pre.right = node.right
            if node.left is not None and node.right is not None: # both children exist
                tmp = node.right
                while tmp.left is not None:
                    tmp = tmp.left
                self.delete(tmp.val)
                node.val = tmp.val
        else:
            if node.left is None and node.right is None: # leaf node
                self.T = None
            if node.left is not None and node.right is None: # only left child
                self.T = node.left
            if node.left is None and node.right is not None: # only right child
                self.T = node.right
            if node.left is not None and node.right is not None: # both children exist
                tmp = node.right
                while tmp.left is not None:
                    tmp = tmp.left
                self.delete(tmp.val)
                node.val = tmp.val

    def inorder(self, node, result):
        if node == None:
            return
        if node.left is not None: self.inorder(node.left, result)
        result.append(node.val)
        if node.right is not None: self.inorder(node.right, result)

    def get_nums(self):
        result = []
        self.inorder(self.T, result)
        return result


# for time in range(1000):
#     bst = BinarySearchTree()
#     nums = []
#     for i in range(100):
#         nums.append(random.randrange(100))
#     for num in nums:
#         bst.insert(num)
#         tmp = bst.get_nums()
#         tmp2 = sorted(tmp)
#         if tmp != tmp2:
#             print('Error!')
#             exit()
#         print(tmp)
#     while len(nums) > 0:
#         idx = random.randrange(len(nums))
#         bst.delete(nums[idx])
#         tmp = bst.get_nums()
#         tmp2 = sorted(tmp)
#         if tmp != tmp2:
#             print('Error!')
#             exit()
#         print(tmp)
#         nums.pop(idx)
import random


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.T = None

    def search(self, node, value, pre):
        if node.val == value:
            return True, node, pre
        if (value < node.val and node.left is None) or (value > node.val and node.right is None):
            return False, node, pre
        if value < node.val: return self.search(node.left, value, node)
        else: return self.search(node.right, value, node)

    def insert(self, value):
        if self.T is None:
            self.T = TreeNode(value)
            return True
        is_exist, node, pre = self.search(self.T, value, None)
        if is_exist: return False
        if value < node.val:
            node.left = TreeNode(value)
        else:
            node.right = TreeNode(value)

    def delete(self, value):
        if self.T == None:
            return False
        is_exist, node, pre = self.search(self.T, value, None)
        if is_exist == False: return False
        if pre is not None:
            if node.left is None and node.right is None: # leaf node
                if value < pre.val: pre.left = None
                else: pre.right = None
            if node.left is not None and node.right is None: # only left child
                if value < pre.val: pre.left = node.left
                else: pre.right = node.left
            if node.left is None and node.right is not None: # only right child
                if value < pre.val: pre.left = node.right
                else: pre.right = node.right
            if node.left is not None and node.right is not None: # both children exist
                tmp = node.right
                while tmp.left is not None:
                    tmp = tmp.left
                self.delete(tmp.val)
                node.val = tmp.val
        else:
            if node.left is None and node.right is None: # leaf node
                self.T = None
            if node.left is not None and node.right is None: # only left child
                self.T = node.left
            if node.left is None and node.right is not None: # only right child
                self.T = node.right
            if node.left is not None and node.right is not None: # both children exist
                tmp = node.right
                while tmp.left is not None:
                    tmp = tmp.left
                self.delete(tmp.val)
                node.val = tmp.val

    def inorder(self, node, result):
        if node == None:
            return
        if node.left is not None: self.inorder(node.left, result)
        result.append(node.val)
        if node.right is not None: self.inorder(node.right, result)

    def get_nums(self):
        result = []
        self.inorder(self.T, result)
        return result


# for time in range(1000):
#     bst = BinarySearchTree()
#     nums = []
#     for i in range(100):
#         nums.append(random.randrange(100))
#     for num in nums:
#         bst.insert(num)
#         tmp = bst.get_nums()
#         tmp2 = sorted(tmp)
#         if tmp != tmp2:
#             print('Error!')
#             exit()
#         print(tmp)
#     while len(nums) > 0:
#         idx = random.randrange(len(nums))
#         bst.delete(nums[idx])
#         tmp = bst.get_nums()
#         tmp2 = sorted(tmp)
#         if tmp != tmp2:
#             print('Error!')
#             exit()
#         print(tmp)
#         nums.pop(idx)
