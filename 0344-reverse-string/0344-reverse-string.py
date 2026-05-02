class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            # Swap characters
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1


# Example Usage
s = ["h", "e", "l", "l", "o"]

obj = Solution()
obj.reverseString(s)

print(s)
        