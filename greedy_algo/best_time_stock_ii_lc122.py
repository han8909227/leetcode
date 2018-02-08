# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However,
# you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


def stock(prices):
    """LC 122."""
    idx = 0
    total_earn = 0

    while idx < len(prices):
        min_v = prices[0]
        max_p = 0
        for i in range(len(prices)):
            if prices[i] < min_v:
                min_v = prices[i]
            if prices[i] - min_v > max_p:
                idx = i
                max_p = prices[i] - min_v
        total_earn += (max_p)
        prices = prices[idx:]

    return total_earn


if __name__ == '__main__':
    prices = [1, 3, 2, 6, 8, 5, 10, 15, 8]
