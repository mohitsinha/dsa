# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/

prices=[1,2,4]

res = 0
n = len(prices)

if n == 1:
    res = 0

dp = [[0] * 2 for i in range(n)]

dp[0][1] = -1 * prices[0]
dp[1][0] = max(0, prices[1] - prices[0])

dp[1][1] = max(-prices[1], dp[0][1])
#         0 is not having stock
# 1 is having stock
for i in range(2, n):
    dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])

    dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])

res= max(dp[n - 1])