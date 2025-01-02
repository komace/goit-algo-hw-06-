import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Дадаємо вершини представлені як локації в місті
nodes = ['A', 'B', 'C', 'D', 'E','F']
G.add_nodes_from(nodes)

# Додаємо ребра між вершинам як відстань між локаціями
edges = [('A', 'B', 1), ('A', 'C', 5),('B', 'C', 2), ('B', 'D', 4), ('C', 'D', 1), ('C', 'E', 3), ('D', 'E', 2), ('E', 'F', 1)]

G.add_weighted_edges_from(edges)

# Створюємо функцію для ініціалізації відстаней попередніх вершин
def dijkstra_paths(graph, source):
    distances = {vertex: float('infinity') for vertex in graph}
    previous_vertices = {vertex: None for vertex in graph}
    distances[source] = 0
    unvisited = list(graph.nodes)
    # Знаходимо вершину з найменшою відстанню
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо відстань до поточної вершини - нескінченність, то виходимо з циклу
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor, weight in graph[current_vertex].items():
            alternative_route = distances[current_vertex] + weight.get['weight']

            # Якщо альтернативний шлях коротший, то змінюємо відстань та попередню вершину
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex
        # видаляємо поточну вершину зі списку невідвіданих
        unvisited.remove(current_vertex)    
# Відновлюємо шлях та відстані
    path = {vertex: [] for vertex in graph}
    for vertex in graph:
        current = vertex
        while current is not None:
            path[vertex].insert(0, current)
            current = previous_vertices[current]
    return path, distances

# Знаходимо найкоротші шляхи для всіх вершин
    shortest_distances = {}
    shortest_paths = {}
    for node in G.nodes():
        distances, paths = dijkstra_paths(G, node)
        shortest_distances[node] = distances
        shortest_paths[node] = paths

    for start_node in shortest_paths:
        print(f"Найкоротший шлях від {start_node}")
        for end_node in shortest_paths[start_node]:
            print(f"Шлях до вершини {end_node} має відстань {shortest_distances[start_node][end_node]}: {shortest_paths[start_node][end_node]}")          
        print()

def nx_dijkstra_paths(graph, source):
    return nx.single_source_dijkstra_path(graph, source)


# Знаходимо найкоротші шляхи для всіх вершин
shortest_paths = {node: nx_dijkstra_paths(G, node) for node in G.nodes()}  

for start_node in shortest_paths:
    print(f"Найкоротший шлях від {start_node}")
    for end_node in shortest_paths[start_node]:
        print(f"Шлях до вершини {end_node} має відстань {shortest_paths[start_node][end_node]}: {shortest_paths[start_node][end_node]}")          
    print() 
    
# Відображення графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='yellow', font_size=20,font_color="black", edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()        