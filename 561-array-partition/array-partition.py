class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        L=len(nums)
        c=0
        for i in range(0,L,2):
            c=c+nums[i]
        return c