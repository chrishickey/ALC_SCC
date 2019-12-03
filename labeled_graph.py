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


class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, target, label):
        self.edges.append((target, label))
