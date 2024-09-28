#TWO SUM 
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store the index of the numbers
        
        for i, num in enumerate(nums):
            complement = target - num  # The number we need to find
            
            if complement in num_map:
                return [num_map[complement], i]  # Return the indices
            
            num_map[num] = i  # Store the index of the current number
        
#REVERSE STRING
class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1