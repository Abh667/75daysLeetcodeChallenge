class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        
        # Dictionary to store prefix sum frequencies
        prefix_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            # Check if there exists a prefix sum
            # such that current_sum - previous_sum = k
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]
            
            # Store current prefix sum
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return count
        