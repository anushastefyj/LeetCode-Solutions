class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        operations = 0

        # Helper function to check if the list is non-decreasing
        def is_sorted(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        while not is_sorted(nums):
            # Find the adjacent pair with the minimum sum (leftmost on tie)
            min_sum = float("inf")
            min_idx = 0
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i

            # Replace the pair with their sum
            nums = nums[:min_idx] + [min_sum] + nums[min_idx + 2 :]
            operations += 1

        return operations