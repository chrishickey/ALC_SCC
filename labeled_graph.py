import random
class LabeledGraph(object):

    def __init__(self):
        self.vertices = {}
        self.label_set = set()

    def add_edge(self, source, target, label):
        source = int(source)
        if source not in self.vertices:
            self.vertices[source] = Vertex(source)
        self.vertices[source].add_edge(int(target), int(label))
        self.label_set.add(int(label))

    @classmethod
    def get_graph_from_file(cls, file_name):
        graph = LabeledGraph()
        with open(file_name, 'r') as f:
            for line in f:
                source, target, label = line.split()
                graph.add_edge(source, target, label)
        return graph

    def get_test_cases(self, number=50, label_size=4):
        true_test_cases = []
        false_test_cases = []
        while len(true_test_cases) < number or len(false_test_cases) < number:
            labels = random.sample(self.label_set, label_size)
            source, target = random.sample(self.vertices.keys(), 2)
            original_source = source
            if ((source, target, tuple(sorted(labels))) in true_test_cases) or \
                    ((source, target, tuple(sorted(labels))) in false_test_cases):
                continue
            queue = [source]
            visited = {id: False for id in self.vertices}
            not_false = False
            while queue:
                source = queue.pop(0)
                visited[source] = True
                if source == target:
                    if len(true_test_cases) < number:
                        true_test_cases.append((original_source, target, tuple(sorted(labels))))
                        if not len(true_test_cases) % 100:
                            print('Found {} True test cases'.format(len(true_test_cases)))
                    not_false = True
                    break
                for vertex in self.vertices[source].edges:
                    if vertex[0] in visited and visited[vertex[0]] == False and vertex[1] in labels:
                        queue.append(vertex[0])
            if len(false_test_cases) >= number or not_false:
                continue
            false_test_cases.append((original_source, target, tuple(sorted(labels))))
            if not len(false_test_cases) % 100:
                print('Found {} False test cases'.format(len(false_test_cases)))
        return true_test_cases, false_test_cases


class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, target, label):
        self.edges.append((target, label))
