from collections import deque

N = int(input())
graph = []  # 미로를 저장할 리스트(visited 정보 저장)
house = []  # 각 단지내 집의 수 저장
count = 0   # 총 단지 수 저장

for _ in range(N):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    graph[x][y] = 0 # 현재 위치를 0으로 만듬
    cnt = 1     # 단지 수

    while Q:
        x, y = Q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    Q.append((nx, ny))
                    cnt += 1
    return cnt


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append(bfs(i, j))
            count += 1


# 출력 부분
print(count)
house.sort()
for _ in range(count) :
    print(house[_])

