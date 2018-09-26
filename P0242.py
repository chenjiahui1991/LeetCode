class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        return s == t


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
