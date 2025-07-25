class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        s=score[ : ]
        scores=[]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                 if s[i][k] < s[j][k]: 
                    t = s[i]
                    s[i] = s[j]
                    s[j] = t
        for i in range(len(s)):
            scores.append(s[i][:])
        return scores
               
