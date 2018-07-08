class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        mem = dict()
        left = 0
        for i in range(len(s)):
            if s[i] in mem:
                tmp = i - mem[s[i]]
                for j in range(left, mem[s[i]]):
                    del mem[s[j]]
                left = mem[s[i]] + 1
            else:
                tmp = i - left + 1
            mem[s[i]] = i
            if tmp > result:
                result = tmp
        return result




s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("ftmupfnqqtwxyixmga"))
