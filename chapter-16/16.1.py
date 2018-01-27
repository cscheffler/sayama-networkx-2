def initialize():
    global g, nextg
    g = nx.karate_club_graph()
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < .5 else 0
    nextg = g.copy()
    g.pos = nextg.pos = nx.spring_layout(g)
