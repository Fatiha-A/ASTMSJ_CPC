class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=set()
        for k in nums:
            if k in n:
                return True
            n.add(k)
        return False
