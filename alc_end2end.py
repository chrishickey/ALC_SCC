from labeled_graph import LabeledGraph
from alc_decomposed import AlcDecomposed
from alc_scc_decomposed import AlcSccDecomposed
import sys, time, datetime
TEST_LABEL_SIZE = 6
TEST_SET_SIZE = 2000


def main():
    try:
        graph_file = sys.argv[1]
    except:
        graph_file = 'V5kD5L8exp.edge'

    labeled_graph = LabeledGraph.get_graph_from_file(graph_file)
    ttc, ftc = labeled_graph.get_test_cases(label_size=TEST_LABEL_SIZE, number=TEST_SET_SIZE)
    print('Found {} true test cases and {} false test case'.format(len(ttc), len(ftc)))

    start_time = time.time()
    alc_decomposed_graph = AlcDecomposed.decompose_labeled_graph(labeled_graph)
    alc_scc_decomposed_graph = AlcSccDecomposed(alc_decomposed_graph.unlabeledGraphs)
    end_time = time.time()
    print('Construction time is {}'.format(end_time - start_time))

    # Free memory space
    del alc_decomposed_graph
    del labeled_graph

    start = datetime.datetime.now()
    for source, target, query_set in ttc:
        answer = alc_scc_decomposed_graph.lcr_query(source, target, query_set)
        assert answer == True
    end = datetime.datetime.now()
    average = (end - start).microseconds / len(ttc)
    print('Average time for true queries {} microseconds after {} questions'.format(average, len(ttc)))

    start = datetime.datetime.now()
    for source, target, query_set in ftc:
        answer = alc_scc_decomposed_graph.lcr_query(source, target, query_set)
        assert answer == False
    end = datetime.datetime.now()
    average = (end - start).microseconds / len(ftc)
    print('Average time for false queries {} microseconds after {} questions'.format(average, len(ftc)))


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    main()
