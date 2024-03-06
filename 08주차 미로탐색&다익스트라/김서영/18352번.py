import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
#0이 아니라 빈 리스트로 초기화되기 때문에, 각 도시에서 출발하는 도로의 목록을 담는 그래프를 나타내기 위한 초기화
graph = [[] for _ in range(N + 1)]
#0으로 초기화된 리스트를 생성하되, 반복 변수가 필요하지 않다는 것을 나타내기 위해 _를 사용한 것
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

result = []

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        current_city = queue.popleft()
        #현재 도시까지의 거리가 k+1이라면(bfs 탐색의 k번째 단계에 도달했다면, 해당 도시를 결과 리스트에 추가
        if visited[current_city] == K + 1:
            result.append(current_city)
            continue
        for neighbor in graph[current_city]:
            #이웃 도시가 아직 방문되지 않았을 경우, 해당 도시 큐에 추가
            if visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = visited[current_city] + 1

#시작 도시 x에서부터 bfs탐색
bfs(X)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for city in result:
        print(city)
