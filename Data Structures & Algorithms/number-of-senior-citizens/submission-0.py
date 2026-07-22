class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for s in details:
            if int(s[11:13]) > 60:
                total += 1
        
        return total