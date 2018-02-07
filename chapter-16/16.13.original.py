p_i = 0.5 # infection probability
p_r = 0.5 # recovery probability

def update():
    global g
    a = rd.choice(g.nodes())
    if g.node[a][’state’] == 0: # if susceptible
        b = rd.choice(g.neighbors(a))
        if g.node[b][’state’] == 1: # if neighbor b is infected
            g.node[a][’state’] = 1 if random() < p_i else 0
    else: # if infected
        g.node[a][’state’] = 0 if random() < p_r else 1
