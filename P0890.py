class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def checkPattern(word, pattern):
            if len(word) != len(pattern): return False
            p2w = dict()
            w2p = dict()
            for i in range(len(word)):
                if word[i] in w2p and pattern[i] != w2p[word[i]]: return False
                if pattern[i] in p2w and word[i] != p2w[pattern[i]] : return False
                w2p[word[i]] = pattern[i]
                p2w[pattern[i]] = word[i]
            return True

        result = []
        for word in words:
            if checkPattern(word, pattern): result.append(word)
        return result


s = Solution()
print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
