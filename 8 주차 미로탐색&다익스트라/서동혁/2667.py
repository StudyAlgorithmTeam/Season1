from collections import deque

N = int(input())

graph = []
result = []
count = 0

for i in range(N):
  graph.append(list(map(int, input())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
  global count
  #정사각형 지도 밖으로 나갈 경우
  if x<0 or x>=N or y<0 or y>=N:
    return
  #방문한적이 없는 집들의 경우
  if graph[x][y] == 1:
    count = count + 1
    graph[x][y] = 0 #방문처리
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx,ny)

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      dfs(i,j)
      result.append(count)
      count = 0

result.sort()
print(len(result))
for i in result:
  print(i)