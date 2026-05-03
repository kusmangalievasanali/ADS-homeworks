from collections import deque
import heapq

# Task 1
graph = {
    'A': ['C', 'B', 'D'],
    'B': ['A', 'C', 'E', 'G'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'A'],
    'E': ['G', 'F', 'B'],
    'F': ['G', 'E'],
    'G': ['F', 'B']
}


def dfs(graph, start):
    visited = set()

    def dfs_visit(node):
        if node in visited:
            return

        visited.add(node)
        print(node, end=' ')

        for neighbor in graph[node]:
            dfs_visit(neighbor)

    dfs_visit(start)


print("Task 1 — DFS:")
dfs(graph, 'A')

print("\n")



# Task 2
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()

        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("Task 2 — BFS:")
bfs(graph, 'A')

print("\n")



# Task 3
print("Task 3 — DFS Output:")
dfs(graph, 'A')

print("\nMatches Task 1 DFS result")

print("\nTask 3 — BFS Output:")
bfs(graph, 'A')

print("\nMatches Task 2 BFS result")



# Task 4
road_graph = {
    'Edinburgh': {
        'Perth': 100,
        'Glasgow': 70
    },

    'Glasgow': {
        'Edinburgh': 70,
        'Perth': 90,
        'Dundee': 150
    },

    'Perth': {
        'Edinburgh': 100,
        'Glasgow': 90,
        'Dundee': 40
    },

    'Dundee': {
        'Perth': 40,
        'Glasgow': 150
    }
}


def dijkstra(graph, start, end):


    distances = {node: float('inf') for node in graph}
    distances[start] = 0


    previous = {}

    pq = [(0, start)]

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                previous[neighbor] = current_node

                heapq.heappush(pq, (distance, neighbor))


    path = []
    current = end

    while current in previous:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return distances[end], path


distance, path = dijkstra(
    road_graph,
    'Edinburgh',
    'Dundee'
)

print("Task 4 — Shortest Path:")
print("Shortest distance:", distance)
print("Path:", " -> ".join(path))