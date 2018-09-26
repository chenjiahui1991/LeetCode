from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        wordDict1 = defaultdict(lambda :0)
        wordDict2 = defaultdict(lambda :0)
        words1 = A.split()
        for word in words1:
            wordDict1[word] += 1
        words2 = B.split()
        for word in words2:
            wordDict2[word] += 1
        result = []
        for word in wordDict1:
            if wordDict1[word] == 1 and word not in wordDict2: result.append(word)
        for word in wordDict2:
            if wordDict2[word] == 1 and word not in wordDict1: result.append(word)
        return result

s = Solution()
print(s.uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(s.uncommonFromSentences("apple apple", ""))
