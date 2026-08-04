class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        sol = [1] * n
        prefix, suffix = 1, 1
        for i in range(n):
            sol[i] = prefix
            prefix *= nums[i]
        
        for i in range(n - 1, -1, -1):
            sol[i] *= suffix
            suffix *= nums[i]
        
        return sol
