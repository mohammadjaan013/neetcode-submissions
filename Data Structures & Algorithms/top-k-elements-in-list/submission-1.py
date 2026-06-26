class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        result = []
        new_res = []
        sorted_freq = dict(sorted(freq.items(), key = lambda item : item[1], reverse = True ))
        for num, count in sorted_freq.items():
            result.append(num)
        for i in range(k):
            new_res.append(result[i])
        return new_res

        