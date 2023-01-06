class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Store ice cream costs in increasing order.
        costs.sort()
        n, icecream = len(costs), 0

        # Pick ice creams till we can.
        while icecream < n and costs[icecream] <= coins:
            # We can buy this icecream, reduce the cost from the coins. 
            coins -= costs[icecream]
            icecream += 1

        return icecream