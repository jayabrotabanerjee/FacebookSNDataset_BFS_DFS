import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('facebook_combined.csv', header=None, names=['edge'])
G = nx.Graph()
for index, row in df.iterrows():
    edge = row['edge'].split()
    user_id = int(edge[0])
    friend_id = int(edge[1])
    G.add_edge(user_id, friend_id)

def bfs_shortest_path(G, start_node, end_node):
    queue = [(start_node, [start_node])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for neighbor in G.neighbors(node):
                if neighbor == end_node:
                    return path + [neighbor]
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

start_node = 1
end_node = 100
path = bfs_shortest_path(G, start_node, end_node)
print("BFS Shortest Path:", path)

def dfs_shortest_path(G, start_node, end_node):
    stack = [(start_node, [start_node])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in G.neighbors(node):
                if neighbor == end_node:
                    return path + [neighbor]
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

start_node = 1
end_node = 100
path = dfs_shortest_path(G, start_node, end_node)
print("DFS Shortest Path:", path)

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=5000)
plt.show()

def find_most_connected_nodes(G, num_nodes):
    degrees = [(node, G.degree(node)) for node in G.nodes()]
    degrees.sort(key=lambda x: x[1], reverse=True)
    return [node for node, degree in degrees[:num_nodes]]

num_nodes = 10
most_connected_nodes = find_most_connected_nodes(G, num_nodes)
print("Most Connected Nodes:", most_connected_nodes)