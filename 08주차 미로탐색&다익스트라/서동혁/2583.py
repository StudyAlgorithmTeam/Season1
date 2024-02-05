import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())

graph = []
result = []
count = 0
my_map = [[1]*(M) for i in range(N)]

for i in range(K):
  graph.append(list(map(int,input().split())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(K):
  for j in range(graph[i][0], graph[i][2]):
    for k in range(graph[i][1], graph[i][3]):
      my_map[j][k] = 0

def dfs(x,y):
  global count

  if x<0 or y<0 or x>=N or y>=M:
    return
  if my_map[x][y] == 1:
    count = count + 1
    my_map[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx,ny)
for i in range(N):
  for j in range(M):
    if my_map[i][j] == 1:
      dfs(i,j)
      result.append(count)
      count = 0
result.sort()
print(len(result))
for i in result:
  print(i, end=" ")