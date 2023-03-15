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