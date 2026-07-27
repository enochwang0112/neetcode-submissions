class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}

        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        max_so_far = -1
        for num in hashmap:
            if hashmap[num] == num:
                max_so_far = max(max_so_far, num)
        
        return max_so_far