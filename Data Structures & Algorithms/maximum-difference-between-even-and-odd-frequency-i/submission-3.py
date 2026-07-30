class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}
        max_odd = 0
        min_even = 102

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        
        for val in hashmap:
            if hashmap[val] % 2 == 1:
                max_odd = max(max_odd, hashmap[val])
            else:
                min_even = min(min_even, hashmap[val])
        
        return max_odd - min_even