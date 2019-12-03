from collections import defaultdict
LOG = False

class UnlabeledGraph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        if LOG:
            print('Adding edge {}->{} to unlabeled graph {}'.format(u, v))
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []

    def scc_decompose(self):
        stack = []
        node_keys = [*self.graph]
        visited = [False] * len(node_keys)
        print(node_keys)
        for i in range(len(node_keys)):
            if visited[i] == False:
                self.fill_order(i, visited, stack, node_keys)

        gr = self._get_transpose()
        print(gr.graph)
        print(stack)

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * len(node_keys)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited, node_keys)
                print()


    # A function used by DFS
    def DFSUtil(self, v, visited, node_keys):
        # Mark the current node as visited and print it
        visited[v] = True
        print(node_keys[v])

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[node_keys.index(i)] == False:
                self.DFSUtil(node_keys.index(i), visited, node_keys)

    def fill_order(self, v, visited, stack, node_keys):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[node_keys.index(i)] == False:
                self.fill_order(node_keys.index(i), visited, stack, node_keys)
        stack = stack.append(v)
        # Function that returns reverse (or transpose) of this graph

    def _get_transpose(self):
        g = UnlabeledGraph()
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

        # The main function that finds and prints all strongly

