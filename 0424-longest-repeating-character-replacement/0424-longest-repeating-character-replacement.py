class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            # Add current character to frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Track the maximum frequency in current window
            max_freq = max(max_freq, count[s[right]])

            # If replacements needed > k, shrink window
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update result
            max_length = max(max_length, right - left + 1)

        return max_length
        