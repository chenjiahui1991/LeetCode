class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.tmp = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while len(self.queue) > 0:
            self.tmp.append(self.queue.pop())
        self.queue.append(x)
        while len(self.tmp) > 0:
            self.queue.append(self.tmp.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())

