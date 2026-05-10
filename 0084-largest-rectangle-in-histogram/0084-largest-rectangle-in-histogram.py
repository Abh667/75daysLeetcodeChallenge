class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        max_area = 0

        # Add a 0 height bar at the end to empty the stack
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                # Width calculation
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area
        