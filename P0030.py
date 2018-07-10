class Solution:
    result = []

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []

        self.result = []

        wordLen = len(words[0])
        for i in range(wordLen):
            d = dict()
            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
            count = 0
            left = i
            for j in range(i, len(s) - wordLen + 1, wordLen):
                cur = s[j : j + wordLen]
                if not cur in d:
                    while s[left : left + wordLen] != cur:
                        if s[left : left + wordLen] in d:
                            count = count - 1
                            d[s[left : left + wordLen]] = d[s[left : left + wordLen]] + 1
                            left = left + wordLen
                    left = left + wordLen
                elif d[cur] > 0:
                    count = count + 1
                    d[cur] = d[cur] - 1
                else:
                    while s[left : left + wordLen] != cur:
                        count = count - 1
                        d[s[left : left + wordLen]] = d[s[left : left + wordLen]] + 1
                        left = left + wordLen
                    left = left + wordLen
                if count == len(words):
                    self.result.append(left)
        return sorted(self.result)


s = Solution()
print(s.findSubstring("abaababbaba", ["ba","ab","ab"]))

