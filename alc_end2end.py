from labeled_graph import LabeledGraph
from alc_decomposed import AlcDecomposed
from alc_scc_decomposed import AlcSccDecomposed
import sys


def main():
    try:
        graph_file = sys.argv[1]
    except:
        graph_file = 'graph.txt'
    labeled_graph = LabeledGraph.get_graph_from_file(graph_file)
    alc_decomposed_graph = AlcDecomposed.decompose_labeled_graph(labeled_graph)
    alc_scc_decomposed_graph = AlcSccDecomposed(alc_decomposed_graph.unlabeledGraphs)

    # Test Case for basic graph
    test1_answer = alc_scc_decomposed_graph.lcr_query(2, 9, (1,))
    print('Expected test 1 True=={}'.format(test1_answer))

    test2_answer = alc_scc_decomposed_graph.lcr_query(7, 6, (1,))
    print('Expected test 2 True=={}'.format(test2_answer))

    test3_answer = alc_scc_decomposed_graph.lcr_query(2, 7, (1,))
    print('Expected test 3 False=={}'.format(test3_answer))

if __name__ == '__main__':
    main()