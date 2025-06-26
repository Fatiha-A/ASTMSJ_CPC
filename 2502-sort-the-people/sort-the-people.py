class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ph=[]
        for i in range(len(names)):
            ph.append((heights[i], names[i]))
        ph.sort()
        ph.reverse()
        s_n=[]
        for k in range(len(names)):
            s_n.append(ph[k][1])
        return s_n
        
