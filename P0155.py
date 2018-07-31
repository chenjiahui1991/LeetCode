class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.minValue = float('inf')


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.nums.append(x)
        if x < self.minValue: self.minValue = x


    def pop(self):
        """
        :rtype: void
        """
        tmp = self.nums.pop()
        if tmp == self.minValue:
            self.minValue = float('inf')
            for val in self.nums:
                self.minValue = min(val, self.minValue)


    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minValue


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
