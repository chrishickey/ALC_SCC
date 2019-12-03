from labeled_graph import LabeledGraph
from alc_decomposed import AlcDecomposed
import sys


def main():
    try:
        graph_file = sys.argv[1]
    except:
        graph_file = 'graph.txt'
    labeled_graph = LabeledGraph.get_graph_from_file(graph_file)
    alc_decomposed_graph = AlcDecomposed.decompose_labeled_graph(labeled_graph)
    print(alc_decomposed_graph.unlabeledGraphs[(1,)].graph)
    alc_decomposed_graph.unlabeledGraphs[(1,)].scc_decompose()


if __name__ == '__main__':
    main()