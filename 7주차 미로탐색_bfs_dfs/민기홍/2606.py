computer = int(input()) #컴퓨터 개수
linked = int(input())   # 연결된 개수
graph = [[] for i in range(computer+1)] #그래프 초기화
visited = [0]*(computer+1)  # 방문처리 리스트

for i in range(linked):
    node1,node2 = map(int, input().split())
    graph[node1] += [node2]   # 각 노드 연결
    graph[node2] += [node1]

# bfs
Q = [1]  # 큐 생성
visited[1] = 1  # 1번부터 시작
while Q:
    current = Q.pop()
    for i in graph[current]:
        if visited[i] == 0:
            Q.append(i)
            visited[i] = 1

print(sum(visited)-1)