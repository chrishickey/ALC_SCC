from itertools import combinations
from unlabeled_graph import UnlabeledGraph

class AlcDecomposed(object):

    def __init__(self, label_set):
        self.unlabeledGraphs = {tuple(sorted(i)): UnlabeledGraph(tuple(sorted(i))) for j in range(1, len(label_set)+1)
                                    for i in combinations(label_set, j)}


    @classmethod
    def decompose_labeled_graph(cls, labeled_graph):
        decomposed_graph = AlcDecomposed(labeled_graph.label_set)
        for l_dash in decomposed_graph.unlabeledGraphs.keys():
            if len(l_dash) == 1:
                for source, vert_obj in labeled_graph.vertices.items():
                    for target, edge_label in vert_obj.edges:
                        if l_dash[0] == edge_label:
                            decomposed_graph.unlabeledGraphs[l_dash].add_edge(source, target)
            else:
                for label in l_dash:
                    for source, targets in decomposed_graph.unlabeledGraphs[(label,)].graph.items():
                        for target in targets:
                            decomposed_graph.unlabeledGraphs[l_dash].add_edge(source, target)

        assert len(decomposed_graph.unlabeledGraphs) == (2 ** len(labeled_graph.label_set) - 1)
        return decomposed_graph


