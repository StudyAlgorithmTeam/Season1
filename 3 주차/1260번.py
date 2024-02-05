from collections import deque

#그래프, 시작노드, 방문 여부 나타내는 배열을 인자로 받기 - 깊이 우선 탐색
def dfs(graph, start, visited):
    print(start, end=' ')
    visited[start] = True #노드 방문 완료

# 현재 노드에 연결된 이웃 노드들 순회 (정렬된 순서로 방문하기 위해 sorted()함수 사용)
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited) # 이웃 노드가 방문되지 않을 시 DFS 함수를 재귀적으로 호출하여 해당 이웃 방문
# 너비 우선 탐색
def bfs(graph, start, visited):
    queue = deque([start]) # BFS에서 사용할 큐 초기화 - 시작 노드로 큐 초기화
    visited[start] = True

    while queue: # 큐가 비어 있지 않는 동안 반복
        node = queue.popleft()  # 큐의 맨 앞에서 노드 꺼내기
        print(node, end=' ') #현재 노드를 출력

        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# 입력 받기 (정점의 개수 - N, 간선의 개수 - M, 시작 노드 - V)
N, M, V = map(int, input().split())

# 1부터 N까지의 정점을 갖는 빈 그래프를 초기화
graph = {i: set() for i in range(1, N + 1)}

#간선 정보를 입력받아 양방향 그래프 만들기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

# DFS와 BFS에서 사용할 방문 여부를 나타내는 배열을 초기화
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

# DFS 수행
dfs(graph, V, visited_dfs)
print()

# BFS 수행
bfs(graph, V, visited_bfs)
