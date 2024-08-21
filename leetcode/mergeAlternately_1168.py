def mergeAlternately(word1, word2):
    if len(word2) > len(word1):
        short_word, long_word = word1, word2
    else:
        short_word, long_word = word2, word1

    res = []
    for i in range(len(short_word)):
        res.append(word1[i])
        res.append(word2[i])

    res.append(long_word[len(short_word):])
    return "".join(res)

assert mergeAlternately("ab", "pqrs") == "apbqrs"