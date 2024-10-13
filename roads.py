import networkx as nx
import matplotlib.pyplot as plt

# Створення нового графа
G = nx.Graph()

# Додавання вершин
intersections = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(intersections)

# Додавання ребер з вагами
edges = [
    ('A', 'B', 3),
    ('A', 'C', 1),
    ('B', 'C', 7),
    ('B', 'D', 5),
    ('C', 'D', 2),
    ('C', 'E', 6),
    ('D', 'E', 1),
    ('D', 'F', 2),
    ('E', 'F', 4)
]
G.add_weighted_edges_from(edges)

# Застосування алгоритму Дейкстри для знаходження найкоротшого шляху
shortest_paths = {}
for intersection in intersections:
    shortest_paths[intersection] = nx.single_source_dijkstra_path(G, intersection)

# Вивід найкоротших шляхів
for source, paths in shortest_paths.items():
    print(f"Шляхи від перехрестя {source}:")
    for destination, path in paths.items():
        print(f"  до {destination}: {path}")

# Візуалізація графа з вагами
edge_labels = nx.get_edge_attributes(G, 'weight')
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title('City Road Map with Weights')
plt.show()
