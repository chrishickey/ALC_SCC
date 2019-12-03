from collections import defaultdict
from scc_decomposed import SccDecomposedGraph
LOG = 0

class UnlabeledGraph(object):

    def __init__(self, label_set=None):
        self.graph = defaultdict(list)
        self.label_set = label_set

    def add_edge(self, u, v):
        if LOG and self.label_set:
            print('Adding edge {}->{} to unlabeled graph {}'.format(u, v, self.label_set))
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []

    def scc_decompose(self):
        if LOG:
            print('Graph before decomposition for label set {} is {}'.format(self.label_set, self.graph))
        stack = []
        visited = {vertex: False for vertex in self.graph}
        for i in self.graph:
            if visited[i] == False:
                self.fill_order(i, visited, stack)

        gr = self._get_transpose()

        # Mark all the vertices as not visited (For second DFS)
        visited = {vertex: False for vertex in self.graph}

        # Now process all vertices in order defined by Stack
        scc_decomposition = SccDecomposedGraph(self.graph)
        scc = []
        sccs = []
        scc_out_portals = []
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited, scc)
                out_vertices = self.get_out_vertices(scc)
                sccs.append(scc)
                scc_out_portals.append(out_vertices)
                scc = []
        if LOG:
            print('With label set {} the SCCs are {}'.format(self.label_set, sccs))
        scc_decomposition.setup(sccs, scc_out_portals)
        return scc_decomposition

    def get_out_vertices(self, scc):
        out_vertices = []
        for vertex in scc:
            for v in self.graph[vertex]:
                if v not in scc:
                    out_vertices.append(v)
        return out_vertices

    # A function used by DFS
    def DFSUtil(self, v, visited, scc):
        # Mark the current node as visited and print it
        visited[v] = True
        scc.append(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, scc)

    def fill_order(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fill_order(i, visited, stack)
        stack.append(v)
        # Function that returns reverse (or transpose) of this graph

    def _get_transpose(self):
        g = UnlabeledGraph()
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g
