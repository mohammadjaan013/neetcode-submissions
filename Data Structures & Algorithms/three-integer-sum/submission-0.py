class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array first - this helps avoid duplicates and makes the process more efficient
        nums.sort()
        result = []

        # Iterate through each number as the first number of the triplet
        for i in range(len(nums) - 2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers technique for the remaining two numbers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet that sums to zero
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result

        