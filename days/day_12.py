from typing import List, Dict


def part_1(data: List[str]):
    graph = make_graph(data)
    paths = find_paths('start', graph, [], [], False)

    return len(paths)


def part_2(data: List[str]):
    graph = make_graph(data)
    paths = find_paths('start', graph, [], [], True)

    return len(paths)


def make_graph(connections: List[str]):
    graph = {}

    for con in connections:
        a, b = con.split('-')
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]

    return graph


def find_paths(cur_node: str, graph: Dict[str, List[str]], visited: List[str], paths: List[List[str]], extra_small: bool):
    visited.append(cur_node)

    if cur_node == 'end':
        paths.append(visited)

    for node in graph[cur_node]:
        if extra_small:
            extra = node not in ['start', 'end'] and node.islower() and not any([n.islower() and visited.count(n) > 1 for n in visited])

        if node not in visited or (node in visited and (node.isupper() or (extra_small and extra))):
            find_paths(node, graph, visited.copy(), paths, extra_small)

    return paths
