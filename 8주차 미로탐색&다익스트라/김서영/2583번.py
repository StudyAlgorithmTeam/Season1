import sys
sys.setrecursionlimit(10**6)

def explore(x, y):
    visited[x][y] = 1
    region_size[0] += 1
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            explore(nx, ny)

region_size = [0]
N, M, K = map(int, sys.stdin.readline().split())
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            visited[j][k] = 1

regions_count = 0
regions_sizes = []

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            explore(i, j)
            regions_count += 1
            regions_sizes.append(region_size[0])
            region_size[0] = 0

regions_sizes.sort()

print(regions_count)
print(*regions_sizes)
