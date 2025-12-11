def minimax(node, is_max):
  if type(graph[node][0]) in [int, float]:
    if is_max:
      return max(graph[node])
    else:
      return min(graph[node])

  if is_max:
    best = -float('inf')
    for child in graph[node]:
      val = minimax(child, False)
      best = max(best, val)
    return best

  else:
    best = float('inf')
    for child in graph[node]:
      val = minimax(child, True)
      best = min(best, val)
    return best

graph = { 'A': ['B', 'C'],
          'B': ['D', 'E'],
          'C': ['F', 'G'],
          'D': [3, 5],
          'E': [6, 9],
          'F': [1, 2],
          'G': [0, -1]
        }

print(minimax('A', True))
