class AlcSccDecomposed(object):

    def __init__(self, unlabeled_graphs):
        self.alc_scc_decomposed_graphs = {label_set: unlabeled_graph.scc_decompose() for label_set, unlabeled_graph in unlabeled_graphs.items()}


    def lcr_query(self, s, t, labels):
        return self.alc_scc_decomposed_graphs[labels].reachability_query(s, t)
