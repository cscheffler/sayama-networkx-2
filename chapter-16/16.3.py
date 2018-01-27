def update():
    global g, nextg
    for i in g.nodes:
        count = g.nodes[i]['state']
        for j in g.neighbors(i):
            count += g.nodes[j]['state']
        ratio = count / (g.degree[i] + 1.0)
        nextg.nodes[i]['state'] = 1 if ratio > .5 \
                                  else 0 if ratio < .5 \
                                  else 1 if random() < .5 else 0
    g, nextg = nextg, g
