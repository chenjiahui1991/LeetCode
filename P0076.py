class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mem = dict()
        for ch in t:
            if ch in mem:
                mem[ch] += 1
            else:
                mem[ch] = 1

        result = ''
        minLength = float('inf')
        count = 0
        right = 0
        left = 0
        while right < len(s):
            if s[right] in mem:
                count += mem[s[right]] > 0
                mem[s[right]] -= 1
            if count == len(t):
                while not (s[left] in mem and mem[s[left]] == 0):
                    if s[left] in mem:
                        mem[s[left]] += 1
                        count -= mem[s[left]] > 0
                    left += 1
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    result = s[left : right + 1]
            right += 1
        return result



s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
