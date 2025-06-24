class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        z_losses = set()
        o_loss = set()
        m_losses = set()

        for winner, loser in matches:
            if winner not in o_loss and winner not in m_losses:
                z_losses.add(winner)
            if loser in m_losses:
                continue 
            elif loser in o_loss:
                o_loss.remove(loser)
                m_losses.add(loser)
            elif loser in z_losses:
                z_losses.remove(loser)
                o_loss.add(loser)
            else:
                o_loss.add(loser)
        return [sorted(z_losses), sorted(o_loss)]
