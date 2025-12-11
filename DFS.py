def dfs(graph, st):
    v = {st}
    stack = [st]
    print(st, end=" ")

    while stack:
        cur = stack.pop()

        for neighbor in graph[cur]:
            if neighbor not in v:
                v.add(neighbor)
                print(neighbor, end=" ")
                stack.append(neighbor)

    return

graph = {
    'a': ['b', 'd'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['a', 'b', 'e'],
    'e': ['c', 'd', 'b']
}

dfs(graph, 'a')
