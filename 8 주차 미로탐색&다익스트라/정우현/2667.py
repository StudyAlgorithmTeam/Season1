N = int(input())
g = []
v = [[0]*N for _ in range(N)]
a = []
for _ in range(N):
    g.append(list(map(int,input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    #집을 일단 찾았으므로 카운트는 1로 시작한다.
    q = []
    q.append((x,y))
    v[x][y] = 1
    count = 1

    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and g[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = 1
                count += 1
    return count

for i in range(N):
    for j in range(N):
        #방문을 체크해서 안했으면 거기에서 bfs 진행
        if g[i][j] == 1 and v[i][j] == 0:
            a.append(bfs(i,j))

a.sort()
print(len(a))
print(*a, sep ="\n")
