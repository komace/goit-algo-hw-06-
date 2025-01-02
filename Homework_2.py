import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Дадаємо вершини представлені як локації в місті
nodes = ['A', 'B', 'C', 'D', 'E','F']
G.add_nodes_from(nodes)

# Додаємо ребра між вершинам як відстань між локаціями
edges = [('A', 'B'), ('A', 'C'),('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('E', 'F')]
G.add_edges_from(edges)

# Створюємо функцію для пошуку шляхів dfs
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    print(stack)
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Створюємо функцію для пошуку шляхів bfs               
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


start = 'A'
goal = 'F'

# Знаходимо шляхи з вершини start до вершини goal за допомогою dfs та bfs
dfs_result = list(dfs_paths(G, start, goal))
bfs_result = list(bfs_paths(G, start, goal))

print(f"DFS шляхи з {start} до {goal}:")
for path in dfs_result:
    print(path)

print(f"BFS шляхи з {start} до {goal}:")
for path in bfs_result:
    print(path)
