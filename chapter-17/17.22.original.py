>>> import networkx as nx
>>> import community as comm
>>> g = nx.karate_club_graph()
>>> bp = comm.best_partition(g)
>>> bp
{0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0, 8: 2, 9: 0, 10: 1,
  11: 0, 12: 0, 13: 0, 14: 2, 15: 2, 16: 1, 17: 0, 18: 2, 19: 0,
  20: 2, 21: 0, 22: 2, 23: 3, 24: 3, 25: 3, 26: 2, 27: 3, 28: 3,
29: 2, 30: 2, 31: 3, 32: 2, 33: 2}
>>> comm.modularity(bp, g)
0.4188034188034188
