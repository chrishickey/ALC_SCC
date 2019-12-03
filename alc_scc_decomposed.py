LOG = 0
import os
from collections import defaultdict


class AlcSccDecomposed(object):

    def __init__(self, unlabeled_graphs):
        self.alc_scc_decomposed_graphs = {label_set: unlabeled_graph.scc_decompose() for label_set, unlabeled_graph in unlabeled_graphs.items()}
        for label_set in  self.alc_scc_decomposed_graphs:
            if 1:
                print('Fully processed graphs for the following sets {}'.format(label_set))
                print('Number of SCCS in label set {} is {}'.format(label_set, len(self.alc_scc_decomposed_graphs[label_set].scc_graph)))

    def lcr_query(self, s, t, labels):
        return self.alc_scc_decomposed_graphs[labels].reachability_query(s, t)

    def write_graph(self, directory):
        for label_set in  self.alc_scc_decomposed_graphs:
            vertex_map_fname = '{}_map.txt'.format('_'.join(str(i) for i in list(label_set)))
            ssc_id_fname = '{}_graph.txt'.format('_'.join(str(i) for i in list(label_set)))
            map_dict = defaultdict(list)
            for v, ssc_id in self.alc_scc_decomposed_graphs[label_set].vertex_to_scc_dict.items():
                map_dict[ssc_id].append(v)
            with open(os.path.join(directory, vertex_map_fname), 'w') as f:
                for ssc_id, vertices in map_dict.items():
                    f.write('{} {}\n'.format(ssc_id, ' '.join(str(i) for i in vertices)))
            with open(os.path.join(directory, ssc_id_fname), 'w') as f:
                for ssc_id, out_portals in self.alc_scc_decomposed_graphs[label_set].scc_graph.items():
                    f.write('{} {}\n'.format(ssc_id, ' '.join(str(i) for i in out_portals)))



