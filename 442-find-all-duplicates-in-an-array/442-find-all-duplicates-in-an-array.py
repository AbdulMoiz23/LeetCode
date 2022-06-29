class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        duplicateNum = []
        for i in range(n):
            if nums[i] != i + 1:
                duplicateNum.append(nums[i])
        return duplicateNum
        