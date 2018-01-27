def update():
    global g, nextg
    for i in g.nodes_iter():
        count = g.node[i]['state']
        for j in g.neighbors(i):
            count += g.node[j]['state']
        ratio = count / (g.degree(i) + 1.0)
        nextg.node[i]['state'] = 1 if ratio > .5 \
                                 else 0 if ratio < .5 \
                                 else 1 if random() < .5 else 0
    g, nextg = nextg, g
