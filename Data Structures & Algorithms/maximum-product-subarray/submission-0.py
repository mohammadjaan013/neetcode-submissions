class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]  # Initialize result with first element
        curMin, curMax = 1, 1  # Initial values for multiplication
    
        for num in nums:
            tmp = curMax * num  # Store this because curMax will change before we use it for curMin
            curMax = max(num * curMax, num * curMin, num)  # Max of: continuing subarray, flipping sign, or starting new
            curMin = min(tmp, num * curMin, num)  # Min of: continuing subarray, flipping sign, or starting new
            res = max(res, curMax)  # Update result if we found a better product
    
        return res
        