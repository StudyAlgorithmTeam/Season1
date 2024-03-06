def min_coin_count(N, K, coin_values):
    count = 0

    # 가장 큰 가치의 동전부터 차례로 사용하여 K를 만듦
    for i in range(N-1, -1, -1):
        if K == 0:
            break
        if K >= coin_values[i]:
            count += K // coin_values[i]
            K %= coin_values[i]

    return count

# 입력 받기
N, K = map(int, input().split())
coin_values = [int(input()) for _ in range(N)]

# 필요한 동전 개수의 최솟값 계산 및 출력
result = min_coin_count(N, K, coin_values)
print(result)
