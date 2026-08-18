class Solution:
    def mergeSimilarItems(
        self, items1: list[list[int]], items2: list[list[int]]
    ) -> list[list[int]]:
        weights = {}

        for value, weight in items1 + items2:
            weights[value] = weights.get(value, 0) + weight

        return sorted([[value, weight] for value, weight in weights.items()])