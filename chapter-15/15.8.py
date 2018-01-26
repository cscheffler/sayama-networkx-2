>>> g = nx.DiGraph()
>>> g.add_edge('Josh', 'Jess')
>>> g.edges['Josh', 'Jess']['love'] = True
>>> dict(g.edges)
{('Josh', 'Jess'): {'love': True}}
>>> g.edges['Jess', 'Josh']['love']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/lib/python2.7/site-packages/networkx/classes/reportviews.py", line 930, in __getitem__
    return self._adjdict[u][v]
KeyError: 'Josh'
>>>
