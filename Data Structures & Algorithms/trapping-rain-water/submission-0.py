class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: if array is empty or has less than 3 elements
        if not height or len(height) < 3:
            return 0
            
        # Initialize two pointers and variables
        left, right = 0, len(height) - 1
        left_max = right_max = total_water = 0
        
        # Continue until pointers meet
        while left < right:
            # Update max heights from left and right
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # Move the pointer on the side with smaller max height
            if left_max < right_max:
                # Water at current position is difference between
                # left_max and current height
                water = left_max - height[left]
                total_water += water
                left += 1
            else:
                # Water at current position is difference between
                # right_max and current height
                water = right_max - height[right]
                total_water += water
                right -= 1
                
        return total_water