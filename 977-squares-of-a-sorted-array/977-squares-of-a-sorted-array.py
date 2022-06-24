class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left = 0
        right = len(nums) - 1
        
        #pointers havent crossed each others
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                result.append(nums[left] * nums[left])
                left +=1
            else:
                result.append(nums[right] * nums[right])
                right -=1
            
        #will append in reverse order
        # to reverse [::-1] 
        
        return result[::-1]
        
        
            