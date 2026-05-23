class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        # Convert into max heap using negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # Smash stones until one or none remains
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # heaviest
            x = -heapq.heappop(max_heap)  # second heaviest

            if y != x:
                heapq.heappush(max_heap, -(y - x))

        # Return remaining stone or 0
        return -max_heap[0] if max_heap else 0
        