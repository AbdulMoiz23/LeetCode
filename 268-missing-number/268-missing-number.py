class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            missNum = nums[i]
            if nums[i] < n and nums[i] != nums[missNum]:
                nums[i], nums[missNum] = nums[missNum], nums[i]
            else:
                i += 1
                
        # for missing number
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n
    
    
    
         
        