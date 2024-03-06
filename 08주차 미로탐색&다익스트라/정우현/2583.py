M,N,K = map(int,input().split())
arr = [[1]*N for _ in range(M)]
#지정된 사각형 외의 영역을 측정하기 때문에 1로 다 채워준다.

for i in range(K):
    x,y,xx,yy = map(int,input().split())

    for i in range(y,yy):
        for j in range(x,xx):
            arr[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

a = []
v = [[0]*N for _ in range(M)]
def bfs(x,y):
    q = []
    q.append((x,y))
    v[x][y] = 1
    count = 1

    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and arr[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = 1
                count += 1
    return count

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] ==0:
            a.append(bfs(i,j))
a.sort()
print(len(a))
print(*a, sep=" ")
