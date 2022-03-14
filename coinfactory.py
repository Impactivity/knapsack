import sys
import math
inf = math.inf

read = sys.stdin.readline

coins = [1 ,5 ,10 ,50 ,100, 500]

# #case 1
# costs = [1, 4, 99, 35, 50, 1000]
# money = 4578

#case 2
# costs = [2, 11, 20, 100, 200, 600]
# money = 1999

money = int(read())
costs = list(map(int,read().split()))

dp = [ inf for _ in range(money+1)]

dp[0] = costs[0]
for c in range(0,6):
    dp[coins[c]] = costs[c]


for c in coins:
    for i in range(1, money+1):
        if i-c >= 0:
            if dp[i] > dp[i-c] + dp[c]:
                dp[i] = dp[i-c] + dp[c]

print(dp[money])





