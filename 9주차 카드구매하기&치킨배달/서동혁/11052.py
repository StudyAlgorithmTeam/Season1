N = int(input())
value = list(map(int, input().split()))
value.insert(0,0)

dp = value
for i in range(1, N):
  for j in range(1,i+1):
    if dp[i+1] <= value[j] + dp[i+1-j]:
      dp[i+1] = value[j] + dp[i+1-j]

print(dp[N])