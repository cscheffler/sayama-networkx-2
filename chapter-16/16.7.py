alpha = 1 # diffusion constant
Dt = 0.01 # Delta t

def update():
    global g, nextg
    for i in g.nodes:
        ci = g.nodes[i]['state']
        nextg.nodes[i]['state'] = ci + alpha * (
            sum(g.nodes[j]['state'] for j in g.neighbors(i))
            - ci * g.degree[i]) * Dt
    g, nextg = nextg, g
