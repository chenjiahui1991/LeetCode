class Solution:
    def fully(self, lines, maxWidth):
        if len(lines) == 1:
            return lines[0] + " " * (maxWidth - len(lines[0]))
        spacecount = maxWidth - len("".join(lines))
        spacenum = spacecount // (len(lines) - 1)
        reminder = spacecount % (len(lines) - 1)
        result = lines[0]
        for i in range(1, len(lines)):
            result += " " * spacenum
            if i <= reminder:
                result += " "
            result += lines[i]
        return result

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        rest = 0
        ln = 0
        lines = []
        cur = []
        for word in words:
            if len(word) > rest:
                if ln != 0:
                    lines.append(cur[:])
                ln += 1
                cur = [word]
                rest = maxWidth - len(word) - 1
            else:
                cur.append(word)
                rest = rest - len(word) - 1
        if len(cur) > 0:
            lines.append(cur)
        for i in range(ln - 1):
            lines[i] = self.fully(lines[i], maxWidth)
        lines[-1] = " ".join(lines[-1])
        lines[-1] += " " * (maxWidth - len(lines[-1]))
        return lines


s = Solution()
print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"], 20))
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
