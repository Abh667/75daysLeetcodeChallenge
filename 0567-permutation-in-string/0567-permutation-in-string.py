from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        # If s1 is longer than s2
        if n1 > n2:
            return False

        # Frequency count of s1
        s1_count = Counter(s1)

        # Frequency count of first window in s2
        window_count = Counter(s2[:n1])

        # Check first window
        if s1_count == window_count:
            return True

        # Sliding window
        for i in range(n1, n2):

            # Add new character
            window_count[s2[i]] += 1

            # Remove left character
            left_char = s2[i - n1]
            window_count[left_char] -= 1

            # Remove key if count becomes 0
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Compare counts
            if window_count == s1_count:
                return True

        return False
        