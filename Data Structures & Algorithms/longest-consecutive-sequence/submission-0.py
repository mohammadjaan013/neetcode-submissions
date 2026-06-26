class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in freq:
                current_count = 0
                while (num + current_count) in freq:
                    current_count += 1
                longest = max(current_count, longest)
        return longest



