graph = {
    'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':[],
    'E':[]
}

visited = set()

def dfs(graph, visited, node):
    if node not in visited:
        visited.add(node)
        print(node)

        for i in graph[node]:
            dfs(graph, visited, i)


dfs(graph, visited, 'A')