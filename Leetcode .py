#TWO SUM 
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  
        
        for i, num in enumerate(nums):
            complement = target - num  
            
            if complement in num_map:
                return [num_map[complement], i]  
            
            num_map[num] = i
            
#REVERSE STRING
class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1
    
#PALINDROME NUM             
def isPalindrome(self, x):
         if x < 0:
            return False
        
        original = x
        reversedNum = 0
        
        while x > 0:
            reversedNum = reversedNum * 10 + x % 10
            x //= 10
        
        return original == reversedNum
        