>>> import networkx as nx
>>> g = nx.DiGraph()
>>> g.add_edges_from([(0,1), (0,2), (0,3), (1,2), (2,3), (3,0)])
>>> nx.degree_assortativity_coefficient(g, x = 'in', y = 'in')
-0.250000000000001
>>> nx.degree_assortativity_coefficient(g, x = 'in', y = 'out')
0.63245553203367555
>>> nx.degree_assortativity_coefficient(g, x = 'out', y = 'in')
0.0
>>> nx.degree_assortativity_coefficient(g, x = 'out', y = 'out')
-0.44721359549995793
