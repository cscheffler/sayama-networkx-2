import networkx as nx
g = nx.complete_graph(5)
nx.write_adjlist(g, 'complete-graph.txt')
