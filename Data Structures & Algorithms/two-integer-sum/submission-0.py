class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        lst = []
        for i in range(len(nums)):
            if nums[i] in comp:
                return [comp[nums[i]], i]
            temp = target - nums[i]
            comp[temp] = i
