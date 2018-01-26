>>> g.edge['Jeff']['Jane']['trust'] = 1.0
>>> g.edge['Josh']['Jess']['love'] = True
>>> g.edge['Jess']['Josh']['love']
True
>>> g.edge
{
    'Jeff': {'Jane': {'trust': 1.0}, 'Jill': {}},
    'Josh': {'Jess': {'love': True}},
    'Jess': {'Jill': {}, 'Josh': {'love': True}},
    'Jill': {'Jess': {}, 'Jeff': {}},
    'Jack': {'Jane': {}},
    'Jane': {'Jack': {}, 'Jeff': {'trust': 1.0}}
}
