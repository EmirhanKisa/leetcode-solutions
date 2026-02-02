# Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Zorluk: Easy

# Time Complexity: O(N) (Diziyi baştan sona tek bir kez taradığımız için - One Pass)
# Space Complexity: O(1) (Ekstra bir liste oluşturmadık, sadece minPrice ve maxProfit değişkenlerini tuttuk)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):

            if prices[i] < minPrice:
                minPrice = prices[i]

            elif maxProfit < (prices[i] - minPrice):
                maxProfit = (prices[i] - minPrice)

        return maxProfit


if __name__ == "__main__":
    solution = Solution()

    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: prices = {prices1}")
    print(f"Output: {solution.maxProfit(prices1)}")

    print("-" * 20)

    prices2 = [7, 6, 4, 3, 1]
    print(f"Input: prices = {prices2}")
    print(f"Output: {solution.maxProfit(prices2)}")

    print("-" * 20)

    prices3 = [1, 20]
    print(f"Input: prices = {prices3}")
    print(f"Output: {solution.maxProfit(prices3)}")