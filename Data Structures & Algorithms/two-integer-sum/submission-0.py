class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapN = {}
        for i, n in enumerate(nums):
            dif = target - nums[i]
            if dif in mapN:
                return [mapN[dif], i]
            mapN[n] = i
        return
        
        