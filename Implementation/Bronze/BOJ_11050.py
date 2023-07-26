n, k = map(int, input().split())
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1

for i in range(2, n + 1):
  dp[i] = i * dp[i - 1]

print(dp[n] // (dp[n - k] * dp[k]))
"""
nCk  =  n!/(n-k)!*k!
      dp로 한번 풀어보았다
"""
