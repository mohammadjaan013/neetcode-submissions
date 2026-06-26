class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefix = 1
        suffix = 1
        # Let's calculate the Prefix
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Now let's calculate the Suffix
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]            
        
        return output

        