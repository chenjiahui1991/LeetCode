# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        result = head
        last = result
        point = head.next
        while point != None:
            while point != None and point.val == last.val:
                point = point.next
            if point != None:
                last.next = point
                last = last.next
                point = point.next
        last.next = None
        return result

nums = [1, 1, 2]
list = ListNode(nums[0])
point = list
for i in range(1, len(nums)):
    point.next = ListNode(nums[i])
    point = point.next
s = Solution()
list = s.deleteDuplicates(list)
while list != None:
    print(list.val)
    list = list.next
