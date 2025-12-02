########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Dynamic Programming | Maximum Profit
########################################################################################################################

from typing import List
import random

### maximum profit function ############################################################################################

def max_profit(prices:List[int]=list()) -> int:
    """
    Finds the solution for the Maximum Profit coding problem:  
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/  
    Uses iterative dynamic programming and memory optimization.

    ### Parameters
    - prices : List[int], series of stock prices  
        1 <= prices.length <= 10^5, 0 <= prices[i] <= 10^4  
        defaults to empty list
    ### Returns
    - int, maximum available profit
    - -1, invalid input
    """

    ### invalid input > returning -1 -----------------------------------------------------------------------------------

    if type(prices) is not list or len(prices) < 2 or 100000 < len(prices): return -1
    if any(type(price) is not int or price < 0 or 10000 < price for price in prices): return -1

    ### register init --------------------------------------------------------------------------------------------------

    buy_price: int = prices[0]
    max_profit: int = 0

    ### calculating maximum profit -------------------------------------------------------------------------------------

    for price in prices:
        max_profit = max(max_profit, price - buy_price)
        buy_price = min(buy_price, price)

    ### returning maximum profit ---------------------------------------------------------------------------------------

    return max_profit

########################################################################################################################
### testing code
########################################################################################################################

print()

print("Maximum Profit")
print()

print("Profit() =", max_profit())
print()

print("Profit('test') =", max_profit(prices=["test"]))
print("Profit([1]) =", max_profit(prices=[1]))
print("Profit([1]*100005) =", max_profit(prices=[1]*100005))
print()

print("Profit([1,'test',2) =", max_profit(prices=[1,"test",2]))
print("Profit([1,-1,2) =", max_profit(prices=[1,-1,2]))
print("Profit([1,15000,2) =", max_profit(prices=[1,15000,2]))
print()

price_list: List[int] = [random.randint(1, 10001) for _ in range(100)]
# price_list.sort(reverse=True)
print(f"Profit({price_list}) = {max_profit(prices=price_list)}")
print()
