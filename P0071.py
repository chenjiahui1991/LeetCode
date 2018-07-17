class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        name = ''
        while path != '':
            if '/' in path:
                index = path.index('/')
                name = path[0 : index]
            else:
                index = len(path)
                name = path
            if name == '.' or name == "":
                pass
            elif name == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(name)
            path = path[index + 1:]
        result = ''
        for val in stack:
            result += '/' + val
        if result == '':
            result = '/'
        return result


s = Solution()
print(s.simplifyPath('/home/foo/'))
