class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()

        for num in nums:
            hashset.add(num)

        sol = 0
        for num in hashset:
            if num - 1 not in hashset:
                length = 1
                current = num
                
                while current + 1 in hashset:
                    current += 1
                    length += 1
                
                sol = max(sol, length)
        
        return sol