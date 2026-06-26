class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapC = {}
        for i in range(len(nums)):
            if nums[i] in mapC:
                return True
            else:
                mapC[nums[i]] = 1
        return False       

         