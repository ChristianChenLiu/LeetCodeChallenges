class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zeroLost = set()
        oneLoss = set()
        losers = set()
        for winner, loser in matches:
            if winner not in losers and winner not in oneLoss:
                zeroLost.add(winner)

            if loser not in oneLoss and loser not in losers:
                oneLoss.add(loser)
                if loser in zeroLost: zeroLost.remove(loser)
            elif loser in oneLoss:
                oneLoss.remove(loser)
                losers.add(loser)
            elif loser in zeroLost:
                zeroLost.remove(loser)
                oneLoss.add(loser)
                
        return [sorted(list(zeroLost)), sorted(list(oneLoss))]
