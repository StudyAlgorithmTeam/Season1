N = int(input())
P = [0] + list(map(int, input().split()))
value = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        value[i] = max(value[i], value[i-j] + P[j])

print(value[N])

