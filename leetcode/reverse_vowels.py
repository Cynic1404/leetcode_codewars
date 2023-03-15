class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = []
        indexes = []
        s=list(s)
        for i in range(len(s)):
            if s[i] in "AaEeIiOoUu":
                letters.append(s[i])
                indexes.append(i)
        letters = list(reversed(letters))
        for i in range(len(letters)):
            s[indexes[i]]=letters[i]
        return("".join(s))


    #memory efficient
    def reverseVowels2(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s) - 1
        while end > start:
            if s[start] not in "AaEeIiOoUu":
                start += 1
            if s[end] not in "AaEeIiOoUu":
                end -= 1

            if s[start] in "AaEeIiOoUu" and s[end] in "AaEeIiOoUu":
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return "".join(s)