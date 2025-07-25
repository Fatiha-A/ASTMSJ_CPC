class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_m=[]
        for k in range(len(matrix[0])):
            new_m.append([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_m[j].append(matrix[i][j])
        return new_m
            