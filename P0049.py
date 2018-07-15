class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mem = dict()
        for str in strs:
            key = sorted(str)
            key = "".join(key)
            if key in mem:
                mem[key].append(str)
            else:
                mem[key] = [str]
        result = []
        for key in mem:
            result.append(mem[key])
        return result


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
