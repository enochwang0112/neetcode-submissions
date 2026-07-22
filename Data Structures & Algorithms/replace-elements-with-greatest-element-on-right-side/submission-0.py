class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        sol = [-1] * len(arr)
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            sol[i] = max_so_far
            max_so_far = max(max_so_far, arr[i])
        return sol