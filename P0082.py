# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getNext(self, head):
        while True:
            if head == None:
                return None
            if head.next == None or head.val != head.next.val:
                return head
            value = head.val
            while head != None and head.val == value:
                head = head.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = self.getNext(head)
        if cur == None:
            return None
        result = ListNode(cur.val)
        last = result
        while True:
            next = self.getNext(cur.next)
            if next == None:
                return result
            last.next = ListNode(next.val)
            last = last.next
            cur = next

nums = [1, 2, 3, 3, 4, 4, 5]
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
