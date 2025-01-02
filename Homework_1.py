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

# Друкуємо граф
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='yellow', 
font_size=20, font_color='black', font_weight='bold', font_family='sans-serif', edge_color='blue', width=2, style='dashed', alpha=0.8)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Аналізуємо базові характеристики графа
num_nodes = G.number_of_nodes()
print(f"Кількість вершин: {num_nodes}")
num_edges = G.number_of_edges()
print(f"Кількість ребер: {num_edges}")
degree_of_nodes = G.degree()
for node, degree in degree_of_nodes:
    print(f"Вершина {node} має ступінь {degree}")
