class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            low = i + 1
            high = len(numbers) - 1
            comp = target - numbers[i]
            while low <= high:
                mid = low + (high - low) // 2
                if numbers[mid] == comp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < comp:
                    low = mid + 1
                else:
                    high = mid - 1
        return []