def order(graph):
    graph = set(graph)
    ordering = []
    possibilities = list({edge[0] for edge in graph} - {edge[1] for edge in graph})

    while len(possibilities) != 0:
        ordering.append(possibilities[0])

        temp_nodes = []
        for edge in filter(lambda e: e[0] == possibilities[0], graph):
            graph.remove(edge)
            temp_nodes.append(edge[1])

        for node in temp_nodes:
            if node not in {edge[1] for edge in graph}:
                possibilities.append(node)

        possibilities = possibilities[1:]

    return ordering


def longest_path(graph, edges, source, sink):
    top_order = order(graph.keys())
    top_order = top_order[top_order.index(source) + 1:top_order.index(sink) + 1]

    S = {node: -100 for node in {edge[0] for edge in graph.keys()} | {edge[1] for edge in graph.keys()}}
    S[source] = 0
    backtrack = {node: None for node in top_order}

    for node in top_order:
        try:
            S[node], backtrack[node] = max(
                map(lambda e: [S[e[0]] + graph[e], e[0]], filter(lambda e: e[1] == node, graph.keys())),
                key=lambda p: p[0])
        except ValueError:
            pass

    path = [sink]
    while path[0] != source:
        path = [backtrack[path[0]]] + path

    return S[sink], path