def tiles(n, dp):
    if n <= 2:
        return n

    if dp[n] != 0 :
        return dp[n]

    dp[n] = (tiles(n-1, dp) + tiles(n-2, dp)) % 10007

    return dp[n]

n = int(input())

dp = [0] * (n+1)

print(tiles(n, dp))