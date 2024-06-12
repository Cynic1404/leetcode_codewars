def isIsomorphic(s, t) -> bool:
    # Dictionary to keep track of the mapping from characters in s to characters in t
    checker = {}

    # Iterate through each character in the strings s and t
    for i in range(len(s)):
        # If the character from s is not in the mapping dictionary
        if s[i] not in checker:
            # Check if the character from t is already mapped to another character
            if t[i] not in checker.values():
                # If not, establish the new mapping from s[i] to t[i]
                checker[s[i]] = t[i]
            else:
                # If t[i] is already mapped, return False because it violates the isomorphic property
                return False
        else:
            # If s[i] is already in the mapping dictionary, check if it maps to the correct character in t
            if t[i] != checker[s[i]]:
                # If it does not map correctly, return False
                return False

    # If all characters map correctly, return True
    return True