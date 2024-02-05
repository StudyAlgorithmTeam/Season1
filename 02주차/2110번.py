import sys

input = sys.stdin.readline
# map 함수를 사용하여 입력된 값을 공백 기준으로 나눈 결과를 정수로 변환하여 각각 저장
N, C = map(int, input().split())
#N개의 집 좌표를 입력받고, 각 좌표를 정수로 변환 후 sorted 함수로 정렬하여 home에 저장
home = sorted([int(input()) for _ in range(N)])

# 공유기가 설치될 수 있는 최대 거리를 받아 해당 거리로 공유기를 설치했을 때의 개수를 세는 함수를 정의
# count 는 공유기의 개수 저장, current 는 현재 집의 좌표
def count_routers(distance):
    count, current = 1, home[0]
    
    for h in home:
        if h - current >= distance:
            count += 1
            current = h
    
    return count

# 이진 탐색을 위한 시작점과 끝점 설정, 시작점은 항상 1, 끝점은 정렬된 집의 좌표 중 가장 뒤에 있는 좌표에서 가장 앞에 있는 좌표를 뺀 값
start, end = 1, home[-1] - home[0]
# result 는 공유기 사이의 최대 거
result = 0

# 시작점이 끝점보다 작거나 같은 동안 계속 반복, 중간지점 mid 계산
while start <= end:
    mid = (start + end) // 2

# 중간 지점으로 공유기를 설치했을 때의 개수가 목표 개수보다 크거나 같다면, 현재의 중간 값을 결과로 저장
    # 시작점을 중간값보다 +1로 갱신, 그렇지 않다면 끝점을 중간 값보다 -1로 갱신
    if count_routers(mid) >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
