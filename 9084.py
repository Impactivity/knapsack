import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    coins = list(map(int,read().split()))
    money = int(read())

    dp = [ 0 for i in range(money + 1)]
    dp[0] = 1

    for c in coins:
        for i in range(1, money+1):
            if i - c >= 0:
                dp[i] += dp[i-c]


    print(dp[money])





