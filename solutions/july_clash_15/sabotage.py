import shlex
import heapq

class Edge:
    def __init__(self, fr, to, idx):
        self.fr = fr
        self.to = to
        self.idx = idx

    def __unicode__(self):
        return '{}-{}:{}'.format(self.fr, self.to, self.idx)

def init_graph(M, tokenizer, graph, edge_idxs):
    starting_vertex = None
    for idx in range(1, M + 1):
        fr = int(tokenizer.get_token())
        to = int(tokenizer.get_token())
        e = Edge(fr, to, idx)
        edge_idxs[idx] = e
        l_fr = graph.get(fr)
        if l_fr is None:
            l_fr = []
        l_fr.append(e)
        graph[fr] = l_fr

        l_to = graph.get(to)
        if l_to is None:
            l_to = []
        l_to.append(e)
        graph[to] = l_to

        starting_vertex = fr

    return starting_vertex


tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

N = int(tokenizer.get_token())
M = int(tokenizer.get_token())

graph = {}
edge_idxs = {}

starting_vertex = init_graph(M, tokenizer, graph, edge_idxs)

front_edge_idxs = []
visited_vertexes = set()
mst_idx_edges = set()

visited_vertexes.add(starting_vertex)
for edge in graph[starting_vertex]:
    heapq.heappush(front_edge_idxs, -edge.idx)

while len(visited_vertexes) < N:
    edge_max_idx = heapq.heappop(front_edge_idxs)
    edge_with_max_idx = edge_idxs[-edge_max_idx]
    while edge_with_max_idx.fr in visited_vertexes and edge_with_max_idx.to in visited_vertexes:
        edge_max_idx = heapq.heappop(front_edge_idxs)
        edge_with_max_idx = edge_idxs[-edge_max_idx]
    mst_idx_edges.add(edge_with_max_idx.idx)

    vertex_to_add = edge_with_max_idx.fr if edge_with_max_idx.to in visited_vertexes else edge_with_max_idx.to
    visited_vertexes.add(vertex_to_add)
    for edge in graph[vertex_to_add]:
        if not (edge.fr in visited_vertexes and edge.to in visited_vertexes):
            heapq.heappush(front_edge_idxs, -edge.idx)

result = [idx for idx in range(1, M+1) if idx not in mst_idx_edges]
print len(result)
print '\n'.join([str(idx) for idx in result])