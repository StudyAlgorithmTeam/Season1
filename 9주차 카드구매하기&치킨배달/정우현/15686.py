from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
home = []
result = float('inf')  # 결과값을 무한대로 초기화 초기 값을 설정하기 위해

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i, j))
        if arr[i][j] == 2:
            chicken.append((i, j))

for comb in combinations(chicken, M):  # 조합 생성
    temp = 0
    for j in home:
        c_len = float('inf')  # c_len을 무한대로 초기화 초기 값을 설정하기 위해
        for k in range(M):
            c_len = min(c_len, abs(j[0] - comb[k][0]) + abs(j[1] - comb[k][1]))
        temp += c_len
    result = min(result, temp)

print(result)
