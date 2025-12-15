from collections import deque

def bfs(graph, st, en):
    q = deque([st])
    v = {st}

    while q:
        c = q.popleft()
        print(c, end=" ")

        if c == en:
            return

        for child in graph[c]:
            if child not in v:
                v.add(child)
                q.append(child)


    return


graph = {
    'a': ['b', 'd'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['a', 'b', 'e'],
    'e': ['c', 'd', 'b']
}

bfs(graph, 'a')
