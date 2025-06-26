class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uni=set()
        for i in nums:
            uni.add(i)
        uniq=sorted(uni)
        uniq.reverse()
        n=uniq[2] if len(uniq)>=3 else uniq[0]
        return n
    
        



