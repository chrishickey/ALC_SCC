
class SccDecomposedGraph:

    def __init__(self, vertices):
        self.vertex_to_scc_dict = {vertex: None for vertex in vertices}
        self.scc_graph = {}

    def setup(self, sccs, out_vertices):
        for scc_id in range(len(sccs)):
            for vertex in sccs[scc_id]:
                self.vertex_to_scc_dict[vertex] = scc_id
            self.scc_graph[scc_id] = []

        for scc_id in range(len(out_vertices)):
            for vertex in out_vertices[scc_id]:
                if self.vertex_to_scc_dict[vertex] not in self.scc_graph[scc_id]:
                    self.scc_graph[scc_id].append(self.vertex_to_scc_dict[vertex])

    def reachability_query(self, s, t):
        s_sccid, t_sccid = self.vertex_to_scc_dict[s], self.vertex_to_scc_dict[t]
        queue = []
        queue.append(s_sccid)
        visited = {id: False for id in self.scc_graph}
        while queue:
            current_ssc = queue.pop(0)
            visited[current_ssc] = True
            if current_ssc == t_sccid:
                return True
            for scc_id in self.scc_graph[current_ssc]:
                if visited[scc_id] == False:
                    queue.append(scc_id)
        return False




