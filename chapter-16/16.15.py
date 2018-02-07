p_i = 0.5 # infection probability
p_r = 0.5 # recovery probability
p_s = 0.5 # severance probability

def update():
    global g
    a = rd.choice(list(g.nodes))
    if g.nodes[a]['state'] == 0: # if susceptible
        if g.degree[a] > 0:
            b = rd.choice(list(g.neighbors(a)))
            if g.nodes[b]['state'] == 1: # if neighbor b is infected
                if random() < p_s:
                    g.remove_edge(a, b)
                else:
                    g.nodes[a]['state'] = 1 if random() < p_i else 0
    else: # if infected
        g.nodes[a]['state'] = 0 if random() < p_r else 1
