# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        mem = dict()
        point = head
        result = RandomListNode(head.label)
        mem[head] = result
        point2 = result
        while point is not None:
            if point.next is not None:
                if point.next not in mem:
                    tmp = RandomListNode(point.next.label)
                    mem[point.next] = tmp
                point2.next = mem[point.next]
            if point.random is not None:
                if point.random not in mem:
                    tmp = RandomListNode(point.random.label)
                    mem[point.random] = tmp
                point2.random = mem[point.random]
            point = point.next
            point2 = point2.next
        return result





root = RandomListNode(1)
root.next = RandomListNode(2)
root.next.next = RandomListNode(3)
s = Solution()
print(s.copyRandomList(root))
