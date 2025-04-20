#readable, but slower

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_p = len(p)
        len_s = len(s)

        # Early exit if s is shorter than p
        if len_s < len_p:
            return res

        # Frequency maps using Counter
        p_counter = Counter(p)
        window_counter = Counter(s[:len_p])

        # Check the initial window
        if p_counter == window_counter:
            res.append(0)

        # Slide the window over the string s
        for i in range(len_s - len_p):
            left_char = s[i]             # character going out
            right_char = s[i + len_p]    # character coming in

            # Decrease count or remove left_char
            window_counter[left_char] -= 1
            if window_counter[left_char] == 0:
                del window_counter[left_char]

            # Increase count of right_char
            window_counter[right_char] += 1

            # Check if current window matches target frequencies
            if p_counter == window_counter:
                res.append(i + 1)

        return res




#faster
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_p = len(p)

        # Build frequency map for string p
        checker = {}
        for ch in p:
            checker[ch] = checker.get(ch, 0) + 1

        # Build frequency map for the initial window in s
        temp_counter = {}
        for ch in s[:len_p]:
            temp_counter[ch] = temp_counter.get(ch, 0) + 1

        # Check if the initial window is an anagram
        if temp_counter == checker:
            res.append(0)

        # Slide the window across s
        for i in range(len(s) - len_p):
            left_char = s[i]             # character leaving the window
            right_char = s[i + len_p]    # character entering the window

            # Decrease or remove the left character from the window
            if temp_counter[left_char] == 1:
                del temp_counter[left_char]
            else:
                temp_counter[left_char] -= 1

            # Add or update the right character in the window
            temp_counter[right_char] = temp_counter.get(right_char, 0) + 1

            # Check if current window matches the anagram pattern
            if temp_counter == checker:
                res.append(i + 1)

        return res






