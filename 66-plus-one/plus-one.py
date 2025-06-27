class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=int(''.join(map(str, digits)))
        n+=1
        news=[int(i) for i in str(n)]
        return news
