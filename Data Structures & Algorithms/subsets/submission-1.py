class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                sol.append(curr.copy())
                return

            backtrack(i + 1)
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
        
        backtrack(0)
        return sol