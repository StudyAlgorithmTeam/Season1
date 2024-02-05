N = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if j-i>=0:
            dp[j] = max(dp[j],a[i]+dp[j-i])

print(dp[N])
