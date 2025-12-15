def dfs(graph, st, en):
    s = [st] 
    v = {st}

    while s:
        c = s.pop()
        print(c, end=" ")

        if c == en:
            return

        for child in graph[c]:
            if child not in v:
                v.add(child)
                s.append(child)


    return


graph = {
    'a': ['b', 'd'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['a', 'b', 'e'],
    'e': ['c', 'd', 'b']
}

dfs(graph, 'a','e')
