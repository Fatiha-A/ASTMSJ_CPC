class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank=[]
        sort=sorted(score, reverse=True)
        f="Gold Medal"
        s="Silver Medal"
        th="Bronze Medal"
        for i in range(len(score)):
            if score[i]==max(score):
                rank.append(f)
            elif score[i]==sort[1]:
                rank.append(s)
            elif score[i]==sort[2]:
                rank.append(th)
            else:
                rank.append(str(sort.index(score[i])+1))
        return rank



                