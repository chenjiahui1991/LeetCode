class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        newS = '#'.join('$' + s + '%')
        # print(newS)
        p = [0 for col in range(len(newS))]
        p[0] = mid = right = 0
        for i in range(1, len(newS) - 1):
            if i <= right:
                other = mid * 2 - i
                if i + p[other] < right:
                    p[i] = p[other]
                else:
                    p[i] = right - i
                    left = i - p[i] - 1
                    right = right + 1
                    while newS[left] == newS[right]:
                        p[i] = p[i] + 1
                        left = left - 1
                        right = right + 1
                        mid = i
                    right = right - 1
            else:
                p[i] = 0
                left = i - 1
                right = i + 1
                mid = i
                while newS[left] == newS[right]:
                    p[i] = p[i] + 1
                    left = left - 1
                    right = right + 1
                right = right - 1
            # print(newS[i], p[i], mid, right)

        tmp, mid = max((n, i) for i, n in enumerate(p))
        if (mid - tmp) % 2 == 0:
            return newS[mid - tmp: mid + tmp + 1: 2]
        else:
            return newS[mid - tmp + 1: mid + tmp + 1: 2]

s = Solution()
print(s.longestPalindrome("cbbd"))
# print(s.longestPalindrome("cbbd"))

