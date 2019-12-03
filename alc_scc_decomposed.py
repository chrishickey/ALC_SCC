LOG = True
class AlcSccDecomposed(object):

    def __init__(self, unlabeled_graphs):
        self.alc_scc_decomposed_graphs = {label_set: unlabeled_graph.scc_decompose() for label_set, unlabeled_graph in unlabeled_graphs.items()}
        for label_set in  self.alc_scc_decomposed_graphs:
            if LOG:
                print('Fully processed graphs for the following sets {}'.format(label_set))
                print('Number of SCCS in label set {} is {}'.format(label_set, len(self.alc_scc_decomposed_graphs[label_set].scc_graph)))

    def lcr_query(self, s, t, labels):
        return self.alc_scc_decomposed_graphs[labels].reachability_query(s, t)
