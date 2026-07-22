class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far, sol = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max_so_far += 1
            else:
                max_so_far = 0

            sol = max(sol, max_so_far)
        
        return sol