class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_len = 1

        def expand(left, right):
            nonlocal start, max_len

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            length = right - left - 1

            if length > max_len:
                max_len = length
                start = left + 1

        for i in range(n):
            # Odd length palindrome
            expand(i, i)

            # Even length palindrome
            expand(i, i + 1)

        return s[start:start + max_len]
        