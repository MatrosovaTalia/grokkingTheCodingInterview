def maxProfit(self, prices) -> int:
    if len(prices) == 1:
        return 0

    minP = 10001
    profit = 0
    for p in prices:
        if p < minP:
            minP = p
        else:
            if p - minP > profit:
                profit = p - minP
    
    return profit

    # [1 2 3 4 1 7]
    # [7 1 2 3 5]
    # [1]
    # [2 7 9]
    # [2 5 3 10]