import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (станції метро Києва)
stations = [
    'Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut',
    'Vokzalna', 'Universytet', 'Teatralna', 'Khreshchatyk', 'Arsenalna', 'Dnipro', 'Hidropark', 'Livoberezhna',
    'Darnytsia', 'Chernihivska', 'Lisova', 'Heroiv Dnipra', 'Minska', 'Obolon', 'Pochaina', 'Tarasa Shevchenka',
    'Kontraktova Ploshcha', 'Poshtova Ploshcha', 'Maidan Nezalezhnosti', 'Ploshcha Lva Tolstoho', 'Olimpiiska',
    'Palats Ukraina', 'Lybidska', 'Demiivska', 'Holosiivska', 'Vasylkivska', 'Vystavkovyi Tsentr', 'Ipodrom',
    'Teremky', 'Syrets', 'Dorohozhychi', 'Lukianivska', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska',
    'Druzhby Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky', 'Kharkivska', 'Vyrlytsia', 'Boryspilska',
    'Chervony Khutir'
]
G.add_nodes_from(stations)

# Додавання ребер (лінії метро між станціями)
edges = [
    # Червона лінія (M1)
    ('Akademmistechko', 'Zhytomyrska'), ('Zhytomyrska', 'Sviatoshyn'), ('Sviatoshyn', 'Nyvky'), ('Nyvky', 'Beresteiska'),
    ('Beresteiska', 'Shuliavska'), ('Shuliavska', 'Politekhnichnyi Instytut'), ('Politekhnichnyi Instytut', 'Vokzalna'),
    ('Vokzalna', 'Universytet'), ('Universytet', 'Teatralna'), ('Teatralna', 'Khreshchatyk'), ('Khreshchatyk', 'Arsenalna'),
    ('Arsenalna', 'Dnipro'), ('Dnipro', 'Hidropark'), ('Hidropark', 'Livoberezhna'), ('Livoberezhna', 'Darnytsia'),
    ('Darnytsia', 'Chernihivska'), ('Chernihivska', 'Lisova'),

    # Синя лінія (M2)
    ('Heroiv Dnipra', 'Minska'), ('Minska', 'Obolon'), ('Obolon', 'Pochaina'), ('Pochaina', 'Tarasa Shevchenka'),
    ('Tarasa Shevchenka', 'Kontraktova Ploshcha'), ('Kontraktova Ploshcha', 'Poshtova Ploshcha'),
    ('Poshtova Ploshcha', 'Maidan Nezalezhnosti'), ('Maidan Nezalezhnosti', 'Ploshcha Lva Tolstoho'),
    ('Ploshcha Lva Tolstoho', 'Olimpiiska'), ('Olimpiiska', 'Palats Ukraina'), ('Palats Ukraina', 'Lybidska'),
    ('Lybidska', 'Demiivska'), ('Demiivska', 'Holosiivska'), ('Holosiivska', 'Vasylkivska'),
    ('Vasylkivska', 'Vystavkovyi Tsentr'), ('Vystavkovyi Tsentr', 'Ipodrom'), ('Ipodrom', 'Teremky'),

    # Зелена лінія (M3)
    ('Syrets', 'Dorohozhychi'), ('Dorohozhychi', 'Lukianivska'), ('Lukianivska', 'Zoloti Vorota'),
    ('Zoloti Vorota', 'Palats Sportu'), ('Palats Sportu', 'Klovska'), ('Klovska', 'Pecherska'),
    ('Pecherska', 'Druzhby Narodiv'), ('Druzhby Narodiv', 'Vydubychi'), ('Vydubychi', 'Slavutych'),
    ('Slavutych', 'Osokorky'), ('Osokorky', 'Pozniaky'), ('Pozniaky', 'Kharkivska'), ('Kharkivska', 'Vyrlytsia'),
    ('Vyrlytsia', 'Boryspilska'), ('Boryspilska', 'Chervony Khutir'),

    # Пересадки
    ('Teatralna', 'Zoloti Vorota'),  # Пересадка між червоною та зеленою лініями
    ('Khreshchatyk', 'Maidan Nezalezhnosti'),  # Пересадка між червоною та синьою лініями
    ('Palats Sportu', 'Ploshcha Lva Tolstoho')  # Пересадка між синьою та зеленою лініями
]
G.add_edges_from(edges)

plt.figure(figsize=(12, 10))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', font_size=5, font_weight='bold')
plt.title('Kyiv Metro Map')
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")
