import collections


def bfs (graph, node):
    visited = set()
    queue = collections.deque([node])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
    print(visited)

graph = {
    0: [1,2,3],
    1: [0,2],
    2: [0,1,4],
    3 : [0],
    4 : [2]
}
bfs(graph, 0)