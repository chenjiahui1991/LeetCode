class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        mem1 = dict()
        mem2 = dict()
        for i in range(len(s)):
            if s[i] not in mem1:
                mem1[s[i]] = t[i]
            else:
                if mem1[s[i]] != t[i]:
                    return False
            if t[i] not in mem2:
                mem2[t[i]] = s[i]
            else:
                if mem2[t[i]] != s[i]:
                    return False
        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
