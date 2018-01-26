# Major changes in networkx

These are the main changes from networkx 1.x to networkx 2.x that
affect the code in the textbook.

## Accessing node properties

The `node` property of a `Graph` object no longer contains a dict
mapping node names to node properties, but a NodeView object that
behaves like a dict. This means you can still get the properties of a
node using

    g.node['name']

but have to use

    dict(g.nodes)

to get a dict of all nodes with their properties.

Also note that the `node` and `nodes` are now equivalent with both
returning the same NodeView object.


## Accessing edges properties

The `edge` property no longer exists. You can now see all edges using

    dict(g.edges)

This returns different output from the old `g.edge`, namely 2-tuples
of edge source and target pairs, rather than a mapping from the source
node to all destination nodes that are neighbors. Use

    g.edges['source', 'target']

to access the properties of a particular edge.
