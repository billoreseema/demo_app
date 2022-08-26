import networkx as nx
from matplotlib import pyplot as plt

graph = nx.DiGraph()
graph.add_edges_from([("node1", "master"), ("node2", "master"), ("node3", "master"),
                      ("cart", "node1"), ("cat", "node1"),("dispatch", "node1"),("mongo", "node1"),
                      ("redis", "node2"),("shipping", "node2"),("user", "node2"),("web", "node2"),
                    ("mysql", "node3"),("payment", "node3"),("rabbitmq", "node3"),("rating", "node2"),
                    ("cartapi", "cart"), ("catapi", "cat"),
                    ("shippingapi", "shipping"),("userapi", "user"),("UI", "web"),
                    ("cat", "mongo"),
                    ("user", "mysql"),("shipping", "mysql"),
                    ("cart", "rabbitmq"),("cart", "redis"),("UI", "payment"),
                      ("UI", "cartapi"), ("UI", "catapi"),("UI", "shippingapi"),("UI", "userapi")])
graph.nodes() # => NodeView(('root', 'a', 'b', 'e', 'c', 'd'))
nx.shortest_path(graph, 'UI', 'mysql') # => ['root', 'a', 'e']
print(nx.dag_longest_path(graph)) # => ['root', 'a', 'b', 'd', 'e']
list(nx.topological_sort(graph)) # => ['root', 'a', 'b', 'd', 'e', 'c']
print(nx.is_directed_acyclic_graph(graph)) # => True
print(nx.is_directed(graph))
print(nx.shortest_path(graph, 'UI', 'master'))
plt.tight_layout()
nx.draw_networkx(graph, arrows=True)
plt.savefig("graph.png", format="PNG")
plt.clf()

graph2 = nx.DiGraph()
graph2.add_edges_from([("node1", "master"), ("node2", "master"), ("node3", "master"),
                      ("cart", "node1"), ("cat", "node1"),("dispatch", "node1"),("mongo", "node1"),
                      ("redis", "node2"),("shipping", "node2"),("user", "node2"),("web", "node2"),
                    ("mysql", "node3"),("payment", "node3"),("rabbitmq", "node3"),("rating", "node2"),
                    ("cartapi", "cart"), ("catapi", "cat"),
                    ("shippingapi", "shipping"),("userapi", "user"),("UI", "web"),
                    ("cat", "mongo"),
                    ("user", "mysql"),("shipping", "mysql"),
                    ("cart", "rabbitmq"),("cart", "redis"),("UI", "payment"),
                      ("UI", "cartapi"), ("UI", "catapi"),("UI", "shippingapi"),("UI", "userapi")])
graph2.nodes() # => NodeView(('root', 'a', 'b', 'e', 'c', 'd'))
nx.shortest_path(graph2, 'UI', 'mysql') # => ['root', 'a', 'e']
print(nx.dag_longest_path(graph2)) # => ['root', 'a', 'b', 'd', 'e']
list(nx.topological_sort(graph2)) # => ['root', 'a', 'b', 'd', 'e', 'c']
print(nx.is_directed_acyclic_graph(graph2)) # => True
print(nx.is_directed(graph2))
print(nx.shortest_path(graph2, 'UI', 'master'))
plt.tight_layout()
nx.draw_networkx(graph, arrows=True)
plt.savefig("graph2.png", format="PNG")
plt.clf()