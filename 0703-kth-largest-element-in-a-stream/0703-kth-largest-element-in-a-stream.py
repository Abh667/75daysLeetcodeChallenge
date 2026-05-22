import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        
        # Convert list into heap
        heapq.heapify(self.min_heap)

        # Keep only k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # If heap has less than k elements
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)

        # If new value is larger than smallest in heap
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)

        # Root of heap is kth largest
        return self.min_heap[0]