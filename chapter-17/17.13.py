>>> from pylab import *
>>> import networkx as nx
>>> g = nx.karate_club_graph()
>>> hist([degree for node, degree in g.degree], bins = 20)
(array([ 1., 11., 6., 6., 0., 3., 2., 0., 0., 0., 1., 1., 0., 1., 0.,
  0., 0., 0., 1., 1.]), array([ 1. , 1.8, 2.6, 3.4, 4.2, 5. , 5.8,
  6.6, 7.4, 8.2, 9. , 9.8, 10.6, 11.4, 12.2, 13. , 13.8, 14.6, 15.4,
  16.2, 17. ]), <a list of 20 Patch objects>)
>>> show()
