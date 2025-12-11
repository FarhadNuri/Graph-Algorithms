import heapq

def fp(came_from, node):
    path = [node]
    while came_from[node] is not None:
        node = came_from[node]
        path.insert(0, node)
    return path


def a_star(graph, h, st, end):
    open = []
    g_cost = {st: 0}

    st_cost = (h.get(st, float('inf')), st)  # f = g + h = 0 + h
    heapq.heappush(open, st_cost)

    came_from = {st: None}

    while open:
        node = heapq.heappop(open)
        cur = node[1]

        if cur == end:
            path = fp(came_from, cur)
            total = 0
            for i in range(len(path) - 1):
                total += graph[path[i]][path[i + 1]]

            return path, total

        for neighbor, weight in graph[cur].items():
            new_g = g_cost[cur] + weight  # g(n) update

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g

                # A* priority f = g + h
                f = new_g + h.get(neighbor, float('inf'))

                cost_pair = (f, neighbor)
                heapq.heappush(open, cost_pair)

                came_from[neighbor] = cur

    return None,0



# --- Heuristic Data (Straight-Line Distance to Bucharest) ---
h = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

# --- Graph Representation (Weighted Adjacency List) ---
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


start = 'Arad'
goal = 'Bucharest'

final_path, astar_cost = a_star(graph, h, start, goal)

if final_path is not None:
    print(f"A* Path: {' -> '.join(final_path)}")
    print("A* Total Cost:", astar_cost)
else:
    print("No path found")
