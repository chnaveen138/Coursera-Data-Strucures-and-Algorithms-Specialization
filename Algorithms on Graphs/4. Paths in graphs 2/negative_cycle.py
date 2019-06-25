# Source code in python3
class Graph:
    def __init__(self, numNodes, numEdges):
        self.weights = dict();
        self.adjacencyList = dict();
        self.distances = dict();
        self.numNodes = numNodes;
        self.numEdges = numEdges;
        self.edges = self.weights.keys();
    def relaxAllEdges(self):
        anyRelax = 0;
        for edge in self.edges:
            u = edge[0];
            v = edge[1];
            comparingWeight = self.distances[u] + self.weights[(u,v)];
            if(self.distances[v] > comparingWeight):
                self.distances[v] = comparingWeight;
                anyRelax = 1;
        return anyRelax;
    def detectNegitiveCycle(self):
        for vertex in self.adjacencyList.keys():
            self.distances[vertex] = 99999999999999999;
        self.distances[1] = 0;
        for i in range(self.numNodes-1):
            self.relaxAllEdges();
        return self.relaxAllEdges();

numNodes, numEdges = map(int, input().split());
graph = Graph(numNodes, numEdges);
for i in range(1, numNodes+1):
    graph.adjacencyList[i] = [];
for i in range(numEdges):
    vertex1, vertex2, weight = map(int, input().split());
    graph.adjacencyList[vertex1].append(vertex2);
    graph.weights[(vertex1, vertex2)] = weight;
print(graph.detectNegitiveCycle());