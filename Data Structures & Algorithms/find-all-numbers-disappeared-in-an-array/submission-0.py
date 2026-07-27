class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset = set(range(1, len(nums) + 1))

        for num in nums:
            hashset.discard(num)

        return list(hashset)