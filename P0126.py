from collections import defaultdict

class Solution:
    def dfs(self, deep, nowWord, nextWord, step_list, subset, set):
        if deep == 0:
            set.append(subset[:])
            return
        for word in nextWord[nowWord]:
            if word in step_list and step_list[word] == deep:
                subset.insert(0, word)
                self.dfs(deep - 1, word, nextWord, step_list, subset, set)
                subset.pop(0)

    def getResult(self, nextWord, line, startWord):
        step_list = dict()
        for item in line:
            step_list[item[0]] = item[1]
        result = []
        self.dfs(step_list[startWord] - 1, startWord, nextWord, step_list, [startWord], result)
        return result

    def calcNext(self, wordList):
        groups = defaultdict(list)
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(wordList[i])):
                groups[word[: j] + ' ' + word[j + 1:]].append(word)
        nextWord = defaultdict(list)
        for key in groups:
            group = groups[key]
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    nextWord[group[i]].append(group[j])
                    nextWord[group[j]].append(group[i])
        return nextWord

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if beginWord not in wordList:
            wordList.append(beginWord)
        if beginWord == endWord:
            return [beginWord]
        nextWord = self.calcNext(wordList)
        visited = dict()
        for i in range(len(wordList)):
            visited[wordList[i]] = False
        line = [(beginWord, 1)]
        visited[beginWord] = True
        point, right = 0, 0
        while point <= right:
            now, step = line[point]
            for next in nextWord[now]:
                if visited[next] == False:
                    right += 1
                    line.append((next, step + 1))
                    visited[next] = True
                if next == endWord:
                    result = self.getResult(nextWord, line, endWord)
                    return result
            point += 1
        return []




s = Solution()
print(s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
print(s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log"]))
print(s.findLadders("hot", "dot", ["hot","dot","dog"]))
