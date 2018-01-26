>>> g.edges['Jeff', 'Jane']['trust'] = 1.0
>>> g.edges['Josh', 'Jess']['love'] = True
>>> g.edges['Jess', 'Josh']['love']
True
>>> dict(g.edges)
{
    ('Jeff', 'Jill'): {},
    ('Josh', 'Jess'): {'love': True},
    ('Jess', 'Jill'): {},
    ('Jeff', 'Jane'): {'trust': 1.0},
    ('Jack', 'Jane'): {}
}
