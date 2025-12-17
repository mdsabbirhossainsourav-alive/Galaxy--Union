import sys
import heapq
input = sys.stdin.readline
n = int(input())
graph = [[] for i in range(n)]
for i in range(n):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b,t))
    graph[b].append((a,t))
def dijkstra(start):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return sum(dist)
res = [dijkstra(i) for i in range(n)]
print(*res)
