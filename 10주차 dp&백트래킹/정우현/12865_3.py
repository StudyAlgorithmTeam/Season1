import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
            #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            #그게 아니면 현재 물건의 가치 더하기 넣을 수 있는 무게에서 현재 무게를
            #뺀 값 중 최대값의 가치를 더한 것과 이전에 그 무게 넣었던 가치 중 더 큰 값을
            #넣어준다.
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])
