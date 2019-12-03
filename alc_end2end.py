from labeled_graph import LabeledGraph
from alc_decomposed import AlcDecomposed
from alc_scc_decomposed import AlcSccDecomposed
import sys, time, datetime


def main():
    try:
        graph_file = sys.argv[1]
        # For DFS recursion is very high
        sys.setrecursionlimit(10**6)
    except:
        graph_file = 'graph.txt'
    start_time = time.time()
    labeled_graph = LabeledGraph.get_graph_from_file(graph_file)
    ttc, ftc = labeled_graph.get_test_cases(label_size=2, number=1000)
    print('Found {} true test cases and {} false test case'.format(len(ttc), len(ftc)))
    alc_decomposed_graph = AlcDecomposed.decompose_labeled_graph(labeled_graph)
    alc_scc_decomposed_graph = AlcSccDecomposed(alc_decomposed_graph.unlabeledGraphs)
    end_time = time.time()
    print('Construction time is {}'.format(end_time - start_time))


    true_answer_times = []
    for source, target, query_set in ttc:
        start = datetime.datetime.now()
        answer = alc_scc_decomposed_graph.lcr_query(source, target, query_set)
        end = datetime.datetime.now()
        assert answer == True
        start = datetime.datetime.now()
        end = datetime.datetime.now()
        true_answer_times.append((start - end).microseconds)
    average = sum(true_answer_times) / len(true_answer_times)
    print('Average time for true queries {}'.format(average))

    false_answer_times = []
    for source, target, query_set in ftc:
        start = datetime.datetime.now()
        answer = alc_scc_decomposed_graph.lcr_query(source, target, query_set)
        end = datetime.datetime.now()
        assert answer == False
        start = datetime.datetime.now()
        end = datetime.datetime.now()
        false_answer_times.append((start - end).microseconds)
    average = sum(false_answer_times) / len(false_answer_times)
    print('Average time for false queries {}'.format(average))

if __name__ == '__main__':
    main()