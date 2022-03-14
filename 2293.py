import sys
read = sys.stdin.readline

n,k = map(int, read().split())
coins = []

for i in range(n):
    coins.append(int(read()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in coins:
    for i in range(1,k+1):
        if i-c >= 0:
            dp[i] = dp[i] + dp[i-c]

print(dp[k])