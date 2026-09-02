import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        
        # Keep only the k largest elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        
        # Evict the smallest if size exceeds k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        return self.min_heap[0]