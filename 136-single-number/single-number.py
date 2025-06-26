class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for k in nums:
            if nums.count(k)==1:
                return k
        