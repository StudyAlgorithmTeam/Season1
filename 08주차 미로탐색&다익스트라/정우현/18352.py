N,M,K,X = map(int,input().split())
g = [[] for _ in range(N+1)]
#1번 도시 부터 있기 때문에 M+1을 해서 변수 그대로 사용한다.

v = [[0] for _ in range(M+1)]
#방문을 확인한다.
a=[]

for i in range(M):
    x,y = map(int,input().split())
    g[x]+=[y]
    #단방향이기 때문에 하나만 연결한다.

def bfs(z):
    q=[]
    q.append((v,0))
    v[z] = 1
    while q:
        now,n = q.pop(0)
        if n == K:
            a.append(now)
        elif n > K:
            return
        for i in g[now]:
            if v[i] == 0:
                v[i] = 1
                q.append([i,n+1])


bfs(X)
if not a:
    print(-1)
else:
    a.sort()
    print(*a,sep = "\n")


