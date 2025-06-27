class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n={}
        for i, num in enumerate(nums):
            c=target-num
            if c in n:
                return [n[c], i]
            n[num]=i