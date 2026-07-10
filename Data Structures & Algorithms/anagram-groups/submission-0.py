class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))

            if sorted_str not in hashmap:
                hashmap[sorted_str] = []
            hashmap[sorted_str].append(s)
        
        lst = []
        for val in hashmap.values():
            lst.append(val)
        
        return lst