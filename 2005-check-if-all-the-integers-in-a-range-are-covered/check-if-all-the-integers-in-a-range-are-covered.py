class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        num=set()
        for start,end in ranges:
            num.update(range(start,end+1))
        for i in range(left,right+1):
            if i not in num:
                return False
        return True

