class Solution(object):
    def longestCommonPrefix(self, strs):
        # Handle edge cases
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        # Initialize prefix as an empty string
        prefix = ""

        # Get the length of the shortest string
        min_length = len(min(strs, key=len))

        # Loop over the characters of the shortest string
        for i in range(min_length):
            char = strs[0][i]  # Take the ith character of the first string as reference

            # Check if this character is present at the ith position in all strings
            is_common = True
            for s in strs:
                if s[i] != char:
                    is_common = False
                    break  # If not, break the loop
            
            if is_common:
                prefix += char  # If yes, add it to the prefix
            else:
                break  # If not, break the loop

        return prefix
