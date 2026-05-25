class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        # Count frequency of each task
        freq = Counter(tasks)

        # Maximum frequency
        max_freq = max(freq.values())

        # Count how many tasks have maximum frequency
        max_count = list(freq.values()).count(max_freq)

        # Formula
        intervals = (max_freq - 1) * (n + 1) + max_count

        # Final answer
        return max(len(tasks), intervals)
        
        

        