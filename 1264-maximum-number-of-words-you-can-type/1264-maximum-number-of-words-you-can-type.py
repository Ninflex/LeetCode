class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        count = 0
        for i in words:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                count += 1
        return count
        