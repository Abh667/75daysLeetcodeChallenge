class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_line(houses):
            prev1 = 0  # dp[i-1]
            prev2 = 0  # dp[i-2]

            for money in houses:
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            rob_line(nums[:-1]),  # exclude last
            rob_line(nums[1:])    # exclude first
        )
        