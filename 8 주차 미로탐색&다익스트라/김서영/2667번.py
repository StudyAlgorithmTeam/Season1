from collections import deque

size = int(input())
grid = [[int(x) for x in input()] for _ in range(size)]

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    grid[start_x][start_y] = 0
    count = 1

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if next_x < 0 or next_x >= size or next_y < 0 or next_y >= size:
                continue
            if grid[next_x][next_y] == 1:
                grid[next_x][next_y] = 0
                queue.append((next_x, next_y))
                count += 1
    return count

component_sizes = []
for i in range(size):
    for j in range(size):
        if grid[i][j] == 1:
            component_sizes.append(bfs(i, j))

component_sizes.sort()
print(len(component_sizes))
for size in component_sizes:
    print(size)
