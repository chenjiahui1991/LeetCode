from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = defaultdict(list)

    def cmp(self, word, pattern):
        if len(word) != len(pattern): return False
        for i in range(len(word)):
            if not(pattern[i] == '.' or word[i] == pattern[i]):
                return False
        return True


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.mem[len(word)].append(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' not in word: return word in self.mem[len(word)]
        for item in self.mem[len(word)]:
            if self.cmp(item, word): return True
        return False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
