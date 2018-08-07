class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.line = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.line.append(0)
        for i in range(len(self.line) - 1, 0 , -1):
            self.line[i] = self.line[i - 1]
        self.line[0] = x


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.line.pop(0)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.line[0]



    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.line) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
# param_3 = obj.top()
# param_4 = obj.empty()

