>>> g = nx.DiGraph()
>>> g.add_edge('Josh', 'Jess')
>>> g.edge['Josh']['Jess']['love'] = True
>>> g.edge
{'Jess': {}, 'Josh': {'Jess': {'love': True}}}
>>> g.edge['Jess']['Josh']['love']

Traceback (most recent call last):
File "<pyshell#16>", line 1, in <module>
  g.edge['Jess']['Josh']['love']
KeyError: 'Josh'
>>>
