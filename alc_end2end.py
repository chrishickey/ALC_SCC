from labeled_graph import LabeledGraph
from alc_decomposed import AlcDecomposed
from alc_scc_decomposed import AlcSccDecomposed
import sys, time


def main():
    try:
        graph_file = sys.argv[1]
        # For DFS recursion is very high
        sys.setrecursionlimit(10**6)
    except:
        graph_file = 'V5D5L8exp.txt'
    start_time = time.time()
    labeled_graph = LabeledGraph.get_graph_from_file(graph_file)
    alc_decomposed_graph = AlcDecomposed.decompose_labeled_graph(labeled_graph)
    alc_scc_decomposed_graph = AlcSccDecomposed(alc_decomposed_graph.unlabeledGraphs)
    end_time = time.time()
    print('Construction time is {}'.format(end_time - start_time))
    # Test Case for basic graph
    test1_answer = alc_scc_decomposed_graph.lcr_query(2, 9, (1,))
    print('Expected test 1 True=={}'.format(test1_answer))

    test2_answer = alc_scc_decomposed_graph.lcr_query(7, 6, (1,))
    print('Expected test 2 True=={}'.format(test2_answer))

    test3_answer = alc_scc_decomposed_graph.lcr_query(2, 7, (1,))
    print('Expected test 3 False=={}'.format(test3_answer))

    test4_answer = alc_scc_decomposed_graph.lcr_query(6, 4, (1, 2))
    print('Expected test 4 True=={}'.format(test4_answer))

    test5_answer = alc_scc_decomposed_graph.lcr_query(6, 2, (0, 1))
    print('Expected test 5 False=={}'.format(test5_answer))

    print('Total number of constructed graphs {}'.format(len(alc_scc_decomposed_graph.alc_scc_decomposed_graphs)))


if __name__ == '__main__':
    main()