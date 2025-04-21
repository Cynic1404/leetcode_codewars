def partitionLabels(s):
    # Dictionary to store the last occurrence index of each character
    last_position = {}
    for i in range(len(s)):
        last_position[s[i]] = i

    res = []       # List to store the size of each partition
    start = 0      # Start index of the current partition
    end = 0        # End index of the current partition

    for i in range(len(s)):
        # Update the end of the current partition to the farthest last occurrence
        end = max(end, last_position[s[i]])

        # If the current index reaches the partition end,
        # we have completed one partition
        if i == end:
            res.append(end - start + 1)  # Add the size of the partition
            start = i + 1               # Start a new partition from the next index

    return res

partitionLabels('ababcbacadefegdehijhklij')