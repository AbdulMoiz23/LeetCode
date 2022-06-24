class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Pnums = {}
        
        
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in Pnums:
                return [Pnums[diff], i]
            Pnums[n] = i
        return
        
        
        