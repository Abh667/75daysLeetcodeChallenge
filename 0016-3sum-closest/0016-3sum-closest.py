class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        # Initialize closest sum
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest sum
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
                # Move pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match
        
        return closest


# Example Usage
sol = Solution()

print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(sol.threeSumClosest([0, 0, 0], 1))       # Output: 0
        