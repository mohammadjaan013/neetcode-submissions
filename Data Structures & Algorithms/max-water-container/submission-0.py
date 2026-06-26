class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers at the start and end
        l, r = 0, len(heights) - 1
        max_area = 0
        
        # Move pointers towards each other
        while l < r:
            # Calculate width between pointers
            width = r - l
            # Calculate height (minimum of two heights)
            height = min(heights[l], heights[r])
            # Calculate current area
            area = width * height
            # Update max_area if current area is larger
            max_area = max(max_area, area)
            
            # Move the pointer with smaller height inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_area