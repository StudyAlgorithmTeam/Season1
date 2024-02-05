N, K = map(int, input().split())
WV = [[0 for _ in range(2)] for i in range(N)]  # 무게
result = [0 for _ in range(N)]
max_result = 0


for i in range(N):
    WV[i][0], WV[i][1] = map(int, input().split())
#
# WV.sort()

# dp
for i in range(N, 0, -1):
    limit = K
    for j in range(i, 0, -1):
        if WV[j-1][0] <= limit :
            limit -= WV[j-1][0]
            result[i-1] += WV[j-1][1]

print(result)