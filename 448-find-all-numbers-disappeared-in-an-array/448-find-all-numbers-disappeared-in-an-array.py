class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            missingNums = nums[i] - 1
            if nums[i] != nums[missingNums]:
                nums[i], nums[missingNums] = nums[missingNums], nums[i]
            else:
                i += 1
                
        #for missing numbers
        missingNumbers = []
        for i in range(n):
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)
            
        return missingNumbers