class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for c in s:
            if c.isalnum():
                temp += c.lower()

        i, j = 0, len(temp) - 1
        while i < j:
            if temp[i] != temp[j]:
                return False
            i += 1
            j -= 1
        return True