class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = []
        for i in range(len(word)):
            if word[i] == ch:
                for z in range(i, -1, -1):
                    res.append(word[z])
                for z in range(i+1, len(word)):
                    res.append(word[z])
                return "".join(res)
        return word