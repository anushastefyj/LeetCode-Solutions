class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        diff = (sum_b - sum_a) // 2
        
        bob_set = set(bobSizes)
        
        for x in aliceSizes:
            target = x + diff
            if target in bob_set:
                return [x, target]