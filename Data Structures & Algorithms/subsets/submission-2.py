class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]

        for num in nums:
            sol += [subset + [num] for subset in sol]

        return sol