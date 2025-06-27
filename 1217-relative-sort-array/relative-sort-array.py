class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr=[]
        c=Counter(arr1)
        for i in arr2:
            arr.extend([i]*c[i])
            c[i]=0
        arr3=[]
        for num in c:
            if c[num]>0:
                arr3.extend([num]*c[num])
        arr.extend(sorted(arr3))
        return arr     
        
