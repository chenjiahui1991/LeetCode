from collections import defaultdict

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def get_next(substr):
            next = [0] * len(substr)
            next[0] = -1
            k = -1
            for j in range(1, len(substr)):
                while k != -1 and substr[k + 1] != substr[j]:
                    k = next[k]
                if substr[k + 1] == substr[j]:
                    next[j] = k + 1
                    k = k + 1
                else:
                    next[j] = k
            return next

        def kmp(str, substr):
            result = []
            if substr == '':
                return result
            next = get_next(substr)
            i = 0
            j = -1
            while i < len(str) and j < len(substr) - 1:
                while j != -1 and str[i] != substr[j + 1]:
                    j = next[j]
                if str[i] == substr[j + 1]:
                    j = j + 1
                i = i + 1
                if j == len(substr) - 1:
                    result.append(i - j - 1)
                    j = next[j] # comment this line for first solution
            return result

        len_dict = defaultdict(list)
        for word in wordDict:
            idx = kmp(s, word)
            for i in idx:
                len_dict[i].append(len(word))
        f = [False for _ in range(len(s))]
        for i in range(len(s)):
            if i == 0 or f[i - 1]:
                for l in len_dict[i]:
                    f[i + l - 1] = True
        return f[-1]


s = Solution()
print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
