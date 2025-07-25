class Solution:
    def findWords(self, words: List[str]) -> List[str]:  
        a=["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        in_same=[]
        for i in words:
            n=set(i.lower())
            if n.issubset(a[0]) or n.issubset(a[1]) or n.issubset(a[2]):
                in_same.append(i)
        return in_same
