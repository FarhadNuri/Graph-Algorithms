import heapq

def path_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    return cost

def fp(came_from,goal):
    path =[goal]
    while came_from[goal] is not None:
        goal =came_from[goal]
        path.insert(0,goal)
    return path

def aStar(graph,h,st,en):
    open=[]
    st_cost=h[st], st
    heapq.heappush(open, st_cost)

    g_approx={st:0}
    came_from={st:None}

    while open:

        node = heapq.heappop(open)
        cur = node[1]

        if cur == en:
            return fp(came_from,cur)

        for nei in graph[cur]:
            gcost = g_approx[cur] + graph[cur][nei]

            if nei not in g_approx or gcost < g_approx[nei]:
                g_approx[nei] = gcost

                f = gcost + h[nei]
                heapq.heappush(open,(f,nei))

                came_from[nei]=cur

    return None

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

final_path = aStar(graph, h, start, goal)

if final_path:
    total_cost = path_cost(final_path, graph)
    print("Path:", " -> ".join(final_path))
    print("Cost:", total_cost)
