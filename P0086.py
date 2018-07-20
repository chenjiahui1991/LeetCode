# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = None
        right = None
        if head == None:
            return None
        current = head
        while current != None:
            if current.val >= x:
                if right == None:
                    right = current
                    lastRight = right
                    current = current.next
                    lastRight.next = None
                else:
                    lastRight.next = current
                    lastRight = current
                    current = current.next
                    lastRight.next = None
            else:
                if left == None:
                    left = current
                    lastLeft = left
                    current = current.next
                    lastLeft.next = None
                else:
                    lastLeft.next = current
                    lastLeft = current
                    current = current.next
                    lastLeft.next = None
        if left != None:
            lastLeft.next = right
            return left
        else:
            return right

nums = [1, 4, 3, 2, 5, 2]
list = ListNode(nums[0])
point = list
for i in range(1, len(nums)):
    point.next = ListNode(nums[i])
    point = point.next
s = Solution()
list = s.partition(list, 3)
while list != None:
    print(list.val)
    list = list.next
