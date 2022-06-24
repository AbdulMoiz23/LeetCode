class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        
        
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left +=1
        return left 
       
        # while(left < len(nums)):
        #     if nums[right - 1] != nums[left]:
        #         nums[right] == nums[left]
        #         nums[right] +=1
        #     left +=1
        # return nums[right]
        