class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        most_common = freq.most_common(k)

        return [key for key, value in most_common]