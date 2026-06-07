class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with a large value
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # Build the DP table
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
        