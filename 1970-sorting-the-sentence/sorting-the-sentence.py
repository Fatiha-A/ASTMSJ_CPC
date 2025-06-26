
class Solution:
    def sortSentence(self, s: str) -> str:
        ws= s.split()
        s_w = sorted(ws, key=lambda w: int(w[-1]))
        r_s = " ".join(w[:-1] for w in s_w)
        return r_s
