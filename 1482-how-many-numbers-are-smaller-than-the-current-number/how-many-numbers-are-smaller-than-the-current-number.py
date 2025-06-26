class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c=0
        n_a=[]
        for i in nums:
            for j in range(len(nums)):
                if i>nums[j]:
                    c+=1
            n_a.append(c)
            c=0
        return n_a
