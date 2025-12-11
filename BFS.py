from collections import deque

def bfs(graph, st):
    v = {st}
    queue = deque([st])
    print(st, end=" ")
  
    while queue:
        cur = queue.popleft()

        for neighbor in graph[cur]:
            if neighbor not in v:
                v.add(neighbor)
                print(neighbor, end=" ")
                queue.append(neighbor)


graph = {
    'a': ['b', 'd'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['a', 'b', 'e'],
    'e': ['c', 'd', 'b']
}

bfs(graph, 'a')
