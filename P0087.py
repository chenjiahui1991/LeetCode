class Solution:
    def isMatch(self, s1, s2):
        if s1 == s2: return True
        for i in range(1, len(s1)):
            left1, right1 = s1[:i], s1[i:]
            left2, right2 = s2[:-i], s2[-i:]
            if sorted(left1) == sorted(right2) and sorted(right1) == sorted(left2):
                if self.isMatch(left1, right2) and self.isMatch(right1, left2):
                    return True
            left2, right2 = s2[:i], s2[i:]
            if sorted(left1) == sorted(left2) and sorted(right1) == sorted(right2):
                if self.isMatch(left1, left2) and self.isMatch(right1, right2):
                    return True
        return False

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False
        return self.isMatch(s1, s2)


s = Solution()
print(s.isScramble("great", "raget"))
